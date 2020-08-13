#!/usr/bin/env python2
from handleGps import Gps
import rospy
import time

from autonomous_ship.msg import motorValue


class Hopping:
    gpsCoordinations = [[3504.1631898, 12834.7376235], [
        3504.1661981, 12834.7364306], [3504.1777948, 12834.7318121]]

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

        for x in range(len(self.gpsCoordinations)):
            latitude = self.returnGps(self.gpsCoordinations[x][0], self.gps[1])
            longitude = self.returnGps(self.gpsCoordination[x][1], self.gps[2])

            while(True):

                if latitude == 0 and longitude <= 0:
                    break

                elif (0.00001 <= latitude <= 0.001 and longitude <= 0):
                    if latitude > 0.00100:
                        self.setServoMotorValue(0)
                        self.publishMotor()

                    elif latitude < 0.00010:
                        self.setServoMotorValue(10)
                        self.publishMotor()

                elif 0.00001 <= longitude <= 0.001 and latitude <= 0:
                    self.setServoMotorValue(5)
                    self.publishMotor()

            for x in range(1, len(self.gpsCoordinations)):
                latitude = self.returnGps(
                    self.gpsCoordinations[x][0], self.gps[1])
                longitude = self.returnGps(
                    self.gpsCoordination[x][1], self.gps[2])

                while(True):

                    if latitude == 0 and longitude <= 0:
                        break

                    elif (0.00001 <= latitude <= 0.001 and longitude <= 0):
                        if latitude > 0.00100:
                            self.setServoMotorValue(0)
                            self.publishMotor()

                        elif latitude < 0.00010:
                            self.setServoMotorValue(10)
                            self.publishMotor()

                    elif 0.00001 <= longitude <= 0.001 and latitude <= 0:
                        self.setServoMotorValue(5)
                        self.publishMotor()


if __name__ == "__main__":
    try:
        aa = Hopping()
        aa.init()

    except rospy.ROSInterruptExceptio:
        pass
