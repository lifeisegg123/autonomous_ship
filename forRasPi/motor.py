from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board
from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_Servo as Servo

import time


class Motor:
    


    def __init__(self):
        self.board = Board(1, 0x10)    # Select i2c bus 1, set address to 0x10
        self.servo = Servo(board)
        self.bldcMotorRight = Servo(board)
        self.bldcMotorLeft = Servo(board)
        self.print_board_status()
        self.connectBoard()
    

    def moveMotor(id, min, max, direction):
        mid = (max - min) / 10
        value = min + (mid * direction)

        pwm = value / (1 / 91 * 0.001)
        
        self.board.set_pwm_duty(id, pwm)
            
    def moveBldc(id, direction):
        self.moveMotor(id, 1.1, 1.9, direction)
    def moveServo(direction):
        self.moveServo(0, 1, 1.8, direction)



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
    m = Motor()
    m.moveBldc(1,5)
