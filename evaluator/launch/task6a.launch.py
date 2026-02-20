#!/usr/bin/env python3
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    script = os.path.join(
        get_package_share_directory('evaluator'),
        'task6a',
        'task6a.py'
    )

    task6a = ExecuteProcess(
        cmd=['/usr/bin/python3', script],
        output='screen',
    )

    ld = LaunchDescription()
    ld.add_action(task6a)
    return ld
