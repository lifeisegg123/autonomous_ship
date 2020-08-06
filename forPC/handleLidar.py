import rospy
import math
import time
from sensor_msgs.msg import LaserScan


class Lidar:
    lidarDatas = []

    def setLidarDatas(self, datas):
        self.lidarDatas = datas

    def callback(self, msg):
        lidarData = []
        print("Quaternoion =========================================================================================")
        indexStart = 0
        for i in range(44, 360, 45):
            lidarData.append(msg.ranges[indexStart:i])
            indexStart = i
        """ for i, data in enumerate(self.lidarData):
            if min(data) < 1:
                print(i) """
        self.setLidarDatas(lidarData)

    def handleLidar(self):
        sub = rospy.Subscriber('scan', LaserScan, self.callback)
