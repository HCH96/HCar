import RPi.GPIO as GPIO
from time import sleep
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
rightlessled = 32
rightmostled = 40
GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled, GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)

metaforward = ((1,1,0,1,1), (1,0,0,1,1), (1,1,0,0,1), (1,0,1,1,1), (1,1,1,0,1))
def signal():
    A = GPIO.input(leftmostled)
    B = GPIO.input(leftlessled)
    C = GPIO.input(centerled)
    D = GPIO.input(rightlessled)
    E = GPIO.input(rightmostled)
    return A, B, C, D, E


def signalbone():
    metasignal = list()
    for i in range(2):
        metasignal.append(signal())
        sleep(0.5)
    return metasignal



def mazer(speed, time):
    right = (1, 1, 0, 0, 0)
    left = (0, 0, 0, 1, 1)
    forward = (1, 1, 0, 1, 1)
    stop = (0, 0, 0, 0, 0)
    void = (1, 1, 1, 1, 1)

    if signalbone()[0] == left:
        if signalbone()[1] == void:
            LeftPointTurn(speed, time)
        elif signalbone()[1] == forward:
            go_forward(30, 0.5)

    elif signalbone()[0] == stop:
        if signalbone()[1] == stop:
            pwm_low()
        elif signalbone()[1] == forward:
            go_forward(30, 0.5)
        elif signalbone()[1] == void:
            rightPointTurn(speed, time)

    elif signalbone()[0] == forward:
        if signalbone()[1] == forward:
            go_forward(30, 0.5)
        else:
            LeftPointTurn(50, 0.7)

    elif signalbone()[0] == right:
        rightPointTurn(speed, time)


if __name__ == "__main__":
    while True:
        go_forward(20)
        if signal() not in metaforward:
           mazer(30, 0.4)