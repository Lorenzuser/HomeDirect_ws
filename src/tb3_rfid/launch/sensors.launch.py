from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource 
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
	return LaunchDescription([
		Node(
			package='tb3_rfid',
			executable='rfid_publisher'
		),
		IncludeLaunchDescription(
			PythonLaunchDescriptionSource(
				os.path.join(get_package_share_directory('turtlebot3_bringup'),
					'launch/robot.launch.py')
			)
		)
	])


