#!/usr/bin/env python2
import rospy
from autonomous_ship.msg import imu


class Imu:

    imuData = [0, 0]

    def handleImu(self):
        self.imuSub = rospy.Subscriber("Imu", imu, self.callbackImu)

    def callbackImu(self, msg):
        self.imuData[0] = msg.xAngle
        self.imuData[1] = msg.yAngle
