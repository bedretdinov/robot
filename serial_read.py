import re
import serial
import time
import numpy as np
import random


from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
for i in range(16):
    kit.servo[i].set_pulse_width_range(500, 3000)

mean_vals = []
with serial.Serial('/dev/ttyUSB0', 115200, timeout=1) as ser:
    while (True):
        line = ser.readline()
        line = line.decode('utf-8').replace('\\n','').replace('\\r','')
        rotates = np.array(line.split(';')).astype(float)

        kit.servo[0].angle = rotates[0]
