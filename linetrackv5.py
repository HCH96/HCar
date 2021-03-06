import RPi.GPIO as GPIO
from trackingModule import *
from time import sleep
from TurnModule import *
from go_any import *
from ultraModule import getDistance


# set GPIO warnings as flase
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)


# REVERSE
def REVERSE(x):
    if x == True:
        return False
    elif x == False:
        return True

#
forward0 = True
forward1 = False

#
backward0 = REVERSE(forward0)
backward1 = REVERSE(forward1)

#
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37


#
def leftmotor(x):
    if x == True:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    elif x == False:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    else:
        print('Config Error')


#
def rightmotor(x):
    if x == True:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    elif x == False:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    else:
        print('Config Error')


#
GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

pwm_setup()


#
LeftPwm = GPIO.PWM(MotorLeft_PWM, 1)
RightPwm = GPIO.PWM(MotorRight_PWM, 1)


#
def go_straight(speed, running_time):
    leftmotor(forward1)
    leftmotor(forward0)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightmotor(forward1)
    rightmotor(forward0)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    time.sleep(running_time)
    signal()


#
def leftcurveturn(speed, running_time):
        leftmotor(forward0)
        GPIO.output(MotorLeft_PWM, GPIO.HIGH)
        rightmotor(forward0)
        GPIO.output(MotorRight_PWM, GPIO.HIGH)
        LeftPwm.ChangeDutyCycle(speed)
        RightPwm.ChangeDutyCycle(0)
        time.sleep(running_time)
        signal()


#
def curveforobs(speed, speed2, running_time):
    leftmotor(forward0)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightmotor(forward0)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed2)
    time.sleep(running_time)


#
def rightcurveturn(speed, running_time):
    leftmotor(forward0)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightmotor(forward0)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(speed)
    time.sleep(running_time)
    signal()

# =======================================================================
# define the stop module
# =======================================================================

def stop():
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)


def pwm_setup():
    LeftPwm.start(0)
    RightPwm.start(0)


def pwm_low():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()

dis = 15

try:
    while True:
        signal()
        distance = getDistance()
        if distance < dis and distance > 10:
            print('obstacle')
            stop()
            sleep(0.3)
            rightPointTurn(40,0.3)
            stop()
            sleep(1)
            go_forward(30,0.5)
            stop()
            sleep(1)
            leftPointTurn(40, 0.6)
            stop()
            sleep(1)
            go_forward(30,0.7)
            stop()
            sleep(1)
            leftPointTurn(40,0.6)
            stop()
            sleep(0.3)
            while signal()[0] == 1:
                go_straight(0.1,0.1)
                signal()
        else:
            if signal()[0] == 1  and signal()[4] == 1:
                if signal()==(1,1,1,1,1):
                    leftSwingTurn(100)
                    signal()
                elif signal()[1] == 0:
                    leftSwingTurn(100)
                elif signal()[3] == 0:
                    rightSwingTurn(30)
                else:
                    go_straight(0.01,0.01)
                    distance = getDistance()
                    signal()
            elif signal()[0] == 0 and signal()[4] == 1:
                if signal()[1] == 0:
                    leftSwingTurn(100)
                    signal()
                elif signal()[1] == 1:
                    leftSwingTurn(100)
                    signal()
            elif signal()[0] == 1 and signal()[4] == 0:
                if signal()[3] == 0:
                    rightSwingTurn(50)
                    signal()
                elif signal()[3] == 1:
                    rightSwingTurn(30)
                    signal()
            elif signal() == (0,0,0,0,0):
                pwm_low()
except KeyboardInterrupt:
    pwm_low()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
