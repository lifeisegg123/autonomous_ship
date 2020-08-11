#!/usr/bin/env python2
from handleGps import Gps
import rospy
import time
class Hopping:
    gpsCoordinations = [[100, 10], [500, 300], [600, 100]]

    motorPub = rospy.Publisher('motor', motorValue, queue_size=10)
    motorValue = motorValue()

    lidar = Lidar()
    imu = Imu()
    gps = Gps()

    

    def motorStraight(self):
        self.motorValue.rightMotor = 6
        self.motorvalue.leftMotor = 6
        time.sleep(1)

    def runSubscribers(self):
        self.lidar.handleLidar()
        self.imu.handleImu()
        self.gps.handleGps()

    def publishMotor(self):
        print self.lidar.lidarData
        #xCoordDifference = gpsCoordination[0] - self.gps.latitude
        #yCoordDifference = gpsCoordination[1] - self.gps.longitude
        self.motorValue.rightMotor = 6
        self.motorValue.leftMotor = 6
        index = 0
        for i in range(self.lidar.lidarData):
            if self.lidar.lidarData[i] >= self.lidar.lidarData[index]:
                index = i
        servoValue = index / 180 * 10
        #servoValue = (180 - index) / 180 * 10
        self.motorValue.servo = servoValue
        self.motorPub.publish(motorValue)

    def init(self):
        rospy.init_node('Ship', anonymous=True)
        while not rospy.is_shutdown():
            self.runSubscribers()
            print(self.lidar.lidarData)
            self.publishMotor()
            rospy.sleep(1)

    def returnBoolGps(self, gpsCoordinations, gps):
        value = gpsCoordinations - gps
        result = False
        if value <= 0:
            result = True
        return result

if __name__ == "__main__":
    try:
        aa = Hopping

        

        while(True):
            
            aa.returnBoolGps(gpsCoordinations[][], gps[1])    

            if  
                
             
            
            
             #    yGps = gpsCoordinations[0][1] - gps[1]


    except:


'''
15750
73270

17300
72240

16





17890
76840
'''