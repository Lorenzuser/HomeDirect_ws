#!/usr/bin/env python3

# This is a program to publish 'id' and 'text' which were perviously written to the RFID tag 
# (see ~/Projekt--HomeDirect/RFID/Write.py)

# import necessary packages & co.
import rclpy
from rclpy.node import Node
# thes following two lines are from https://pimylifeup.com/raspberry-pi-rfid-rc522/ 
# (site also referenced elsewhere in this project)
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from std_msgs.msg import String

# following code orientates itself acording ~/Projekt--HomeDirect/RFID/Read.py 
# as well as ~/my_robot_controller/draw_circle.py

# Create a new class which is a subclass of the Node class
class TagInfoNode(Node):

    def __init__(self):
        super().__init__("rfid_reader") # node name might better be changed
        # Create Publisher 
        self.publisher_ = self.create_publisher(
            String, "tag_info", 10) # (message type, topic name, queue size)
        # Create timer
        self.timer_ = self.create_timer(
            1.0, self.publish_tag_info) # Read and publish tag info every second
        # reader = SimpleMFRC522()
        # Let them know node is running
        self.get_logger().info("Read tag info node has been started")   

    # Create a function to read and publish the tag info
    def publish_tag_info(self):
        # define 'reader' , this will be used to read the tag info
        reader = SimpleMFRC522()

        # referencing: ~/RFID/Read.py ~/RFID/AiPaste.py 
        # 'try' + 'finnaly' in order to: catch errors and clean up propperly
        try:
            # define 'id' and 'text' 
            id, text = reader.read()
            # create message by calling 'String' message type
            msg = String()
            # fill message 
            msg.data = text
            # publish message
            self.publisher_.publish(msg)
            # print tag info 
            self.get_logger().info('Tag ID: %s' % id + ' Tag text: %s' % text)
            # print Node Status
            self.get_logger().info("Tag info published")

        finally:
            # clean up GPIO pins
            GPIO.cleanup()
        

def main(args=None):
    rclpy.init(args=args)
    node = TagInfoNode()
    rclpy.spin(node)
    rclpy.shutdown()

        
