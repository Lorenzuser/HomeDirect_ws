#!/usr/bin/env python3

# This is a program to publish 'id' and 'text' which were perviously written to the RFID tag 
# (see ~/Projekt--HomeDirect/RFID/Write.py)

import rclpy
from rclpy.node import Node
# thes following two lines are from https://pimylifeup.com/raspberry-pi-rfid-rc522/ 
# (site also referenced elsewhere in this project)
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
# Allows the use of the String message type
from std_msgs.msg import String

# following code orientates itself acording ~/Projekt--HomeDirect/RFID/Read.py 
# as well as ~/my_robot_controller/draw_circle.py

# Create a new class which is a subclass of the Node class
class TagInfoNode(Node):

    def __init__(self):
        # call super() and pass the name of the node
        super().__init__("rfid_reader")
        # Create Publisher 
        self.tag_info_pub_ = self.create_publisher(
            String, "tag_info", 10) # (message type, topic name, queue size)
        # Create timer
        self.timer_ = self.create_timer(
            # Read and publish tag info every second
            1.0, self.publish_tag_info)
        # reader = SimpleMFRC522()
        # Let them know node is running
        self.get_logger().info("Read tag info node has been started")   

    # Create a function to read and publish the tag info
    def publish_tag_info(self):
        # define 'reader' , this will be used to read the tag info
        reader = SimpleMFRC522()

        # Programm-Elements from ~/RFID/Read.py ~/RFID/AiPaste.py 
        # 'try' statement used to catch errors and clean up propperly
        try:
            # write the tag info to 'id' and 'text'
            id, text = reader.read()
            # create message by calling the String message type
            msg = String()
            # fill the message with the tag info
            msg.data = "ID: " + str(id) + " Text: " + text
            # publish the message
            self.tag_info_pub_.publish(msg)
            # print the tag info to the terminal
            self.get_logger().info('Tag ID: %s' % id)
            # Let them know the tag info was published
            self.get_logger().info("Tag info published")

        # handle exiting the program
        # I am not sure if this should go here or in the main function
        finally:
            # clean up GPIO pins
            GPIO.cleanup()
        

def main(args=None):
    rclpy.init(args=args)
    node = TagInfoNode()
    rclpy.spin(node)
    rclpy.shutdown()

        
