#!/usr/bin/env python3

import sys
import json
from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

FILENAME = '/home/dev/HomeDirect_ws/config/' + str(sys.argv[1]) + '.json'
# Daten aus der Datei lesen
def read_from_file():
    with open(FILENAME, 'r') as openfile:
        return json.load(openfile)

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=100.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

class TaginfoSubscriber(Node):
    

    # Subscribes to the 'taginfo' topic
    def __init__(self):
        super().__init__('taginfo_subscriber')
        self.subscription = self.create_subscription(
            String, # msg type
            'tag_info', # topic
            self.taginfo_callback, # reference "output" function
            10) # queue size
        self.subscription  # prevent unused variable warning
        self.minimal_client = MinimalClientAsync()
        self.get_logger().info("Taginfo subscriber has been started")

    def shutdown(self):
        self.minimal_client.destroy_node()
        self.destroy_node()
        rclpy.shutdown()
    # Print the received tag info to the terminal
    def taginfo_callback(self, msg):
        self.get_logger().info('RFID read: "%s"' % msg.data)
        msg.data = msg.data.replace(" ", "")
        file_content = dict(read_from_file())
        x = file_content[str(msg.data)][0]
        y = file_content[str(msg.data)][1]
        print(str(x) + " " + str(y))
        response = self.minimal_client.send_request(int(x * 1000), int(y * 1000))
        self.minimal_client.get_logger().info(
        'Navigation to  %d + %d completed. answer: %d' %
        (x, y, response.sum))


def main():
    rclpy.init()

    taginfo_subscriber = TaginfoSubscriber()
    rclpy.spin(taginfo_subscriber)
    
    taginfo_subscriber.shutdown()
    


if __name__ == '__main__':
    main()