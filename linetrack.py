import RPi.GPIO as GPIO
from time import sleep
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


def mover(reli, speed):
    speed = speed
    if reli[0] == 1 and reli[1] == 1:
        go_forward(speed, 0.00001)
	if reli[0] == 0:
		leftSwingTurn(speed, 0.00001)
	if reli[-1] == 0:
		rightSwingTurn(speed, 0.00001)
    else:
        go_forward(speed, 0.00001)


def avoider():
    leftPointTurn(20, 2)
    go_forward(20, 2)
    rightPointTurn(20, 2)


GPIO.setwarnings(False)
pwm_setup()

mindis = 30
obstacle = 1

SwingPr = 90
SwingTr = 0.5

if __name__ == "__main__":
    speed = input("Please input speed : ")
    alpha = input("Please input alpha : ")
    while True:
        try:
            if getDistance() < mindis:
                avoider()
            else:
                mover(trackingModule(), speed, alpha)
        except KeyboardInterrupt:
            GPIO.cleanup()
            pwm_low()
