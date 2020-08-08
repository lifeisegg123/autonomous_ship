#!/usr/bin/env python2
import rospy
from autonomous_ship.msg import gps
from matplotlib import pyplot as plt


class Gps:

    latitude = 0
    longitude = 0

    def handleGps(self):
        self.gpsSub = rospy.Subscriber("Gps", gps, self.callbackGps)

    def callbackGps(self, msg):
        self.latitude = msg.latitude
        self.longitude = msg.longitude
        plt.plot(self.latitude, self.longitude, 'b.')
        plt.axis('equal')
        plt.pause(0.005)
