#!/usr/bin/env python2
import rospy

from autonomous_ship.msg import lidar
from sensor_msgs.msg import LaserScan


def callback(msg):
    lidarMsg = lidar()
    lidarData = list(msg.ranges[270:])

    lidarData.extend(list(msg.ranges[0:90]))

    lidarMsg.lidarData = lidarData
    pub.publish(lidarMsg)


if __name__ == "__main__":
    rospy.init_node("lidarModifier")
    sub = rospy.Subscriber('scan', LaserScan, callback)
    pub = rospy.Publisher("lidar", lidar, queue_size=10)
    rospy.spin()
