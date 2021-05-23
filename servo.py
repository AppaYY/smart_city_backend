# IMPORT MODULES
import RPi.GPIO as GPIO
import time

def lock_container(boolean):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 

    GPIO.setup(25, GPIO.OUT)
    servo = GPIO.PWM(25, 50)
    servo.start(3)
    if boolean == "True":
        servo.ChangeDutyCycle(7.5)
        time.sleep(0.6)
        # print("LOCKED")
    else:
        servo.ChangeDutyCycle(2.5)
        time.sleep(0.6)
        # print("OPEN")
    GPIO.cleanup()

# lock_container("True")