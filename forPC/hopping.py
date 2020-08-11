#!/usr/bin/env python2
from handleGps import Gps
import rospy
import time


class Hopping:
    gpsCoordinations = [[100, 10], [500, 300], [600, 100]]

    motorPub = rospy.Publisher('motor', motorValue, queue_size=10)
    motorValue = motorValue()

    lidar = Lidar()
    imu = Imu()
    gps = Gps()

    def motorStraight(self):
        self.motorValue.rightMotor = 6
        self.motorvalue.leftMotor = 6
        time.sleep(1)

    def goToFirstDestination(self):
        if gpsCoordination[0][0] - 100 <= gps[1] <= gpsCoordination[0][0] + 100 and
        gpsCoordination[0][1] - 100 <= gps[2] <= gpsCoordination[0][1] + 100:
            self.motorValue.rightMotor = 6
            time.sleep(1)
            while(gpsCoordination[1][0] - 100 <= gps[1] <= gpsCoordination[1][0] + 100 and
                  gpsCoordination[1][1] - 100 <= gps[2] <= gpsCoordination[1][1] + 100)
            self.motorStraight()
            self.goToSecondDestination()

    def goToSecondDestination(self):
        if gpsCoordination[1][0] - 100 <= gps[1] <= gpsCoordination[1][0] + 100 and
        gpsCoordination[1][1] - 100 <= gps[2] <= gpsCoordination[1][1] + 100:
            self.motorValue.leftMotor = 7
            time.sleep(3)

            while(gpsCoordination[2][0] - 100 <= gps[1] <= gpsCoordination[2][0] + 100 and
                  gpsCoordination[2][1] - 100 <= gps[2] <= gpsCoordination[2][1] + 100)
            self.motorStraight()
            self.goToThirdDestination()

    def goToThirdDestination(self):
        if gpsCoordination[2][0] - 100 <= gps[1] <= gpsCoordination[2][0] + 100 and
        gpsCoordination[2][1] - 100 <= gps[2] <= gpsCoordination[2][1] + 100:
            self.motorValue.rightMotor = 6
            time.sleep(3)

            while(gpsCoordination[3][0] - 100 <= gps[1] <= gpsCoordination[3][0] + 100 and
                  gpsCoordination[3][1] - 100 <= gps[2] <= gpsCoordination[3][1] + 100)
            self.motorStraight()
            self.goToFourthDestination()

    def goToFourthDestination(self):
        if gpsCoordination[2][0] - 100 <= gps[1] <= gpsCoordination[2][0] + 100 and
        gpsCoordination[2][1] - 100 <= gps[2] <= gpsCoordination[2][1] + 100:
            self.motorValue.leftMotor = 6
            time.sleep(3)

            while(gpsCoordination[3][0] - 100 <= gps[1] <= gpsCoordination[3][0] + 100 and
                  gpsCoordination[3][1] - 100 <= gps[2] <= gpsCoordination[3][1] + 100)
            self.motorStraight()

    def runSubscribers(self):
        self.lidar.handleLidar()
        self.imu.handleImu()
        self.gps.handleGps()

    def publishMotor(self):
        print self.lidar.lidarData
        #xCoordDifference = gpsCoordination[0] - self.gps.latitude
        #yCoordDifference = gpsCoordination[1] - self.gps.longitude
        self.motorValue.rightMotor = 6
        self.motorValue.leftMotor = 6
        index = 0
        for i in range(self.lidar.lidarData):
            if self.lidar.lidarData[i] >= self.lidar.lidarData[index]:
                index = i
        servoValue = index / 180 * 10
        #servoValue = (180 - index) / 180 * 10
        self.motorValue.servo = servoValue
        self.motorPub.publish(motorValue)

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        while not rospy.is_shutdown():
            self.runSubscribers()
            print(self.lidar.lidarData)
            self.publishMotor()
            rospy.sleep(1)


if __name__ == "__main__":
    try:

        goToFirstDestination()

    except:
