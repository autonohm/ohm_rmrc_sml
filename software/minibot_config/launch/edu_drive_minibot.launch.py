import os
import yaml

from launch import LaunchDescription
from launch_ros.actions import Node

from launch.substitutions import EnvironmentVariable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
   
    package_path = FindPackageShare('minibot_config')
    parameter_file = PathJoinSubstitution([
      package_path,
      'params',
      'edu_drive_minibot.yaml'
    ])

    edu_drive = Node(
      package='edu_drive_ros2',
      executable='edu_drive_ros2_node',
      name='edu_drive_ros2_node',
      parameters=[parameter_file],
      namespace=os.environ.get('EDU_ROBOT_NAMESPACE', "edu_sml"),
      output='screen'
    )  
    
    return LaunchDescription([
        edu_drive
    ])
