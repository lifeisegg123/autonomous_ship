#!/usr/bin/env python2
from handleLidar import Lidar
from handleImu import Imu
from handleGps import Gps
import rospy

from autonomous_ship.msg import motorValue


class Ship:
    #gpsCoordinations = [[100, 10], [500, 300], [600, 100]]

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
        print self.lidar.lidarData
        #xCoordDifference = gpsCoordination[0] - self.gps.latitude
        #yCoordDifference = gpsCoordination[1] - self.gps.longitude
        self.motorValue.leftMotor = 6
        self.motorValue.rightMotor = 6
        index = 0
        flag = False
        for i in range(self.lidar.lidarData):
            if self.lidar.lidarData[i] != 0 and self.lidar.lidarData[i] <= self.lidar.lidarData[index]:
                if self.lidar.lidarData[index] - self.lidar.lidarData[i] < 1:

                else:
                    index = i

        #servoValue = index / 180 * 10
        servoValue = (180 - index) / 180 * 10
        self.motorValue.servo = servoValue
        self.motorPub.publish(motorValue)

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        while not rospy.is_shutdown():
            self.runSubscribers()
            print(self.lidar.lidarData)
            self.publishMotor()
            rospy.sleep(1)


if __name__ == '__main__':
    try:
        a = Ship()
        a.init()
    except rospy.ROSInterruptException:
        pass
