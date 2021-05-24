# IMPORT MODULES
import RPi.GPIO as GPIO
import time
import math

def calc_distance():
    GPIO.setmode(GPIO.BCM)

    TRIG = 13
    ECHO = 19

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    GPIO.setwarnings(False)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start

    distance = sig_time / 0.000058
    # while True
    # print(math.floor(distance))

    # Return rounded down distance
    return math.floor(distance)

    GPIO.cleanup()
# calc_distance()