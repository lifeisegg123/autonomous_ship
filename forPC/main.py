from handleCamera import handleCamera
from handleLidar import Lidar
from handleImu import Imu

import rospy

from std_msgs.msg import Int32


class Ship:
    lidar = Lidar()
    imu = Imu()
    motorPub = rospy.Publisher('motor', Int32, queue_size=10)

    def runSubscribes(self):
        self.lidar.handleLidar()
        self.imu.handleImu()

    def publishMotor(self):
        self.pub.publish()

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        self.runSubscribes()
        while not rospy.is_shutdown():
            # print(self.lidar.lidarDatas)
            publishMotor()
            rospy.sleep(1)


if __name__ == '__main__':
    try:
        a = Ship()
        a.init()
    except rospy.ROSInterruptException:
        pass
