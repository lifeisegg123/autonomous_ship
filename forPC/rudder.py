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

    """\
    def runSubscribers(self):
        self.lidar.handleLidar()
        self.imu.handleImu()
        self.gps.handleGps()
    """

    def publishMotor(self):
        self.motorPub.publish(self.motorValue)

    def moveServo(self):

        co = 0
        self.setServoMotorValue(5)
        self.publishMotor()
        rospy.sleep(5)

        while True:

            self.setServoMotorValue(0)
            self.publishMotor()
            rospy.sleep(5)

            self.setServoMotorValue(10)
            self.publishMotor()
            rospy.sleep(2)

            self.setServoMotorValue(5)
            self.publishMotor()
            rospy.sleep(11)

            self.setServoMotorValue(10)
            self.publishMotor()
            rospy.sleep(5)

            self.setServoMotorValue(0)
            self.publishMotor()
            rospy.sleep(2)

            self.setServoMotorValue(10)  # reach to start point
            self.publishMotor()
            rospy.sleep(6)

            if co == 2:
                self.setServoMotorValue(0)
                self.publishMotor()
                rospy.sleep(5)

                self.setServoMotorValue(5)
                self.publishMotor()
                rospy.sleep(5)
                break

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        while not rospy.is_shutdown():
            self.moveServo()
            rospy.sleep(0.1)


if __name__ == '__main__':
    ko = Gara()
    ko.init()
