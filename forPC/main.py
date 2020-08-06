from handleCamera import handleCamera
from handleLidar import Lidar
import rospy

from std_msgs.msg import Int32


class Ship():
    Lidar = Lidar()
    pub = rospy.Publisher('motor', Int32, queue_size=10)

    def sub(self):
        self.Lidar.handleLidar()

    def talker(self):
        rate = rospy.Rate(10)  # 10hz
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)

    def init(self):
        rospy.init_node('talker', anonymous=True)
        self.sub()
        while not rospy.is_shutdown():
            print(Lidar.lidarDatas)
            self.pub.publish()
            rospy.sleep(1)


if __name__ == '__main__':
    try:
        a = Ship()
        a.init()
    except rospy.ROSInterruptException:
        pass
