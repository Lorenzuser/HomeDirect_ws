from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy

rclpy.init()

nav = BasicNavigator()
#...
nav.setInitialPose(init_pose)
nav.waitUntilNav2Active() # if autostarted, else use `lifecycleStartup()`
#...
path = nav.getPath(init_pose, goal_pose)
smoothed_path = nav.smoothPath(path)
#...
nav.goToPose(goal_pose)
while not nav.isTaskComplete():
	feedback = nav.getFeedback()
	if feedback.navigation_duration > 600:
		nav.cancelTask()
#34...
result = nav.getResult()
if result == TaskResult.SUCCEEDED:
    print('Goal succeeded!')
elif result == TaskResult.CANCELED:
    print('Goal was canceled!')
elif result == TaskResult.FAILED:
    print('Goal failed!')