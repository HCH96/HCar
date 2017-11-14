import tkinter as tk
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

GPIO.setwarnings(False)
pwm_setup()

def onKeyPress(event):
    key = event.char
    text.insert('end', 'You pressed %s\n' %key)
    if key == 'w':
        go_forward(35,0.1)
    if key == 'a':
        leftSwingTurn(35,0.1)
    if key == 's':
        go_backward(35,0.1)
    if key == 'd':
        rightSwingTurn(35,0.1)
    if key == 'q':
        leftPointTurn(35,0.1)
    if key == 'e':
        rightPointTurn(35,0.1)


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
