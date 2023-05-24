from launch import LaunchDescription
from launch_ros.actions import Node

# Launch file for the homedirect project
# Starts all the relevant self made nodes as well as the Bringup for the Turtlebot3
def generate_launch_description():
    ld = LaunchDescription()

    rfid_publisher_node = Node(
        package="tb3_rfid",
        executable="rfid_publisher",
    )


    # Die Node die auf dem PC laufen soll
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