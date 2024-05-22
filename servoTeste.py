import RPi.GPIO as GPIO
from time import sleep

min_position = 1
max_position = 13
step = 1 # tem de ser inteiro

servo_signal_pin = 13

if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(servo_signal_pin, GPIO.OUT)
    # set pwm signal to 50Hz
    servo = GPIO.PWM(servo_signal_pin, 50)
    servo.start(0)

    print("Opening Gate")
    for i in range(min_position, max_position, step):
        servo.ChangeDutyCycle(i)
        sleep(0.5)

    sleep(1)

    print("Closing Gate")
    for i in range(max_position, min_position, -step):
        servo.ChangeDutyCycle(i)
        sleep(0.5)

    # cleanup the gpio pins
    GPIO.cleanup()
