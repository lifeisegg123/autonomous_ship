import rospy
from autonomous_ship.msg import imu


class Imu:

    self.imuData = []

    def handleImu(self):
        self.imuSub = rospy.Subscriber("Imu", imu, callbackMotorSubscribe)

    def callbackMotorSubscribe(self, msg):
        imuData[0] = msg.xAngle
        imuData[1] = msg.yAngle
