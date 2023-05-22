# These are some very common commands.
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
```
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim:=True map:=~/HomeDirect_ws/config/Maps/tb3_map.yaml
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