#! /usr/bin/env python3

import rospy 
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import math

def my_publisher():
    # control part

    rospy.init_node('mir130_1_control_node')
    control_publisher = rospy.Publisher('/mir1350v5_1/abb_arm_controller/command', JointTrajectory, queue_size=10)

    while not rospy.is_shutdown():
        
        msg = JointTrajectory()

        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = ''
        msg.joint_names = ['abbLink2_revJoint', 'abbLink3_revJoint', 'abbLink4_revJoint', 'abbLink5_revJoint', 'abbLink6_revJoint', 'abbLink7_revJoint']
 
        point = JointTrajectoryPoint()
        j1 = 0
        j2 = 0
        j3 = 0
        j4 = 0
        j5 = 0
        j6 = 0

        point.positions = [j1, j2, j3, j4, j5, j6]
        point.velocities = []
        point.accelerations = []
        point.effort = []
        point.time_from_start = rospy.Duration(.5)

        msg.points.append( point )

        control_publisher.publish( msg )
        rospy.loginfo( msg ) 


if __name__ == '__main__':

    my_publisher()