# IMPORT MODULES
from math import log
from gpiozero import Button
import RPi.GPIO as GPIO
import time
from firebase import Firebase

# IMPORT CLASSES
from led import set_green_light, set_red_light, set_output_off
from display import display_message, shut_oled
from lightsensor import check_container_status
from servo import lock_container

# Initialize Firebase class
realtime_firebase = Firebase(2, 0)

while True:
    try:
        time.sleep(1)
        # LIGHT SENSOR CHECK IF VALUE RETURNS OPEN
        if check_container_status() == "OPEN":
            realtime_firebase.insert_Firebase_Row()
        else :
            # print(realtime_firebase.get_container_info("status"))
            if realtime_firebase.get_container_info("status") == "True":
                set_green_light()
                lock_container("False")
            else:
                set_red_light()
                lock_container("True")
        
        GPIO.setmode(GPIO.BCM) # Use physical pin numbering
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        if GPIO.input(26) == GPIO.HIGH:
            display_message(realtime_firebase.get_city_info(), realtime_firebase.get_container_info("street_name"), realtime_firebase.get_container_info("container_depth"))
    except KeyboardInterrupt:
        shut_oled()
        set_output_off()
        break