from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board
from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_Servo as Servo
from mpu6050 import mpu6050

from os import system

import pigpio
import time

system("sudo pigpiod"):




board = Board(1, 0x10)    # Select i2c bus 1, set address to 0x10
servo = Servo(board)


''' print last operate status, users can use this variable to determine the result of a function call. '''
def print_board_status():
  if board.last_operate_status == board.STA_OK:
    print("board status: everything ok")
  elif board.last_operate_status == board.STA_ERR:
    print("board status: unexpected error")
  elif board.last_operate_status == board.STA_ERR_DEVICE_NOT_DETECTED:
    print("board status: device not detected")
  elif board.last_operate_status == board.STA_ERR_PARAMETER:
    print("board status: parameter error")
  elif board.last_operate_status == board.STA_ERR_SOFT_VERSION:
    print("board status: unsupport board framware version")


def connectBoard():

  if board.begin() != board.STA_OK:    # Board begin and check board status
    print_board_status()
    print("board begin faild")
    return 0
  print("board begin success")

  print_board_status()
  servo.begin()   # servo control begin
  return 1

if __name__ == "__main__":
  pi = pigpio.pi()
  sensor = mpu6050(0x68)
  while True:
    accelerometer_data = sensor.get_accel_data()
    gyro = sensor.get_gyro_data()
    print("accel ", accelerometer_data)
    print("gyro ", gyro)
    time.sleep(1)