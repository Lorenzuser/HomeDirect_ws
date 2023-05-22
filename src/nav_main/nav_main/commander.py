import rclpy
from rclpy.node import Node
from nav2_msgs.action import NavigateToPose
import geometry_msgs.msg as geometry_msgs
from rclpy.action import ActionClient


class SimpleCommander(Node):

    def __init__(self):
        super().__init__('simple_commander')
        self.action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.action_client.wait_for_server()

    def send_goal(self, pose):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.pose.position = pose.position
        goal_msg.pose.pose.orientation = pose.orientation

        self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

    def feedback_callback(self, feedback_msg):
        # Hier kannst du den Fortschritt des Roboters überwachen
        pass


def main(args=None):
    rclpy.init(args=args)
    simple_commander = SimpleCommander()

    pose = geometry_msgs.PoseStamped()
    pose.pose.position.x = 10.0
    pose.pose.position.y = 200.0
    pose.pose.orientation.w = 1.0

    simple_commander.send_goal(pose)

    rclpy.spin(simple_commander)
    simple_commander.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()











# import rclpy
# from rclpy.node import Node
# from nav2_msgs.action import NavigateToPose
# import geometry_msgs.msg as geometry_msgs


# class SimpleCommander(Node):

#     def __init__(self):
#         super().__init__('simple_commander')
#         self.action_client = self.create_action_client(NavigateToPose, 'navigate_to_pose')
#         self.action_client.wait_for_server()

#     def send_goal(self, pose):
#         goal_msg = NavigateToPose.Goal()
#         goal_msg.pose.header.frame_id = 'map'
#         goal_msg.pose.pose.position = pose.position
#         goal_msg.pose.pose.orientation = pose.orientation

#         self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

#     def feedback_callback(self, feedback_msg):
#         # Hier kannst du den Fortschritt des Roboters überwachen
#         pass


# def main(args=None):
#     rclpy.init(args=args)
#     simple_commander = SimpleCommander()

#     pose = geometry_msgs.PoseStamped()
#     pose.pose.position.x = -1.20
#     pose.pose.position.y = -2.36
#     pose.pose.orientation.w = 0

#     simple_commander.send_goal(pose)

#     rclpy.spin(simple_commander)
#     simple_commander.destroy_node()
#     rclpy.shutdown()


# if __name__ == '__main__':
#     main()

