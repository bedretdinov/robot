import time
from random import randint
from ServoV2 import  Servo

from multiprocessing import Pool


motors = []
for x in range(0, 12):
    motors.append(Servo(x))

def rotate(data):
    #motors[data[0]].pin_obj.set_pulse_width_range(500, 3000)
    motors[data[0]].rotate(data[1])


while True:

    rotateFull = []
    for x in range(0, 12):
        roratte = randint(30, 110)
        rotateFull.append([x, roratte])

    with Pool(8) as p:
        print(p.map(rotate, rotateFull))

