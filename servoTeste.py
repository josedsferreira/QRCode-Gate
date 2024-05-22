import RPi.GPIO as GPIO
from time import sleep

# duty cycle, calibrate if needed
MIN_DUTY = 3
MAX_DUTY = 10

servo_signal_pin = 13

def deg_to_duty(deg):
    return (deg - 0) * (MAX_DUTY- MIN_DUTY) / 180 + MIN_DUTY

if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(servo_signal_pin, GPIO.OUT)
    # set pwm signal to 50Hz
    servo = GPIO.PWM(servo_signal_pin, 50)
    print("Opening Gate")
    servo.start(0)
    sleep(2)
    servo.stop()
    

    sleep(5)
    print("Closing Gate")
    servo.start(70)
    sleep(2)
    servo.stop()
    

    # cleanup the gpio pins
    GPIO.cleanup()
