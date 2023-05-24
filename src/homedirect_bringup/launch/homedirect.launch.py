from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    rfid_publisher_node = Node(
        package="tb3_rfid",
        executable="rfid_publisher",
    )

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

    return ld