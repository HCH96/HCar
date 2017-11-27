import RPi.GPIO as GPIO
from trackingModule import *
from time import sleep
from TurnModule import *
from go_any import *

# set GPIO warnings as flase
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

# right way : (1,1,0,0,0) -> turn 90 right
# left way : (0,0,0,1,1) -> turn 90 left
if __name__ == "__main__":
    while True:
        if signal()[2] == 0:
            go_forward(40, 0.3)
        elif signal() == (0,0,0,1,1):
            leftPointTurn(40, 0.4)
        elif signal() == (1,1,0,0,0):
            rightPointTurn(40, 0.4)