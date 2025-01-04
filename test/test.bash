#!/bin/bash
# SPDX-FileCopyrightText: 2025 AkariHirohara <a.hirohara.0526@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build || { echo "Build failed"; exit 1; }
source $dir/.bashrc
timeout 30 ros2 run homework bitcoin_publisher > /tmp/homework.log

sleep 5

ros2 topic echo /bitcoin_price |
grep 'bitcoin_price:'
