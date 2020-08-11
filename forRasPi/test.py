#!/usr/bin/env python2
import rospy
from std_msgs.msg import String

rospy.init_node("test")
pub = rospy.Publisher("test", String, queue_size=10)
while not rospy.is_shutdown():
    pub.publish("test")
