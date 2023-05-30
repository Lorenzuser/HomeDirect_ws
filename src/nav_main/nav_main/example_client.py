#!/usr/bin/env python3

import sys
import json
from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

FILENAME = '/home/dev/HomeDirect_ws/config/' + str(sys.argv[2]) + '.json'
# Daten aus der Datei lesen
def read_from_file():
    with open(FILENAME, 'r') as openfile:
        return json.load(openfile)

class NameTagSubscriber(Node):

    # Subscribes to the 'taginfo' topic
    def __init__(self):
        super().__init__('name_tag_subscriber')
        self.subscription = self.create_subscription(
            String, # msg type
            'tag_info', # topic
            self.set_goal_callback, # reference "output" function
            10) # queue size
        self.subscription  # prevent unused variable warning
        self.minimal_client = MinimalClientAsync()
        self.get_logger().info("Taginfo subscriber has been started")

    # Print the received tag info to the terminal
    def set_goal_callback(self, msg):
        self.get_logger().info('RFID read: "%s"' % msg.data)
        # Ermittle Koordinaten die mit Ziel der jeweiligen Person übereinstimmen
        file_content = dict(read_from_file())
        ## Struktur der Datei: {Name: [x, y]} also [Name][Korordinate x/y ]
        # Name = 'msg.data' = 'text' 
        x = file_content[msg.data][0]
        y = file_content[msg.data][1]
        print(str(x) + " " + str(y))
        response = self.minimal_client.send_request(int(x * 1000), int(y * 1000))
        self.minimal_client.get_logger().info(
        'Navigation to  %d + %d completed. answer: %d' %
        (x, y, response.sum))

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=100.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request() 

    # gewünschte x und y Koordinaten werden an den Server gesendet
    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    rclpy.init()
    # Koordinaten zurücksetzen zum Initalisieren
    x = 0
    y = 0

    name_tag_subscriber = NameTagSubscriber()
    minimal_client = MinimalClientAsync()
    try:
        if sys.argv[3] is not None:
            x = sys.argv[1]
            y = sys.argv[2]
    except IndexError:
    
    ## Dies soll in eine Callbakc Funktion des RFID Subscribers ##
    #   
        # Ermittle Koordinaten die mit Ziel der jeweiligen Person übereinstimmen
        file_content = dict(read_from_file())
        ## Struktur der Datei: {Name: [x, y]} also [Name][Korordinate x/y ]
        x = file_content[sys.argv[1]][0]
        y = file_content[sys.argv[1]][1]
        print(str(x) + " " + str(y))
        response = minimal_client.send_request(int(x * 1000), int(y * 1000))
        minimal_client.get_logger().info(
        'Navigation to  %d + %d completed. answer: %d' %
        (x, y, response.sum))
    #
    ## - ##

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()