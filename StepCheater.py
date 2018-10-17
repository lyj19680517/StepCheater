import RPi.GPIO as GPIO
import tkinter
import time


count = 0
angle = 0

def DriveInit():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    global do
    do = GPIO.PWM(18, 50)

def DriveExec():
    global do
    global angle
    while True:
        do.start((angle/180*(2.5-0.5)+0.5)/20)

