# These are some very common commands, which may speed up the testing process, but may are device specific aswell
## WS
- **compile package:** colcon build (--packages-select my_package) (--symlink-install)
- ros2 topic echo /name = **usable for checking published Data**
- ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py = **Speicherort für Sim. world is changeable.**
- colcon build --symlink-install --packages-select nav_main

## Maps 
- map.pgm size * map.yaml resolution = size in m

## Launch
```
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```
Without RViz
```
ros2 launch nav2_bringup bringup.launch.py use_sim_time:=True map:=~/HomeDirect_ws/config/Maps/tb3_map.yaml
```
- With RViz
```
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim:=True map:=/home/dev/HomeDirect_ws/config/Maps/tb3_map.yaml
```
```
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
```
```
ros2 run nav2_map_server map_saver_cli -f ~/HomeDirect_ws/config/Maps/
```
```
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim:=True map:=/home/dev/HomeDirect_ws/config/Maps/Maps.yaml
```
- Set Init Pose(Change accordingly)
```
ros2 topic pub /initialpose geometry_msgs/msg/PoseWithCovarianceStamped "{header: {stamp: {sec: 0}, frame_id: 'map'}, pose: {pose: {position: {x: 3.45, y: 2.15, z: 0.0}, orientation: {z: 1.0, w: 0.0}}}}"
```
