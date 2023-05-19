#!/usr/bin/env python3

# This programm is used to subscribe the tag information from the RFID reader and output 'id' and 'text' of the read tag


import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TaginfoSubscriber(Node):

    # Subscribes to the 'taginfo' topic
    def __init__(self):
        super().__init__('taginfo_subscriber')
        self.subscription = self.create_subscription(
            String, # msg type
            'taginfo', # topic
            self.taginfo_callback, # reference "output" function
            10) # queue size
        self.subscription  # prevent unused variable warning

    # Print the received tag info to the terminal
    def taginfo_callback(self, msg):
        self.get_logger().info('RFID read: "%s"' % msg.data)


# use the main function to start the node above
def main(args=None):

    rclpy.init(args=args)
    taginfo_subscriber = TaginfoSubscriber()
    rclpy.spin(taginfo_subscriber)
    taginfo_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
