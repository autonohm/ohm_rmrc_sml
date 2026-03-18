#!/usr/bin/python3
# Copyright 2020, EAIBOT
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import LifecycleNode
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import LogInfo

import lifecycle_msgs.msg
import os


def generate_launch_description():
    share_dir_minibot = get_package_share_directory('minibot_config')
    share_dir = get_package_share_directory('ydlidar_ros2_driver')
    #parameter_file = LaunchConfiguration('params_file')
    params_file1 = LaunchConfiguration('params_file1')
    params_file2 = LaunchConfiguration('params_file2')
    node_name = 'ydlidar_ros2_driver_node'

    params_declare1 = DeclareLaunchArgument('params_file1',
                                           default_value=os.path.join(
                                               share_dir_minibot, 'params', 'Tmini1.yaml'),
                                           description='Path to the ROS2 parameters file to use.')

    driver_node1 = Node(package='ydlidar_ros2_driver',
                                executable='ydlidar_ros2_driver_node',
                                name='ydlidar_ros2_driver_node1',
                                output='screen',
                                emulate_tty=True,
                                parameters=[params_file1],
                                namespace='lidar1',
                                )
    tf2_node1 = Node(package='tf2_ros',
                    executable='static_transform_publisher',
                    name='static_tf_pub_laser1',
                    arguments=['0.1438', '-0.0787', '0.081','0', '1', '0', '0','base_link','laser_frame1'],
                    )
    
    params_declare2 = DeclareLaunchArgument('params_file2',
                                           default_value=os.path.join(
                                               share_dir_minibot, 'params', 'Tmini2.yaml'),
                                           description='Path to the ROS2 parameters file to use.')

    driver_node2 = Node(package='ydlidar_ros2_driver',
                                executable='ydlidar_ros2_driver_node',
                                name='ydlidar_ros2_driver_node2',
                                output='screen',
                                emulate_tty=True,
                                parameters=[params_file2],
                                namespace='lidar2',
                                )
    tf2_node2 = Node(package='tf2_ros',
                    executable='static_transform_publisher',
                    name='static_tf_pub_laser2',
                    arguments=['-0.105', '0.0787', '0.081','1', '0', '0', '0','base_link','laser_frame2'],
                    )
    return LaunchDescription([
        params_declare1,
        driver_node1,
        tf2_node1,
        params_declare2,
        driver_node2,
        tf2_node2,
    ])
