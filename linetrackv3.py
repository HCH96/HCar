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


def mover(reli, speed, meth):
    speed = speed
    metalist = [ [[1,1,1,1,0],[1,1,1,0,0],[1,1,0,0,0]]  ,  [[1,0,0,0,1],[1,1,0,0,1],[1,0,0,1,1]]  ,  [[0,1,1,1,1],[0,0,1,1,1],[0,0,0,1,1]] ]
    if reli in metalist[0]:
        alpha = (reli.count(1) - 2) * 4
        rightSwingTurn(speed + alpha, 0.2)
    elif reli in metalist[1]:
        go_forward(speed, 0.2)
    elif reli in metalist[2]:
        alpha = (reli.count(1) - 2) * 4
        leftSwingTurn(speed + alpha, 0.2)
    if reli == [1,1,1,1,1]:
        if meth == "1":
            while not (0 in reli):
                leftSwingTurn(speed, 0.2)
        if meth == "2":
            while not (0 in reli):
                rightSwingTurn(speed, 0.2) 
    else:
        go_forward(30, 0.00001)


def avoider(avs):
#     start = time.time()
#     dis = 0
#     while (start - time.time()) < 1:
#         time.sleep(0.1)
#         dis = dis + getDistance()
#         go_forward(1, 0.000001)
#     if dis//10 < mindis:
        leftSwingTurn(avs, 2)
        go_forward(avs, 2)


GPIO.setwarnings(False)
pwm_setup()

mindis = 25
obstacle = 1

SwingPr = 90
SwingTr = 0.5

if __name__ == "__main__":
    meth = input("INPUT METH : ")
    speed = input("Please input speed : ")
    try:
        while True:
            if getDistance() < mindis:
                avoider(30)
            else:
                mover(trackingModule(), speed, meth)
    except KeyboardInterrupt:
            GPIO.cleanup()
            pwm_low()
