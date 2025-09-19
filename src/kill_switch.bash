#!/bin/bash

color_red() { printf '\033[31m%s\033[0m\n' "$1"; }
color_green() { printf '\033[32m%s\033[0m\n' "$1"; }
color_yellow() { printf '\033[33m%s\033[0m\n' "$1"; }
color_cyan() { printf '\033[36m%s\033[0m\n' "$1"; }

color_cyan "🛑 Starting kill switch to terminate all ROS terminal windows..."

pids_killed=0

kill_term() {
  local title="$1"
  color_yellow "Trying to close terminal with title: $title"

  # Find window id by title (case-sensitive)
  local win_id=$(wmctrl -l | grep "$title" | awk '{print $1}')

  if [ -n "$win_id" ]; then
    # Close the window gracefully
    xdotool windowclose "$win_id"
    color_green "✔ Successfully closed terminal window titled: '$title'"
    ((pids_killed++))
  else
    color_red "✖ No window found with title: '$title'"
  fi
}

kill_term "roscore"
sleep 1
kill_term "voice_tester"
sleep 1
kill_term "eyetracker"
sleep 1
kill_term "merger"
sleep 1
kill_term "tester_node"
sleep 1
kill_term "chat_node"
sleep 1
kill_term "api_serve"
sleep 1
kill_term "voice_serial"
sleep 1
kill_term "vision_serial"
sleep 1
kill_term "rqt_node"
sleep 1

if [ "$pids_killed" -gt 0 ]; then
  color_green "✅ All matched terminals have been terminated."
else
  color_red "⚠ No terminals were found or killed."
fi
