# Veronica

Veronica is a ROS-based humanoid assistant project that combines:
- a ROS Node system for voice, vision, and sensor data
- an ADK/Google agent backend for conversational AI
- serial/device communication setup for robot movement/audio control

This project is designed to run on Ubuntu with ROS Noetic and Python 3.

## Best Ubuntu version for performance

Use Ubuntu 20.04 LTS (Focal Fossa) for the best compatibility and performance with this project.

Why:
- ROS Noetic officially targets Ubuntu 20.04
- Python 3 is the native runtime used here
- the scripts and environment setup in this workspace assume a desktop Ubuntu environment and ROS Noetic tooling

If you are on another Ubuntu version, this project may still work, but 20.04 is the most stable option for this codebase.

## Requirements

### Operating system
- Ubuntu 20.04 LTS (recommended)
- desktop version preferred, because the startup scripts use GNOME terminals

### ROS / system packages
- ROS Noetic
- catkin
- python3
- gnome-terminal
- wmctrl
- xdotool
- rosserial_python

### Python packages
Install these inside the project environment:

```bash
cd /path/to/Veronica
python3 -m pip install -r src/humanoid/src/requirements.txt
```

The dependency list in the project is:
- cvzone
- pipwin
- mediapipe
- opencv-python
- ffprobe
- gtts
- SpeechRecognition
- pyttsx3
- pygame
- sounddevice
- pydub
- google-adk

### Hardware / runtime assumptions
This project expects:
- USB serial devices for robot hardware
- microphone input
- webcam / camera stream
- local Google ADK server running on localhost:8000
- robot topics like `vision_node`, `voice_node`, `merger_node`, and `adk_server`

## Main project layout

```text
Veronica/
├── src/
│   ├── CMakeLists.txt              # catkin workspace entry point
│   ├── runner.bash                 # starts all nodes in separate terminals
│   ├── kill_switch.bash            # closes matching terminal windows
│   ├── rosserial/                  # ROS serial library dependency
│   └── humanoid/
│       ├── CMakeLists.txt          # package config for humanoid
│       ├── package.xml             # ROS package metadata
│       └── src/
│           ├── adk_node.py         # ROS bridge for user input / AI answer
│           ├── tester_node.py      # voice/audio testing node
│           ├── voice_tester.py     # speech + movement sync logic
│           ├── eye_tracker.py      # vision / eye tracking node
│           ├── merger.py           # merges vision + voice streams
│           └── veronica_agent/     # Google ADK agent logic
│               ├── agent.py
│               ├── prompts.py
│               ├── sub_agents/
│               └── __init__.py
└── devel/ / build / install/       # generated ROS build outputs
```

## What actually does the work

The real logic is split across a few important files:

### 1) `src/humanoid/src/veronica_agent/agent.py`
This is the main AI agent definition. It loads the environment model, sets up the agent, and registers sub-agents.

### 2) `src/humanoid/src/adk_node.py`
This is the ROS bridge. It:
- initializes a ROS node
- reads user prompt text from the terminal
- sends the question to the ADK server
- publishes the final response back on a ROS topic

### 3) `src/humanoid/src/merger.py`
This combines data from the vision and voice streams into a single merged ROS message.

### 4) `src/humanoid/src/voice_tester.py`
This handles speech generation, playback, and synchronization of voice-driven movement/angles.

### 5) `src/humanoid/src/eye_tracker.py`
This captures camera/vision data and publishes position information.

## Which files are mostly optional or useless

These are not the core logic:

- `src/kill_switch.bash`  
  This is only a cleanup helper. It closes terminal windows by title, but the actual robot logic does not depend on it.

- `build/`, `devel/`, and `install/`  
  These are generated ROS build artifacts. They are not the application logic.

- `src/rosserial/`  
  This is a dependency/library tree used for serial communication; it is important only if you need ROS serial support for hardware.

- `src/CMakeLists.txt`  
  This is the workspace-level CMake bootstrap file, not the main application implementation.

## How to start the project

### Option 1: use the provided runner script
This is the easiest method because the project expects multiple terminals:

```bash
cd /path/to/Veronica
source /opt/ros/noetic/setup.bash
catkin_make
source devel/setup.bash
bash src/runner.bash
```

This script launches:
- roscore
- serial nodes for devices
- tester nodes
- voice and vision nodes
- merger node
- ADK API server
- chat node
- rqt graph

### Option 2: start manually
If you want more control:

```bash
source /opt/ros/noetic/setup.bash
cd /path/to/Veronica
catkin_make
source devel/setup.bash
roscore
```

Then open separate terminals and run:

```bash
rosrun rosserial_python serial_node.py _port:=/dev/ttyUSB0 _baud:=57600 __name:=usb0_node
rosrun rosserial_python serial_node.py _port:=/dev/ttyUSB1 _baud:=57600 __name:=usb1_node
rosrun humanoid tester_node.py
rosrun humanoid voice_tester.py
rosrun humanoid eye_tracker.py
rosrun humanoid merger.py
```

For the agent backend:

```bash
cd /path/to/Veronica/src/humanoid/src/veronica_agent
source .env
adk api_server
```

Then run:

```bash
rosrun humanoid adk_node.py
```

## Important notes about the startup script

The launcher script uses hardcoded paths and terminal titles, for example:

```bash
source /home/ubuntu/Desktop/git_codes/Humanoid-VIT/devel/setup.bash
cd humanoid/src/veronica_agent/
set -a; source .env; set +a;
adk api_server
```

This means you may need to update the paths if your workspace is not in the same folder.

Also, the script depends on:
- `gnome-terminal`
- `wmctrl`
- `xdotool`

If you are running in a minimal server or non-GNOME environment, the script may fail.

## Recommended setup

For best results:
- Ubuntu 20.04 LTS
- ROS Noetic
- desktop Ubuntu with GNOME
- Python 3.8+
- a working microphone and camera
- stable ADK server on `http://localhost:8000`
- hardware serial ports connected correctly

## Quick summary

- Best Ubuntu: Ubuntu 20.04 LTS
- Best starting method: `bash src/runner.bash`
- Main AI logic: `src/humanoid/src/veronica_agent/agent.py`
- Main ROS bridge: `src/humanoid/src/adk_node.py`
- Optional/cleanup file: `src/kill_switch.bash`
- Main requirements: ROS Noetic + Python 3 + project Python packages + GNOME desktop utilities

## Final note

This project is not a single-file app. It is a ROS robot control + AI assistant workflow with several nodes working together. The core work is distributed across the Python ROS nodes and the ADK agent configuration, while the runner script simply orchestrates the full startup sequence.
