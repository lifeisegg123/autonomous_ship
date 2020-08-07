#!/usr/bin/env python
from handleLidar import Lidar
from handleImu import Imu

import rospy

from autonomous_ship.msg import motorValue


class Ship:
    gpsCoordination = [[100, 10], [500, 300], [600, 100]]

    motorPub = rospy.Publisher('motor', motorValue, queue_size=10)

    lidar = Lidar()
    imu = Imu()

    def runSubscribes(self):
        self.lidar.handleLidar()
        self.imu.handleImu()

    def publishMotor(self):
        self.motorPub.publish()

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        self.runSubscribes()
        while not rospy.is_shutdown():
            # print(self.lidar.lidarDatas)
            self.publishMotor()
            rospy.sleep(1)


if __name__ == '__main__':
    try:
        a = Ship()
        a.init()
    except rospy.ROSInterruptException:
        pass
