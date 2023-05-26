#!/usr/bin/env python3#

# Subscribes to the 'tag_info' topic
# and helps the Navigation-Node to determine the goal(right Room) by providing the patient's tag info

import sys

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TagInfoClient(Node):

    # Create Subscriber and Client
    def __init__(self):
        super().__init__('tag_info_client') 
        self.subscription = self.create_subscription(
            String, # msg type
            'tag_info', # topic
            self.taginfo_callback, # call for the programm to make client requests
            10) # queue size
        self.client = self.create_client(String, 'tag_info_service') # client is called 'tag_info_service'
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.req = String.Request() # create storrage for the request
        # Log
        self.get_logger().info("Taginfo subscriber has been started")    

    # Handle received tag info
    def taginfo_callback(self, msg):
            self.get_logger().info('Received tag info: "%s"' % msg.data)
            self.req.data = msg.data # fill the request with the received tag info
            self.future = self.client.call_async(self.req)
            self.future.add_done_callback(self.client_callback) # Log-Feedback callback

    # Log-Feedback
    def client_callback(self, future):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info('Tag request has been sent')
            else:
                self.get_logger().info('Server failed to process the request')
        except Exception as e:
            self.get_logger().info(f'Tag request failed: {e}')

def main(args=None):
    rclpy.init(args=args)
    taginfo_client = TagInfoClient()
    rclpy.spin(taginfo_client)
    taginfo_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
                


        


