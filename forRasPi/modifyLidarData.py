#!/usr/bin/env python2
import rospy

from autonomous_ship.msg import lidar
from sensor_msgs.msg import LaserScan


def callback(msg):
    lidarMsg = lidar()
    lidarData = list(msg.ranges[540:])
    lidarData.extend(list(msg.ranges[0:180]))

    lidarMsg.lidarData = lidarData
    print len(lidarData)
    pub.publish(lidarMsg)


if __name__ == "__main__":
    rospy.init_node("lidarModifier")
    sub = rospy.Subscriber('scan', LaserScan, callback)
    pub = rospy.Publisher("lidar", lidar, queue_size=10)
    rospy.spin()
