#!/bin/bash
# SPDX-FileCopyrightText: 2025 AkariHirohara <a.hirohara.0526@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build || { echo "Build failed"; exit 1; }
source $dir/.bashrc
timeout 30 ros2 launch homework bitcoin_subscribe.launch.py > /tmp/homework.log

cat /tmp/homework.log |
grep 'bitcoin_price:'
