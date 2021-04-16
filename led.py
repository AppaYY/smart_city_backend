import RPi.GPIO as GPIO
import time

green_pin = 13
blue_pin = 21
red_pin = 26

def set_light(location, speed=0.5):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(location, GPIO.OUT)
    GPIO.output(location, GPIO.HIGH)

    time.sleep(speed)

    GPIO.output(location, GPIO.LOW)

    time.sleep(speed)


def set_blue_light():
    set_light(blue_pin)

def set_green_light():
    set_light(green_pin)

def set_red_light():
    set_light(red_pin)
