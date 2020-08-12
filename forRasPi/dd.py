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
	for i in range(50, 58):
	    value = float(i) / 10
	    self.moveBldc(2, value)
            self.moveBldc(1, value)
	    time.sleep(0.1)
	
        while True:
	    """
	    print "------should input motor value-------" 
	    a = input()
	    print "------should input servo value-------"
	    b = input()
            self.moveBldc(2, float(a))
	    self.moveBldc(1, float(a))
	    self.moveServo(float(b))
	    """
	  
	    self.moveBldc(2, 5.7)
            self.moveBldc(1, 5.7)            
        """ self.subMotorValue = rospy.Subscriber(
            "motorValue", motorValue, self.callbackMotorSubscriber)
        rospy.spin() """

    def moveMotor(self, id, min, max, direction):
        mid = (max - min) / 10
        value = min + (mid *direction)
        pwm = value / (1.0 / 91.0 * 1000) * 100
        print pwm, value
        self.board.set_pwm_duty(id, pwm)

    def moveBldc(self, id, direction):
        self.moveMotor(id, 1.1, 1.9, direction)

    def moveServo(self, direction):
        self.moveMotor(0, 1.0, 2.0, direction)

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
            print_board_status()
            print("board begin faild")
            return 0
        print("board begin success")

        self.print_board_status()
        return 1

    def callbackMotorSubscriber(self, msg):
        """ self.moveServo(msg.servo)
        self.moveBldc(1, msg.leftMotor)
        self.moveBldc(2, msg.rightMotor) """
        self.moveServo(5)
        print("servo")

if __name__ == "__main__":
    m = Motor()
