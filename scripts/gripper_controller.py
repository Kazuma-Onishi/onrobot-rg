#!/usr/bin/env python3

##########################
# Python Standard modules
##########################
import sys, os
import time
import atexit
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from time import sleep
#####################
# OnRobot module
#####################
from onrobot import RG

################
# ROS module
################
import rospy
import std_msgs.msg as std_msgs


class RG2Controller:
    def __init__(self, IP, PORT):
        self.rg = RG('rg2', IP, PORT)
        subscriber_for_control = rospy.Subscriber('/rg2_gripper/reference_width', std_msgs.Int16, self.control_rg2_gripper_by_width,queue_size=1)
        self.publisher = rospy.Publisher('/rg2_gripper/width_state', std_msgs.Int16, queue_size=1)
        self.rate = rospy.Rate(10)

    def get_gripper_width(self, e):
        msg = std_msgs.Int16()
        print(self.rg.get_status())
        msg.data = int(self.rg.get_width()) * 10
        self.publisher.publish(msg)

    def loop(self):
        rospy.spin()
        self.rate.sleep()

    def control_rg2_gripper_by_width(self, msg):
        width = msg.data
        while self.rg.get_status()[0]:
            return
        self.rg.move_gripper(width)

    def disconnect_rg2_gripper(self):
        self.rg.move_gripper(1100)

        while self.rg.get_status()[0]:
            pass

        self.rg.close_connection()
        print("[*] RG was closed")

def main():
    rospy.init_node('rg2_gripper_node')

    rg2_controller_node = RG2Controller('10.40.20.69', 502)

    atexit.register(rg2_controller_node.disconnect_rg2_gripper)

    while not rospy.is_shutdown():
        rg2_controller_node.loop()


if __name__ == '__main__':
    main()
