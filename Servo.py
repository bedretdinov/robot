# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import botbook_gpio as gpio 
import numpy as np

class Servo():

    pin_num = None
    pin_obj = None
    position = 0
    position_default = 0

    def __init__(self, pin_num, position=90):

        self.position = position
        self.position_default = position
        GPIO.setup(pin_num, GPIO.OUT)  
        self.pin_obj = GPIO.PWM(pin_num, 50) 
        self.pin_obj.start(self.gradus(self.position))

        self.pin_num  = pin_num 
        
    def gradus(self,gradus):
        return float(gradus)/float(18)+2.5 
    
    def rotate(self, rotate = None):

        if(rotate is None):
            rotate = self.position_default

        if(rotate==self.position):
            return False
        
        incremet=-1
        if(rotate>self.position):
            incremet=1


        for i in range(abs(rotate-self.position)):
            self.position+=incremet
            self.pin_obj.ChangeDutyCycle(
                    self.gradus(self.position) 
            )  
            time.sleep(0.01)
            
            if(rotate==self.position):
                break


class ServoSynchronous():
    pin_nums = None
    pin_obj = []
    positions = []

    def __init__(self, pin_nums):

        pinsdetect = {}

        for pin_num in pin_nums:

            if(pin_num not in pinsdetect.keys()):
                GPIO.setup(pin_num, GPIO.OUT)
                pin_obj = GPIO.PWM(pin_num, 50)
            else:
                pin_obj = pinsdetect[pin_num]

            pin_obj.start(self.gradus(90))

            self.pin_obj.append(pin_obj)
            self.positions.append(90)

            pinsdetect[pin_num] = pin_obj

        self.pin_nums = pin_nums

    def gradus(self, gradus):
        return float(gradus) / float(18) + 2.5


    def rotateAll(self, rotates):

        i=0

        positionFlag = []
        while (True):

            if (rotates == self.positions):
                break

            incremet = -1
            if (rotates[i] > self.positions[i]):
                incremet = 1

            self.positions[i] += incremet
            self.pin_obj[i].ChangeDutyCycle(
                self.gradus(self.positions[i])
            )
            time.sleep(0.01)

            if (rotates[i] == self.positions[i]):
                positionFlag.append(1)

            if(len(positionFlag)>=len(rotates)):
                break

            i+=1

            if(i>=len(rotates)):
                i=0
