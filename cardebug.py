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


def mover(reli, speed, deli):
    speed = speed
    deli.append("reli : " + str(reli) + " >> ")
    metalist = [ [[1,1,1,1,0],[1,1,1,0,0],[1,1,0,0,0]]  ,  [[1,0,0,0,1],[1,1,0,0,1],[1,0,0,1,1]]  ,  [[0,1,1,1,1],[0,0,1,1,1],[0,0,0,1,1]] ]
    if reli in metalist[0]:
        alpha = (reli.count(1) - 2) * 4
        rightSwingTurn(speed + alpha, 0.2)
        deli.append("rightSwingTurn" + "\n")
    elif reli in metalist[1]:
        go_forward(speed, 0.2)
        deli.append("go_forward" + "\n")
    elif reli in metalist[2]:
        alpha = (reli.count(1) - 2) * 4
        leftSwingTurn(speed + alpha, 0.2)
        deli.append("leftSwingTurn" + "\n")
    else:
        go_forward(1, 0.1)
        deli.append("else go_forward" + "\n")


def avoider(avs):
    leftSwingTurn(avs, 2)
    go_forward(avs, 2)
    rightSwingTurn(avs, 2)


GPIO.setwarnings(False)
pwm_setup()

mindis = 20
obstacle = 1

SwingPr = 90
SwingTr = 0.5

if __name__ == "__main__":
    fH = open("debug.txt", 'w')
    deli = list()
    speed = input("Please input speed : ")
    try:
        while True:
            time.sleep(0.1)
            if getDistance() < mindis:
                avoider(30)
            else:
                mover(trackingModule(), speed, deli)
    except KeyboardInterrupt:
            fH.writelines(deli)
            fH.close()
            GPIO.cleanup()
            pwm_low()
