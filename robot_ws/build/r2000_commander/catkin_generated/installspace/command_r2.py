#!/usr/bin/env python3
from multiprocessing.connection import wait
import sys, rospy, tf, moveit_commander, random
import copy
from geometry_msgs.msg import Pose, Point, Quaternion
from gazebo_msgs.msg import ContactsState
from time import sleep

class R2ChessboardWrapper:
    def __init__(self):
        self.arm = moveit_commander.MoveGroupCommander("arm")
        self.hand = moveit_commander.MoveGroupCommander("hand")
        self.arm.set_goal_position_tolerance(0.01)
        self.arm.set_goal_orientation_tolerance(0.1)
        self.arm.set_planning_time(0.1)
        self.arm.set_max_acceleration_scaling_factor(.8)
        self.arm.set_max_velocity_scaling_factor(.8)
        self.isBoxPresent = False
        self.subscriber = rospy.Subscriber('knife_bumper', ContactsState, self.callback)

    def callback(self,ContactData):
        if (len(ContactData.states) != 0):
            self.isBoxPresent = True

    def validPose(self,x, y, z, phi, theta, psi):
        orient = Quaternion(*tf.transformations.quaternion_from_euler(phi, theta, psi))
        pose = Pose(Point(x, y, z), orient)
        return pose

    def setPose(self, x, y, z, phi, theta, psi):
        orient = Quaternion(*tf.transformations.quaternion_from_euler(phi, theta, psi))
        pose = Pose(Point(x, y, z), orient)
        self.arm.set_pose_target(pose)
        self.arm.go(True)
    
    def prelievo(self):
        joint_goal = self.arm.get_current_joint_values()
        joint_goal[0] = -0.55
        joint_goal[1] = 1.04
        joint_goal[2] = -0.28
        joint_goal[3] = 6.28
        joint_goal[4] = -0.2
        joint_goal[5] = -4.16
        self.arm.go(joint_goal, wait=True)

    def boa(self):
        joint_goal = self.arm.get_current_joint_values()
        joint_goal[0] = 0
        joint_goal[1] = 0.69
        joint_goal[2] = -0.62
        joint_goal[3] = 3.14
        joint_goal[4] = 0.29
        joint_goal[5] = -3.14
        self.arm.go(joint_goal, wait=True)

    def deposito(self):
        joint_goal = self.arm.get_current_joint_values()
        joint_goal[0] = 0.55
        joint_goal[1] = 1.04
        joint_goal[2] = -0.28
        joint_goal[3] = 3.14
        joint_goal[4] = 0.2
        joint_goal[5] = 1.02
        self.arm.go(joint_goal, wait=True)

    def pickBox(self):
        joint_goal = self.hand.get_current_joint_values()
        joint_goal[0] -= 0.06
        joint_goal[1] += 0.06
        while (not r2w.isBoxPresent):
            sleep(0.5)
            pass
        self.hand.go(joint_goal, wait=True)
        self.isBoxPresent = False

    def openHand(self):
        joint_goal = self.hand.get_current_joint_values()
        joint_goal[0] = 0
        joint_goal[1] = 0
        self.hand.go(joint_goal, wait=True)

    def rilascio(self):
        joint_goal = self.hand.get_current_joint_values()
        joint_goal[0] += 0.0105
        joint_goal[1] -= 0.0105
        self.hand.go(joint_goal, wait=True)

    def pickCartesianPath(self):
        waypoints = []
        prelievo = self.validPose(1.5,-0.95,2, 3.14, 0, 1.57)
        waypoints.append(copy.deepcopy(prelievo))
        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0 disabling:
        plan, fraction = self.arm.compute_cartesian_path(
                                        waypoints,   # waypoints to follow
                                        0.01,        # eef_step
                                        0.0)         # jump_threshold
        self.arm.execute(plan,wait=True)
        # Note: We are just planning, not asking move_group to actually move the robot yet:
        #return plan, fraction
    
    def placeCartesianPath(self,place_pose):
        waypoints = []
        boa_prelievo = self.validPose(1.5,-0.95,2.3, 3.14, 0, 1.57)
        boa = self.validPose(1.5,0,2.5, 3.14, 0, 1.57)
        boa_deposito = self.validPose(1.5,0.95,2.3, 3.14, 0, 1.57)
        wpose = copy.deepcopy(place_pose)
        wpose.position.z += 0.5
        waypoints.append(copy.deepcopy(wpose))
        #deposito = self.validPose(1.5,0.95,2, 3.14, 0, 1.57)
        #waypoints.append(copy.deepcopy(boa_prelievo))
        #waypoints.append(copy.deepcopy(boa))
        #waypoints.append(copy.deepcopy(boa_deposito))
        waypoints.append(copy.deepcopy(place_pose))
        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0 disabling:
        plan, fraction = self.arm.compute_cartesian_path(
                                        waypoints,   # waypoints to follow
                                        0.01,        # eef_step
                                        0.0)         # jump_threshold
        self.arm.execute(plan,wait=True)
        # Note: We are just planning, not asking move_group to actually move the robot yet:
        #return plan, fraction

    def home(self):
        waypoints = []
        wpose = self.arm.get_current_pose().pose
        wpose.position.z += 0.5   # First move up (z)
        boa = self.validPose(1.5,0,2.5, 3.14, 0, 1.57)
        waypoints.append(copy.deepcopy(wpose))
        waypoints.append(copy.deepcopy(boa))
        plan, fraction = self.arm.compute_cartesian_path(
                                        waypoints,   # waypoints to follow
                                        0.01,        # eef_step
                                        0.0)         # jump_threshold
        self.arm.execute(plan,wait=True)

if __name__ == '__main__':
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('r2_chessboard_cli')

    sleep(10)

    r2w = R2ChessboardWrapper()

    #r2w.setPose(1.55,-0.95,0.4, 3.14, 0, 1.57) # prelievo
    #r2w.setPose(1.55,0,0.65, 3.14, 0, 0) #posizione wait/boa
    #r2w.setPose(1.55,0.95,0.4, 3.14, 0, -1.57) #deposito
    yPinza = 0.55
    boxX = 0.4
    boxY = 0.4
    offset = yPinza/2 - boxY/2

    accosto = 0.018 #12.5cm
    centro_deposito = r2w.validPose(1.5,0.95,2, 3.14, 0, 1.57)
    xDeposito = 1.5
    yDeposito = 0.95
    zDeposito = 2
    boxes=[]
    box1 = r2w.validPose(xDeposito+boxX/2+accosto, yDeposito+boxY/2+accosto - offset, zDeposito, 3.14, 0, 1.57)
    box2 = r2w.validPose(xDeposito-boxX/2-accosto, yDeposito+boxY/2+accosto - offset, zDeposito, 3.14, 0, 1.57)
    box3 = r2w.validPose(xDeposito+boxX/2+accosto, yDeposito-boxY/2-accosto - offset, zDeposito, 3.14, 0, 1.57)
    box4 = r2w.validPose(xDeposito-boxX/2-accosto, yDeposito-boxY/2-accosto - offset, zDeposito, 3.14, 0, 1.57)
    boxes.append(copy.deepcopy(box1))
    boxes.append(copy.deepcopy(box2))
    boxes.append(copy.deepcopy(box3))
    boxes.append(copy.deepcopy(box4))
    EEF_height = 0.4
    #r2w.setPose(1.5,-0.95,2.3, 3.14, 0, 1.57) # attesa prelievo
    #r2w.setPose(1.5,-0.95,2, 3.14, 0, 1.57)
    #r2w.setPose(1.5,-0.95,2, 3.14, 0, 1.57)
    
    r2w.openHand()    
    r2w.home()
    
    for box in boxes:
        r2w.pickCartesianPath()
        r2w.pickBox()
        r2w.home()
        r2w.placeCartesianPath(copy.deepcopy(box))
        r2w.rilascio()
        r2w.home()
        r2w.openHand()
    
    moveit_commander.roscpp_shutdown()


