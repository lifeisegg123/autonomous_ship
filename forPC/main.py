from handleCamera import handleCamera
from handleLidar import Lidar
import rospy

from std_msgs.msg import Int32


class Ship:
    lidar = Lidar()
    motorPub = rospy.Publisher('motor', Int32, queue_size=10)

    def subscribeLidar(self):
        self.lidar.handleLidar()

    def publishMotor(self):
        self.pub.publish()

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        self.subscribeLidar()
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
