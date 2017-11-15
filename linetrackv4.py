import RPi.GPIO as GPIO
import time
import sys
from ultraModule import getDistance
from TurnModule import *
from go_any import *


# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)

leftmostled = 16
leftlessled = 18
centerled = 22
rightlessled = 32  #
rightmostled = 40  #

GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled,   GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)  #
GPIO.setup(rightlessled, GPIO.IN)  #


def trackingModule():
    reli = list()
    reli.append(GPIO.input(leftmostled))
    reli.append(GPIO.input(leftlessled))
    reli.append(GPIO.input(centerled))
    reli.append(GPIO.input(rightlessled))
    reli.append(GPIO.input(rightmostled))
    return reli


def mover(speed):
    speed = speed
    reli1 = trackingModule()
    time.sleep(0.05)
    reli2 = trackingModule()
    time.sleep(0.05)
    reli3 = trackingModule()
    result = aver(reli1, reli2, reli3)
    if result <= 3:
        leftSwingTurn(speed, 0.2)
    elif 9 <= result:
        rightSwingTurn(speed, 0.2)
    elif 3 < result and result < 9:
        go_forward(speed, 0.2)
    else:
        pass


def aver(reli1, reli2, reli3):
    sumed = indexer(reli1) + indexer(reli2) + indexer(reli3)
    return sumed


def indexer(reli):
    count = reli.count(0)
    sum_index = 0
    for i in range(len(reli)):
        if reli[i] == 0:
            sum_index = sum_index + i
    if count != 0:
        sum_index = sum_index // count
    else:
        sum_index = 2
    return sum_index


def avoider(avs):
    start = time.time()
    dis = 0
    while (start - time.time()) < 1:
        time.sleep(0.1)
        dis = dis + getDistance()
        go_forward(1, 0.000001)
    if dis//10 < mindis:
        leftSwingTurn(avs, 1)
        go_forward(avs, 2)
        rightSwingTurn(avs, 1)


GPIO.setwarnings(False)
pwm_setup()

mindis = 25
obstacle = 1

SwingPr = 90
SwingTr = 0.5

if __name__ == "__main__":
    speed = input("Please input speed : ")
    try:
        while True:
            if getDistance() < mindis:
                # avoider(30)
            else:
                mover(speed)
    except KeyboardInterrupt:
            GPIO.cleanup()
            pwm_low()
