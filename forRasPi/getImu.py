from mpu6050 import mpu6050

import rospy
from std_msgs.msg import Imu

if __name__ == "__main__":
    rospy.init_node("publishIMU")
    pub = rospy.Publisher("Imu", Imu)
    sensor = mpu6050(0x68)

    while True:
        accelerometer_data = sensor.get_accel_data()
        gyro = sensor.get_gyro_data()
        print("accel ", accelerometer_data)
        print("gyro ", gyro)
        time.sleep(1)
