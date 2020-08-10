#!/usr/bin/env python2
import pigpio
import time

pi = pigpio.pi()

pi.set_mode(8, pigpio.OUTPUT)  # conversion
pi.set_mode(17, pigpio.OUTPUT)  # LEDout
pi.set_mode(23, pigpio.INPUT)  # control
pi.set_mode(27, pigpio.INPUT)  # auto

while true:
    if pi.read(23):
        pi.write(8, 0)
        pi.write(17, 1)
    elif pi.read(27):
        pi.write(8, 1)
        pi.write(17, 1)
        time.sleep(0.5)
        pi.write(17, 0)
