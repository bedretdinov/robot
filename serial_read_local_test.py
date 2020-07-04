import re
import serial
import time
import numpy as np
import random


mean_vals = []
with serial.Serial('/dev/ttyUSB1', 115200, timeout=1) as ser:

    while (True):
        line = ser.readline()
        line = line.decode('utf-8').replace('\\n','').replace('\\r','')

        try:
            rotates = (np.array(line.split(';')).astype(int)/1.4166666666666667).astype(int)
        except:
            print(line)

        print(rotates[0])
