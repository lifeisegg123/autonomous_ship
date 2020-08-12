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

    def publishMotor(self):
        self.motorPub.publish(self.motorValue)

    def moveServo(self):
        for x in range(0, 1):    
            self.setServoMotorValue(5)
            self.publishMotor()
            rospy.sleep(2)

            self.setServoMotorValue(0)
            self.publishMotor()
            rospy.sleep(8)

            self.setServoMotorValue(10)
            self.publishMotor()
            rospy.sleep(8)

            self.setServoMotorValue(5) #reach to end
            self.publishMotor()
            rospy.sleep(1)

            self.setServoMotorValue(10)
            self.publishMotor()
            rospy.sleep(7)
            
            self.setServoMotorValue(5)
            self.publishMotor()
            rospy.sleep(3)
            
            self.setServoMotorValue(10) #reach to start point
            self.publishMotor()
            rospy.sleep(7)

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        while not rospy.is_shutdown():
            self.runSubscribers()
            self.moveServo()
            rospy.sleep(0.1)

    
if __name__ == '__main__':
    try:
        ko = Gara()
        ko.init()

    except:
    