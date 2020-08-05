import rospy
import math
import time
from sensor_msgs.msg import LaserScan


def callback(msg):
    print("Quaternoion =========================================================================================")
    indexStart = 0
    for i in range(44, 360, 45):
        print(msg.ranges[indexStart:i])

        indexStart = i
    print(msg.ranges)
    time.sleep(2)


if __name__ == "__main__":
    rospy.init_node('getLidar')

    sub = rospy.Subscriber('scan', LaserScan, callback)

    rospy.spin()
