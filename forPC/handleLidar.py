#!/usr/bin/env python2
import rospy

from sensor_msgs.msg import LaserScan


class Lidar:
    lidarData = []

    def callback(self, msg):
        self.lidarData = []

        self.lidarData = msg.ranges[269:]
        self.lidarData.append(msg.ranges[:89])
        print lidarData
        """ indexStart = 0
        for i in range(44, 360, 45):
            lidarData.append(msg.ranges[indexStart:i])
            indexStart = i
        for i, data in enumerate(self.lidarData):
            if min(data) < 1:
                result = i + 1
 """

    def handleLidar(self):
        sub = rospy.Subscriber('scan', LaserScan, self.callback)
