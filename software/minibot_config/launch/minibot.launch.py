from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    edu_drive_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('minibot_config'),
                'launch',
                'edu_drive_minibot.launch.py'
            )
        )
    )

    lidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('minibot_config'),
                'launch',
                'tmini_launch.py'
            )
        )
    )

    minibot_scan_fusion_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('minibot_scan_fusion'),
                'launch',
                'minibot_scan_fusion.launch.py'
            )
        )
    )

    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('slam_toolbox'),
                'launch',
                'online_sync_launch.py'
            )
        ),
        launch_arguments={
            'slam_params_file': os.path.join(
                get_package_share_directory('minibot_config'),
                'params',
                'slam_config.yaml'
            )#'/home/user/ros2_ws/src/slam_config.yaml',
        }.items()
    )

    return LaunchDescription([
        edu_drive_launch,
        lidar_launch,
        minibot_scan_fusion_launch,
        slam_launch,
        #nav2 launch,
    ])