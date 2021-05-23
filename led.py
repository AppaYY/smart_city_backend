# IMPORT MODULES
import RPi.GPIO as GPIO
import time

green_pin = 21
red_pin = 20

def set_light(location):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(location, GPIO.OUT)
    
    GPIO.output(location, GPIO.HIGH)

def set_green_light():
    set_light(green_pin)

def set_red_light():
    set_light(red_pin)

def set_output_off():
    GPIO.setup(green_pin, GPIO.OUT)
    GPIO.setup(red_pin, GPIO.OUT)
    GPIO.output(green_pin, GPIO.LOW)
    GPIO.output(red_pin, GPIO.LOW)