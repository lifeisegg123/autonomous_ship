#!/usr/bin/env python2
import rospy

from autonomous_ship.msg import lidar


class Lidar:
    lidarData = []

    def callback(self, msg):
        self.lidarData = msg.lidarData

    def handleLidar(self):
        sub = rospy.Subscriber('lidar', lidar, self.callback)
