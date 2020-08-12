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

    def setServoMotorValue(self, servoValue):
        self.motorValue.servo = servoValue

    def runSubscribers(self):
        self.gps.handleGps()

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        while not rospy.is_shutdown():
            self.runSubscribers()
            self.gpsServo()
            rospy.sleep(0.1)

    def returnGps(self, gpsCoordinations, gps):
        value = gpsCoordinations - gps
        return result

    def publishMotor(self):
        self.motorPub.publish(self.motorValue)

    def gpsServo(self):

        for x in range(self.gpsCoordinations.length):
            latitude = self.returnGps(self.gpsCoordinations[x][0], self.gps[1])    
            longitude = self.returnGps(self.gpsCoordination:s[x][1], self.gps[2])
            
            # longitude = 0 ? True : False
            
            while(True):
                if latitude <= 0 and longitude <= 0:
                    break;

                elif latitude != 0 and longitude <= 0:
                    if latitude  > 0:
                        self.setServoMotorValue(0)
                        self.publishMotor()
                    elif latitude < 0:
                        self.setServoMotorValue(10)
                        self.publishMotor()
                elif longitude != 0 and latitude <= 0:
                        self.setServoMotorValue(5)
                        self.publishMotor()

if __name__ == "__main__":
    try:
        aa = Hopping()
        aa.init()

    except rospy.ROSInterruptExceptio:
        pass
