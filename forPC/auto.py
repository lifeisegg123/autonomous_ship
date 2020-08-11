#!/usr/bin/env python2
from handleLidar import Lidar
import rospy
import math
from autonomous_ship.msg import motorValue


class Ship:
    motorPub = rospy.Publisher('motor', motorValue, queue_size=10)
    motorValue = motorValue()

    lidar = Lidar()

    def runSubscribers(self):
        self.lidar.handleLidar()

    def publishMotor(self):
        self.motorValue.leftMotor = 6
        self.motorValue.rightMotor = 6

        index = 0
        for i in range(1, len(self.lidar.lidarData)):
            if not math.isinf(self.lidar.lidarData[i]):
                index = i
                break
        for i in range(1, len(self.lidar.lidarData)):
            if self.lidar.lidarData[i] >= self.lidar.lidarData[index] and not math.isinf(self.lidar.lidarData[i]):
                print i, self.lidar.lidarData[i]
                index = i
        servoValue = (index) / 360.0 * 10.0
        self.motorValue.servo = servoValue
        self.motorPub.publish(self.motorValue)

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        while not rospy.is_shutdown():
            self.runSubscribers()
            self.publishMotor()
            rospy.sleep(0.1)


if __name__ == '__main__':
    try:
        a = Ship()
        a.init()
    except rospy.ROSInterruptException:
        pass
