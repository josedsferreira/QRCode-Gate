import cv2
import fbase
from time import time
from time import sleep
import RPi.GPIO as GPIO

# duty cycle, calibrate if needed
MIN_DUTY = 5
MAX_DUTY = 10

servo_signal_pin = 13

def deg_to_duty(deg):
    return (deg - 0) * (MAX_DUTY- MIN_DUTY) / 180 + MIN_DUTY
    

def openGate():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(servo_signal_pin, GPIO.OUT)
    # set pwm signal to 50Hz
    servo = GPIO.PWM(servo_signal_pin, 50)
    print("Opening Gate")
    servo.start(0)

    # loop from 0 to 180
    #for deg in range(181):
    #    duty_cycle = deg_to_duty(deg)    
    #    servo.ChangeDutyCycle(duty_cycle)

    sleep(10)
    print("Closing Gate")

    # loop from 180 to 0
    for deg in range(180, -1, -1):
        duty_cycle = deg_to_duty(deg)    
        servo.ChangeDutyCycle(duty_cycle)

    # cleanup the gpio pins
    #GPIO.cleanup()