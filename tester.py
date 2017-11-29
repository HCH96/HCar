import RPi.GPIO as GPIO
from go_any import *

# set GPIO warnings as flase
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

go_forward(50, 100)