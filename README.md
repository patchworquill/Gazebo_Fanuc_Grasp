# Gazebo_Fanuc_Grasp
ROS/Gazebo simulation of a Fanuc Industrial Robot performing Pick&Place tasks:
- packing boxes
- OpenCV pipeline to autonomously detect and pick boxes 

## Dependencies
- ROS Noetic
- MoveIt! (for Noetic) 
- Gazebo 11
- Python 3.8.2
- OpenCV
- ros-gazebo, ros-control packages

## Usage
```
$ cd robot_ws
$ catkin_make
```
To Run Palletizing simulation (standard boxes) :
```
$ roslaunch fanuc_r2000ic_moveit_config palletizzation.launch
```
Or 
```
$ roslaunch fanuc_r2000ic_moveit_config palletizzation_costa.launch
```
To Run OpenCV detetction+PicPlace simulation (standard boxes) :
```
$ roslaunch fanuc_r2000ic_moveit_config opencv_palletizzation.launch
```

## TODO
- [ ] Do dockerfile



# RESOURCES
- example usage of xacro command (from xacro to urdf file) https://github.com/wrbernardoni/robot_tutorial_1/blob/master/scripts/play.sh
- passing params to xacro in launch https://answers.ros.org/question/38956/pass-parameters-to-xacro-in-launch-file/
- spawn xacro in gazebo https://answers.ros.org/question/70417/how-to-spawn-urdfxacro-file-into-gazebo/

- gazebo plugins http://gazebosim.org/tutorials?tut=ros_gzplugins
- bumper sensor gazebo https://answers.ros.org/question/29158/how-do-i-use-force-sensor-bumper-sensor-in-gazebo/ and
https://answers.ros.org/question/246448/getting-contact-sensorbumper-gazebo-plugin-to-work/ and 
https://answers.gazebosim.org//question/5355/adding-ros-integrated-contact-sensors/ and
http://gazebosim.org/tutorials?cat=sensors&tut=contact_sensor&ver=1.9-4.0
- Gazebo spawn script example! https://github.com/roboticist8/ros_gazebo_spawn_models/blob/master/spawn_urdf_sdf/src/spawn_sdf.cpp
- Gazebo bodywrench error https://answers.gazebosim.org//question/24764/gazebo-applybodywrench-throwing-errors/
- Gazebo scripting python (check Main exception !!!) https://answers.gazebosim.org//question/22125/how-to-set-a-models-position-using-gazeboset_model_state-service-in-python/
- Gazebo Gripper https://answers.ros.org/question/302358/anyone-whos-succeeded-with-grasping-using-ros-and-gazebo-what-advice-do-you-have-to-offer/ and
https://answers.ros.org/question/208735/pickup-object-in-gazebo-graspped-object-doesnt-move/ and 
https://answers.gazebosim.org/question/25267/cannot-control-gripper-to-grasp-object-in-gazebo/ and
https://github.com/Kinovarobotics/kinova-ros/issues/157

- ROS subscriber not up to date https://stackoverflow.com/questions/26415699/ros-subscriber-not-up-to-date

- Ros Control Explanation (all types of controller) https://www.rosroboticslearning.com/ros-control
- OSRF ariac warehouse http://gazebosim.org/ariac and https://bitbucket.org/osrf/ariac/src/master/
- Euler Angles Tutorial https://mathworld.wolfram.com/EulerAngles.html 

## Blogs
- ROS BOOKS http://wiki.ros.org/Books (Amazing book from O'Reiley 2015)
- Erdal's Blog (Gazebo integration) https://erdalpekel.de/
- Robotic Seabass (Docker..Jenkins..) https://roboticseabass.com/
- Mike Moore (Docker, Jupyter) http://moore-mike.com/index.html
- ETH course Autonomous Mobility on Demand: From Car to Fleet https://idsc.ethz.ch/education/lectures/duckietown.html
- ETH duckietown https://www.duckietown.org/instructors/classes/educational-resources
- Blog with ROS/Gazebo Integration https://www.codenong.com/cs110953023/

## Thesis & Papers
- Robotic arm pick-and-place tasks https://webthesis.biblio.polito.it/16766/1/tesi.pdf
- A ROS-based Workspace Control and Trajectory Planner for a Seven Degrees Of Freedom Robotic Arm https://amslaurea.unibo.it/10919/1/Alessandro_Santoni_Thesis_(abstract_ITA).pdf
- NAVIGATION AND GRASPING WITH A MOBILE MANIPULATOR: FROM SIMULATION TO EXPERIMENTAL RESULTS http://tesi.cab.unipd.it/62262/1/matteo_iovino_tesi.pdf
- Simultaneous localization and mapping: part I https://ieeexplore.ieee.org/document/1638022
- Davide Scaramuzzo Zurich PHD https://ieeexplore.ieee.org/author/37397688400
- IEEE Robotics & Automation Magazine https://ieeexplore.ieee.org/xpl/topAccessedArticles.jsp?punumber=100
- artificial intelligence in robotic palletization https://scholar.google.it/scholar?start=10&q=artificial+intelligence+in+robotic+palletization&hl=it&as_sdt=0,5&as_vis=1
- Goole's RL https://github.com/google-research/ravens/tree/master/ravens
- UR5 OpenCV pickplace https://github.com/lihuang3/ur5_ROS-Gazebo/blob/master/ur5_mp.py

## TOOLS 
- Mesh Cleaner https://www.hamzamerzic.info/mesh_cleaner/?
- Mass/Inertia online calculator
