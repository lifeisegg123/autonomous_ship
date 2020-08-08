#!/usr/bin/env python2
from handleLidar import Lidar
from handleImu import Imu
from handleGps import Gps
import rospy

from autonomous_ship.msg import motorValue


class Ship:
    gpsCoordinations = [[100, 10], [500, 300], [600, 100]]

    motorPub = rospy.Publisher('motor', motorValue, queue_size=10)
    motorValue = motorValue()

    lidar = Lidar()
    imu = Imu()
    gps = Gps()

    def runSubscribers(self):
        self.lidar.handleLidar()
        self.imu.handleImu()
        self.gps.handleGps()

    def publishMotor(self):
        for coord in self.gpsCoordinations:
            self.calculateMotorValue(coord)

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        self.runSubscribers()
        while not rospy.is_shutdown():
            # print(self.lidar.lidarDatas)
            self.publishMotor()
            rospy.sleep(1)

    def calculateMotorValue(self, gpsCoordination):
        xCoordDifference = gpsCoordination[0] - self.gps.latitude
        yCoordDifference = gpsCoordination[1] - self.gps.longitude
        if self.lidar.result == 0:
            if xCoordDifference > 1:
                self.motorValue.rightMotor = 10
                self.motorValue.leftMotor = 10
        else:
            if self.lidar.result == 1:


if __name__ == '__main__':
    try:
        a = Ship()
        a.init()
    except rospy.ROSInterruptException:
        pass
