#!/usr/bin/env python2
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import CompressedImage


class Vision():

    bridge = CvBridge()

    def callback(self, image_msg):

        cv_image = self.bridge.imgmsg_to_cv2(image_msg, "bgr8")
        cv_gray = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)
        ret, cv_binary = cv2.threshold(cv_gray, 50, 100, cv2.THRESH_BINARY)
        cv2.imshow('test', cv_binary)
        cv2.waitKey(1)

    def handleCamera(self):
        sub = rospy.Subscriber(
            '/image_raw', Image, callback, queue_size=1)
