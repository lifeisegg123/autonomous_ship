#!/usr/bin/env python2
from handleGps import Gps
import rospy
import time

from autonomous_ship.msg import motorValue

class Hopping:
    gpsCoordinations = [[100, 10], [500, 300], [600, 100]]

    motorPub = rospy.Publisher('motor', motorValue, queue_size=10)
    motorValue = motorValue()

    gps = Gps()

    

    def setMotorValue(self, servoValue, rightValue = 6, leftValue = 6):
        self.motorValue.rightMotor = rightValue
        self.motorvalue.leftMotor = leftValue
        self.motorValue.servo = servoValue
    
    def runSubscribers(self):
        self.lidar.handleLidar()
        self.imu.handleImu()
        self.gps.handleGps()

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        while not rospy.is_shutdown():
            self.runSubscribers()
            self.publishMotor()
            rospy.sleep(0.1)

    def returnBoolGpsLatitude(self, gpsCoordinations, gps):
        value = gpsCoordinations - gps
        #result = False
        #if value <= 0:
        #    result = True
        return result
    
    
if __name__ == "__main__":
    try:
        aa = Hopping()

        for x in range(aa.gpsCoordinations.length):
            
            latitude = aa.returnBoolGps(aa.gpsCoordinations[x][0], aa.gps[1])    
            longitude = aa.returnBoolGps(aa.gpsCoordination:s[x][1], aa.gps[2])
            
            #longitudeBool = longitude = 0 ? True : False

            whlie(True):
                if latitude <= 0 and longitude <= 0:
                    break;

                elif latitude != 0 and longitude <= 0:
                    if latitude  > 0:
                        aa.setMotorValue(0, 6, 6)
                    elif latitude < 0:
                        aa.setMotorValue(10, 6, 6)

                elif longitude != 0 and latitude <= 0:
                        aa.setMotorValue(5, 6, 6)

                    
                    

    except rospy.ROSInterruptExceptio:
        pass


'''
15750
73270

17300
72240

16





17890
76840
'''