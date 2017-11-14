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

leftmostled=16
leftlessled=18
centerled=22
rightlessled=32  #
rightmostled=40  #

GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled,   GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN) #
GPIO.setup(rightlessled, GPIO.IN) #

def trackingModule():
	reli = []
	reli.append(GPIO.input(leftmostled))
	reli.append(GPIO.input(leftlessled))
	reli.append(GPIO.input(centerled))
	reli.append(GPIO.input(rightlessled))
	reli.append(GPIO.input(rightmostled))
	return reli

def mover(reli, speed):
	speed = speed
	if reli == [0,0,1,1,1] or reli == [0,0,0,1,1]:
		leftSwingTurn(speed, 0.07)
	elif reli == [0,0,0,0,1]:
		leftSwingTurn(speed-10, 0.07)
	elif reli == [0,1,1,1,1]:
		leftSwingTurn(speed+10, 0.07)
	elif reli == [1,0,0,0,1] or reli == [1,1,0,1,1]:
		go_forward(speed, 0.3)
	elif reli == [1,1,0,0,0] or reli == [1,1,1,0,0]:
		rightSwingTurn(speed, 0.07)
	elif reli == [1,0,0,0,0]:
		rightSwingTurn(speed-10, 0.07)
	elif reli == [1,1,1,1,0]:
		rightSwingTurn(speed+10, 0.07)
        elif reli == [1,1,1,1,1]:
		leftSwingTurn(speed-10, 0.07)
		go_forward(speed-10, 0.07)
	else:
		go_forward(speed, 0.3)

GPIO.setwarnings(False)
pwm_setup()

dis = 12
obstacle = 1

SwingPr = 90
SwingTr = 0.5

if __name__ == "__main__":
	try:
		while True:
		    distance = getDistance()
		    if (distance > dis):
		    mover(trackingModule(), 30)
		    else:
			rightSwingTurn(50, 1)
			print("a")
			go_forward(20, 2)
			print("b")
			leftSwingTurn(60, 1)
			print("c")
			go_forward_any(30, 1)
			print("d")
	except KeyboardInterrupt:
		GPIO.cleanup()
		pwm_low()
		
