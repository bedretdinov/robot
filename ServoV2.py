# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time
import math
import numpy as np
kit = ServoKit(channels=16)

class Servo():

    speed = 0.3
    pin_num = None
    pin_obj = None
    position = 0
    position_default = 0

    def __init__(self, pin_num, position=90):
        self.pin_obj = kit.servo[pin_num]
        self.pin_obj.angle = position
        self.position = position
        self.position_default = position
        self.pin_num  = pin_num


    def rotate(self, rotate ):

        print(self.pin_obj.angle)