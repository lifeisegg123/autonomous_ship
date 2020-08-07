#!/usr/bin/env python2
import rospy

from sensor_msgs.msg import LaserScan


class Lidar:
    result = 0

    def callback(self, msg):
        lidarData = []
        print("Quaternoion =========================================================================================")
        indexStart = 0
        for i in range(44, 360, 45):
            lidarData.append(msg.ranges[indexStart:i])
            indexStart = i
        for i, data in enumerate(self.lidarData):
            if min(data) < 1:
                result = i + 1

    def handleLidar(self):
        sub = rospy.Subscriber('scan', LaserScan, self.callback)
