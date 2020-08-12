#!/usr/bin/env python2
from handleGps import Gps
import rospy
import time

from autonomous_ship.msg import motorValue

class Gara:

    motorPub = rospy.Publisher('motor', motorValue, queue_size=10)
    motorValue = motorValue()


    def setServoMotorValue(self, servoValue):
        self.motorValue.servo = servoValue
    
    """
    def runSubscribers(self):
        self.lidar.handleLidar()
        self.imu.handleImu()
        self.gps.handleGps()
    """
    def setServo(self):
        rospy.sleep(10)

        self.setServoMotorValue(10)
        rospy.sleep(10)

        self.setServoMotorValue(0)
        rospy.sleep(10)

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        while not rospy.is_shutdown():
            self.runSubscribers()
            self.publishMotor()
            rospy.sleep(0.1)

    
if __name__ == '__main__':
    try:
        ko = Gara()
        ko.init()

    except:
    