#!/usr/bin/env python2
import pigpio
import time

pi = pigpio.pi()

pi.set_mode(8, pigpio.OUTPUT)  # conversion
pi.set_mode(17, pigpio.OUTPUT)  # LEDout

while True:
    pi.write(8, 1)
    pi.write(17, 1)
    time.sleep(0.5)
    pi.write(17, 0)
    time.sleep(0.5)
