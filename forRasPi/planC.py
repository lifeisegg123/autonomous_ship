#!/usr/bin/env python2
from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board

import time

class Motor:

    def __init__(self):
        self.board = Board(1, 0x10)
        self.print_board_status()
        self.connectBoard()
        self.board.set_pwm_enable()
	self.board.set_pwm_frequency(91)

	while False:
            self.moveBldc(2, 5.8)
            self.moveBldc(1, 5.8)

    def moveMotor(self, id, min , max, direction):
	mid = (max - min) / 10
	value = min + (mid * direction)
	pwm = value / (1.0 / 91.0 * 1000) * 100
	print pwm, value
	self.board.set_pwm_duty(id, pwm)

    def moveBldc(self, id, direction):
	self.moveMotor(id, 1.1, 1.9, direction)

    def print_board_status(self):
	if self.board.last_operate_status == self.board.STA_OK:
	    print("board status: everything ok")
	elif self.board.last_operate_status == self.board.STA_ERR:
	    print("board status: unexpected error")
	elif self.board.last_operate_status == self.board_STA_ERR_DEVICE_NOT_DETECTED:
            print("board status: device not detected")
	elif self.board.last_operate_status == self.board.STA_ERR_PARAMETERT:
	    print("board status: parameter error")

    def connectBoard(self):
        if self.board.begin() != self.board.STA_OK:
            print_board_status()
	    print("board begin faild")
	    return 0
	print("board begin success")

	self.print_board_status()
	return 1


if __name__ == "__main__":
    m = Motor()
