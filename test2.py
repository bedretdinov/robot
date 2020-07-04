# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time
import math
import numpy as np
kit = ServoKit(channels=16)




for i in range(16):
    kit.servo[i].set_pulse_width_range(500, 3000)


kit.servo[13].angle = 120 # бедро
kit.servo[14].angle = 90 # пятка
kit.servo[15].angle = 0 # Колено

kit.servo[12].angle = 110 # бедро бок

while True:
    break
   # rotate([1, 10])
   # rotate([1, 110])

   # rotate([12, 0])
   # rotate([12, 110])



#
#     rotateFull = []
#
#     rotateFull.append([0, randint(1,180)])
#     rotateFull.append([1, randint(1,180)])
#
#     with Pool(8) as p:
#         p.map(rotate, rotateFull)
#         p.close()
#
#     rotateFull = []
#     rotateFull.append([0, randint(1,180)])
#     rotateFull.append([1, randint(1,180)])
#     with Pool(8) as p:
#         p.map(rotate, rotateFull)
#         p.close()
