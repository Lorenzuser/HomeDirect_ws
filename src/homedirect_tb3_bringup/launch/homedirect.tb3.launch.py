from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

# Launch file for the homedirect project
# Starts all the relevant self made nodes as well as the Bringup for the Turtlebot3
def generate_launch_description():
    ld = LaunchDescription()

    rfid_publisher_node = Node(
        package="tb3_rfid",
        executable="rfid_publisher",
    )

    turtlebot3_launch_file = IncludeLaunchDescription( # Das was ld.add_action referenziert
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('turtlebot3_bringup'), # Package-Pfad
                         'launch/robot.launch.py') # Pfad zur robot.launch.py Datei
        )
    )

    # Die Node die auf dem PC laufen soll müsste enfernt werden

    commander_node = Node(
        package="nav_main",
        executable="commander",
    )

    controller_main_node = Node(
        package="nav_main",
        executable="controller_main",
    )

    ld.add_action(rfid_publisher_node)
    ld.add_action(commander_node)
    ld.add_action(controller_main_node)
    ld.add_action(turtlebot3_launch_file)

    return ld