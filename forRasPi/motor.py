#!/usr/bin/env python2
from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board
from autonomous_ship.msg import motorValue

import rospy
import time


class Motor:

    def __init__(self):
        self.board = Board(1, 0x10)
        self.print_board_status()
        self.connectBoard()
        self.board.set_pwm_enable()
        self.board.set_pwm_frequency(91)

        rospy.init_node("motorSubscriber")

        self.subMotorValue = rospy.Subscriber(
            "motor", motorValue, self.callbackMotorSubscriber)

        rospy.spin()

    def moveMotor(self, id, min, max, direction):
        mid = (max - min) / 10
        value = min + (mid * direction)
        pwm = value / (1.0 / 91.0 * 1000) * 100
        self.board.set_pwm_duty(id, pwm)

    def moveBldc(self, id, direction):
        self.moveMotor(id, 1.1, 1.9, direction)

    def moveServo(self, direction):
        self.moveMotor(0, 8.0, 2.2, direction)

    def print_board_status(self):
        if self.board.last_operate_status == self.board.STA_OK:
            print("board status: everything ok")
        elif self.board.last_operate_status == self.board.STA_ERR:
            print("board status: unexpected error")
        elif self.board.last_operate_status == self.board.STA_ERR_DEVICE_NOT_DETECTED:
            print("board status: device not detected")
        elif self.board.last_operate_status == self.board.STA_ERR_PARAMETER:
            print("board status: parameter error")
        elif self.board.last_operate_status == self.board.STA_ERR_SOFT_VERSION:
            print("board status: unsupport board framware version")

    def connectBoard(self):
        if self.board.begin() != self.board.STA_OK:    # Board begin and check board status
            self.print_board_status()
            print("board begin faild")
            return 0
        print("board begin success")

        self.print_board_status()
        return 1

    def callbackMotorSubscriber(self, msg):
        self.moveServo(msg.servo)
        self.moveBldc(1, msg.leftMotor)
        self.moveBldc(2, msg.rightMotor)


if __name__ == "__main__":
    m = Motor()
