import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep
import sys
from ultraModule import getDistance
from TurnModule import *
from go_any import *
import os

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
pwm_setup()

def onKeyPress(event):
    key = event.char
    text.insert('end', 'You pressed %s\n' %key)
    if key == 'w':
        go_forward(50,0.1)
    if key == 'a':
        leftSwingTurn(50,0.1)
    if key == 's':
        go_backward(50,0.1)
    if key == 'd':
        rightSwingTurn(50,0.1)
    if key == 'q':
        leftPointTurn(50,0.1)
    if key == 'e':
        rightPointTurn(50,0.1)
    if key == 'b':
        go_forward(100,0,1)
    if key == 'l':
        GPIO.cleanup()
        pwm_low()
        os.system("exit")


if __name__ == "__main__":
    try:
        root = tk.Tk()
        root.geometry('300x200')
        text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
        text.pack()
        root.bind('<KeyPress>', onKeyPress)
        root.mainloop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        pwm_low()
