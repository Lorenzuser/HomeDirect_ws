#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import sys
import json

FILENAME = '/home/dev/HomeDirect_ws/config/' + str(sys.argv[2]) + '.json'
# Daten aus der Datei lesen
def read_from_file():
    with open(FILENAME, 'r') as openfile:
        return json.load(openfile)
    
# Daten in die Datei schreiben
def write_to_file(data):
    with open(FILENAME, "w") as outfile:
        json.dump(data, outfile)

# Sub
class MapSubscriber(Node):
    def __init__(self):
        self.node = rclpy.create_node('my_subscriber')
        super().__init__('map_subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            'odom',
            self.callback,
            10
        )
        self.subscription
        print("init")

    def callback(self, msg):
        # Speichern der Position in einer Variable
        position_x = msg.pose.pose.position.x
        position_y = msg.pose.pose.position.y

        self.get_logger().info("Position: " + str(position_x) + " , " + str(position_y))
        
        # Speicher der Position in einer Datei
        content = dict(read_from_file())
  
        content.update({str(sys.argv[1]): [position_x, position_y]})
        write_to_file(content)
        self.get_logger().info(str(content))


        # Deactivate
        self.subscription.destroy()  # Subscriber zerstören
        self.node.destroy_node()  # Node zerstören
        exit(0)

def main(args=None):
    rclpy.init(args=args)
    node = MapSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


