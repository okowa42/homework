#!/bin/bash
# SPDX-FileCopyrightText: 2025 AkariHirohara <a.hirohara.0526@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd /ros2_ws
colcon build
source $dir/.bashrc
timeout 30 ros2 run homework bitcoin_publisher > /tmp/homework.log

cat /tmp/homework.log |
grep 'bitcoin_price:'
