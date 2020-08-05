from mpu6050 import mpu6050

from os import system
import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32
from tf.transformations import euler_from_quaternion

import pigpio
import time

system("sudo pigpiod")

if __name__ == "__main__":
    pi = pigpio.pi()
    sensor = mpu6050(0x68)
    while True:
        accelerometer_data = sensor.get_accel_data()
        gyro = sensor.get_gyro_data()
        print("accel ", accelerometer_data)
        print("gyro ", gyro)
        time.sleep(1)




   def callback(incomming_msg):
	   list_orientation = [incomming_msg.orientation.x, incomming_msg.orientation.y, 
						   incomming_msg.orientation.z, incomming_msg.orientation.w]
	   roll, pitch, yaw = euler_from_quaternion(list_orientation)

	   pub_imu_roll.publish(roll)
	   pub_imu_pitch.publish(pitch)
	   pub_imu_yaw.publish(yaw)

   rospy.init_node('imu_sub_and_pub_test')

   pub_imu_roll = rospy.Publisher('IMU_Roll', Float32, queue_size=10)
   pub_imu_pitch = rospy.Publisher('IMU_Pitch', Float32, queue_size=10)
   pub_imu_yaw = rospy.Publisher('IMU_Yaw', Float32, queue_size=10)

   sub = rospy.Subscriber('imu', Imu, callback)

   rospy.spin()
