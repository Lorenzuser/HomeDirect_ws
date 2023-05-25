#!/usr/bin/env python3

import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations as tft

def main():
    rclpy.init()
    nav = BasicNavigator()

    q_x, q_y, q_z, q_w =  tft.quaternion_from_euler(0.0, 0.0, 0.0)
    InitPose = PoseStamped()
    InitPose.header.frame_id = 'map'
    InitPose.header.stamp = nav.get_clock().now().to_msg()
    InitPose.pose.position.x = 0.0
    InitPose.pose.position.y = 0.0
    InitPose.pose.position.z = 0.0
    InitPose.pose.orientation.x = q_x
    InitPose.pose.orientation.y = q_y
    InitPose.pose.orientation.z = q_z
    InitPose.pose.orientation.w = q_w

    nav.setInitialPose(InitPose)

    nav.waitUntilNav2Active()

    gq_x, gq_y, gq_z, gq_w =  tft.quaternion_from_euler(0.0, 0.0, 0.0)
    GoalPose = PoseStamped()
    GoalPose.header.frame_id = 'map'

    GoalPose.pose.position.x = 1.5
    GoalPose.pose.position.y = 0.0
    GoalPose.pose.position.z = 0.0
    GoalPose.pose.orientation.x = gq_x
    GoalPose.pose.orientation.y = gq_y
    GoalPose.pose.orientation.z = gq_z
    GoalPose.pose.orientation.w = gq_w

    nav.goToPose(GoalPose)

    while not nav.isTaskComplete():
        pass
    print("Task Complete" + str(nav.getResult()))
    rclpy.shutdown()

    
if __name__ == '__main__':
    main()








# from nav2_simple_commander.robot_navigator import BasicNavigator
# import rclpy

# rclpy.init()

# nav = BasicNavigator()
# #...
# nav.setInitialPose(init_pose)
# nav.waitUntilNav2Active() # if autostarted, else use `lifecycleStartup()`
# #...
# path = nav.getPath(init_pose, goal_pose)
# smoothed_path = nav.smoothPath(path)
# #...
# nav.goToPose(goal_pose)
# while not nav.isTaskComplete():
# 	feedback = nav.getFeedback()
# 	if feedback.navigation_duration > 600:
# 		nav.cancelTask()
# #34...
# result = nav.getResult()
# if result == TaskResult.SUCCEEDED:
#     print('Goal succeeded!')
# elif result == TaskResult.CANCELED:
#     print('Goal was canceled!')
# elif result == TaskResult.FAILED:
#     print('Goal failed!')