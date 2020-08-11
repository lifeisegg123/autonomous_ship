#!/usr/bin/env python2
from handleGps import Gps
import rospy
import time

from autonomous_ship.msg import motorValue

class Hopping:
    gpsCoordinations = [[100, 10], [500, 300], [600, 100]]

    motorPub = rospy.Publisher('motor', motorValue, queue_size=10)
    motorValue = motorValue()

    gps = Gps()

    

    def setMotorValue(self, servoValue, rightValue = 6, leftValue = 6):
        self.motorValue.rightMotor = rightValue
        self.motorvalue.leftMotor = leftValue
        self.motorValue.servo = servoValue
    
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
            self.publishMotor()
            rospy.sleep(0.1)

    def returnBoolGps(self, gpsCoordinations, gps):
        value = gpsCoordinations - gps
        result = False
        if value <= 0:
            result = True
        return result
    
    
if __name__ == "__main__":
    try:
        aa = Hopping()

        for x in range(aa.gpsCoordinations.length):
            
            latitude = aa.returnBoolGps(aa.gpsCoordinations[x][0], aa.gps[1])    
            longitude = aa.returnBoolGps(aa.gpsCoordination:s[x][1], aa.gps[2])
            
            whlie(True):
                if latitude and longitude == True:
                    break;

                elif latitude == False:
                    if latitude <= 0:     
                        aa.setMotorValue(10, 6, 6) #modify servo value
                    else:
                        aa.setMotorValue(0, 6, 6)

                elif longitude == False:
                    aa.setMotorValue(5, 6, 6)
                    

    except rospy.ROSInterruptExceptio:
        pass


'''
15750
73270

17300
72240

16





17890
76840
'''