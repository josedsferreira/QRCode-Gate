import cv2
import fbase
from time import time
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)

def openGate():
    GPIO.output(14,GPIO.HIGH)
    print("Gate Opening")
    sleep(5)
    GPIO.output(14,GPIO.LOW)
    print("Gate Closing")