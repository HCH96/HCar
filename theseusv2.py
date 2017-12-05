import RPi.GPIO as GPIO
from TurnModule import *
from go_any import *

# set GPIO warnings as flase
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

# trackingModule setup
leftmostled = 16
leftlessled = 18
centerled = 22
rightlessled = 40
rightmostled = 32
GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled, GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)

# variable to interpret signal
F = (1, 1, 0, 1, 1)  # forward
L = (0, 0, 0, 1, 1)  # left
R = (1, 1, 0, 0, 0)  # right
S = (0, 0, 0, 0, 0)  # stop
V = (1, 1, 1, 1, 1)  # void


def infra_module():
    a = GPIO.input(leftmostled)
    b = GPIO.input(leftlessled)
    c = GPIO.input(centerled)
    d = GPIO.input(rightlessled)
    e = GPIO.input(rightmostled)
    return a, b, c, d, e


def trackmode(signal):
    stop()
    if signal == F:
        go_forward(20, 0.1)
    elif signal == (1, 0, 0, 1, 1) or signal == (1, 0, 1, 1, 1):
        leftSwingTurnobs(30, 0.1)
    elif signal == (1, 1, 0, 0, 1) or signal == (1, 1, 1, 0, 1):
        rightSwingTurnobs(30, 0.1)
    else:
        while not 0 in infra_module():
            print(signal)
            rightSwingTurnobs(30, 0.1)
            stop()
            sleep(0.5)


def mazemode(history):
    while (beep[0] == 0 or  beep[-1] == 0):
        print("in mazemode")
        go_forward(20,0.1)
        signal = infra_module()
        stop()
    if signal == F or signal == (1, 0, 0, 1, 1) or signal(1, 1, 0, 0, 1):
        if history[-1] == 0:
            rightPointTurn(30,0.1)
        else:
            trackmode()

    elif signal == V:
        if history[-1] == 0:
            while infra_module() != V:
                rightSwingTurnobs(30, 0.1)
        else:
            while infra_module() != V:
                leftSwingTurnobs(30, 0.1)
    else:
            trackmode(infra_module())

if __name__ == "__main__":
    try:
        while True:
            beep = infra_module()
            print("ok")
            if (beep[0] == 0 or beep[-1] == 0):
                mazemode(beep)
            else:
                trackmode(beep)
    except KeyboardInterrupt:
        pwm_low()
