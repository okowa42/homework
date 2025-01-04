# SPDX-FileCopyrightText: 2025 AkariHirohara <a.hirohara.0526@gmail.com># SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    bitcoin_publisher = launch_ros.actionis.Node(
            package='homework',
            executable='bitcoin_publisher',
            name='bitcoin_publisher_node',
            output='screen',
            )
    subscriber = launch_ros.actions.Node(
            package='homework',
            executable='subscriber',
            name='bitcoin_subscriber_node',
            output='screen',
            )

    return launch.LaunchDescription([
        bitcoin_publisher,
        subscriber,
    ])

