import cv2
import fbase
from time import time
from time import sleep
import RPi.GPIO as GPIO

# Constantes do servo
min_position = 0
max_position = 13
step = 1 # tem de ser inteiro
servo_signal_pin = 13 # Pin do servo

# Constantes do sensor
TRIG_PIN = 17 # Pin Trig do sensor
ECHO_PIN = 27 # Pin Echo do sensor
distancia_limite = 50 # distancia da cancela

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_signal_pin, GPIO.OUT)
servo = GPIO.PWM(servo_signal_pin, 50) # pwm signal 50Hz
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def startGate():

    servo.start(0) # posição inicial do servo

    openGate()

    sleep(5)

    closeGate()

    # cleanup gpio pins
    GPIO.cleanup()

def openGate(start_pos=min_position):
    # start_pos: posição da cancela quando iniciar movimento de abertura
    print("Opening Gate")
    for i in range(start_pos, max_position, step):
        servo.ChangeDutyCycle(i)
        sleep(0.5)

def closeGate():
    print("Closing Gate")
    
    # nao deu para usar o ciclo for each normal pq nao permitia mudar o valor de i dentro do ciclo
    i = max_position 
    while i >= min_position:
        if distance() < distancia_limite: # se detetar obstrução -> recomeça o ciclo abrir/fehar
            openGate(start_pos=i) # começa a subir a cancela a partir da posição atual
            sleep(5)
            i = max_position # reset do valor de i
        servo.ChangeDutyCycle(i)
        i -= step
        sleep(0.5)

def distance():
    # Dar trigger the pulso de 10 microsegundos
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Medir duração do pulso do ECHO
    pulse_start = time()
    pulse_end = pulse_start

    while GPIO.input(ECHO_PIN) == 0 and time() - pulse_start < 0.1:
        pulse_start = time()

    while GPIO.input(ECHO_PIN) == 1 and time() - pulse_end < 0.1:
        pulse_end = time()

    duration = pulse_end - pulse_start

    # Calcular distancia em cm
    distance_cm = duration * 34300 / 2

    return round(distance_cm, 2)