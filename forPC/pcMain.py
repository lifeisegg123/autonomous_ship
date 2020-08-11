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
    
    def shipReward():
        self.motorValue.rightMotor = 3
        self.motorValue.leftMotor = 3

    def shipStraight():
        self.motorValue.rightMotor = 7
        self.motorValue.leftMotor = 7

    def ReturnToZero():

    def calculateMotorValue(self, gpsCoordination):
        xCoordDifference = gpsCoordination[0] - self.gps.latitude
        yCoordDifference = gpsCoordination[1] - self.gps.longitude
        imuXrotation = Imu.get_x_rotation
        imuYrotation = Imu.get_y_rotation

        if self.lidar.result == 0:
            if xCoordDifference < 1 and yCoordDifference < 1: #do not goal to destination
                self.shipStraight()#???
                
        else if self.lidar.result == 1:
            if xCoordDifference < 1 and yCoordDifference < 1:
                if imuXrotation <= 0:
                    while(imuXrotation <= 45):
                        self.motorValue.leftMotor = 7
                    while(xCoordDifference <= 1):  #will modify defaul value
                        self.shipStraight()

        else if self.lidar.result == 8:
            if xCoordDifference < 0 and yCoordDifference < 0: #when 
                if imuXerotation >= 0:
                    while(imuXrotation <= -45): # -10 == xcoord???? i don't know
                        self.motorValue.rightMotor = 7
                    while(xCoordDifference <= 1):
                        self.shipStraight()

if __name__ == '__main__':
    try:
        a = Ship()
        a.init()
    except rospy.ROSInterruptException:
        pass
