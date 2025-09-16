#!/bin/bash

# Color functions using printf for compatibility
color_red() { printf '\033[31m%s\033[0m\n' "$1"; }
color_green() { printf '\033[32m%s\033[0m\n' "$1"; }
color_yellow() { printf '\033[33m%s\033[0m\n' "$1"; }
color_blue() { printf '\033[34m%s\033[0m\n' "$1"; }
color_magenta() { printf '\033[35m%s\033[0m\n' "$1"; }
color_cyan() { printf '\033[36m%s\033[0m\n' "$1"; }
color_yellow_multiline() {
  printf '\033[33m%s\n%s\n%s\n%s\n%s\033[0m\n' "$1" "$2" "$3" "$4" "$5"
}

color_cyan "🚀 Starting ROS nodes and environment setup..."

color_green "✔ Launching: roscore"
color_yellow "Command: roscore"
gnome-terminal --title="roscore" -- bash -c "roscore; exec bash"
sleep 1

color_green "✔ Launching: voice_tester.py node"
color_yellow "Command: rosrun humanoid voice_tester.py"
gnome-terminal --title="voice_tester" -- bash -c "rosrun humanoid voice_tester.py; exec bash"
sleep 1

color_green "✔ Launching: eye_tracker.py node"
color_yellow "Command: rosrun humanoid eye_tracker.py"
gnome-terminal --title="eyetracker" -- bash -c "rosrun humanoid eye_tracker.py; exec bash"
sleep 1

color_green "✔ Launching: merger.py node"
color_yellow "Command: rosrun humanoid merger.py"
gnome-terminal --title="merger" -- bash -c "rosrun humanoid merger.py; exec bash"
sleep 1

color_green "✔ Launching: tester_node.py node"
color_yellow "Command: rosrun humanoid tester_node.py"
gnome-terminal --title="tester_node" -- bash -c "rosrun humanoid tester_node.py; exec bash"
sleep 1


color_magenta "⏳ Running directory navigation and API server start..."
printf '\033[33m%s\n%s\n%s\n%s\n%s\033[0m\n' "Commands:" "source ROS environment" "roscd humanoid" "cd .. && cd src/humanoid/src" "adk api_serve"
gnome-terminal --title="api_serve" -- bash -c "
source /opt/ros/noetic/setup.bash;
source /home/ubuntu/Desktop/git_codes/Humanoid-VIT/devel/setup.bash;
ls;
cd veronica_agent;
ls -a;
cat .env
set -a; source .env; set +a;
cd ..
adk api_server;
exec bash
"
sleep 1


color_cyan "✅ All terminals launched successfully! Monitor each process in its window."
sleep 1
