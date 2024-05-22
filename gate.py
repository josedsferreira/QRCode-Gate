import cv2
import fbase
from time import time
from time import sleep
import RPi.GPIO as GPIO

min_position = 1
max_position = 13
step = 1 # tem de ser inteiro
servo_signal_pin = 13

def openGate():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_signal_pin, GPIO.OUT)
    # pwm signal 50Hz
    servo = GPIO.PWM(servo_signal_pin, 50)
    servo.start(0)

    print("Opening Gate")
    for i in range(min_position, max_position, step):
        servo.ChangeDutyCycle(i)
        sleep(0.5)

    sleep(5)

    print("Closing Gate")
    for i in range(max_position, min_position, -step):
        servo.ChangeDutyCycle(i)
        sleep(0.5)

    # cleanup gpio pins
    GPIO.cleanup()
