from math import log
from gpiozero import Button
import time

# from display import display_message
from firebase import Firebase
from led import set_blue_light, set_green_light, set_red_light
from display import display_message

realtime_firebase = Firebase(2, 0)

# Config shit
buttonPin = 17
button = Button(buttonPin)

uniqueInteger = 0
while True:
    time.sleep(1)

    try:
        line_one, line_two, line_three = realtime_firebase.insertFirebaseRow(uniqueInteger)

        # set_blue_light()
        # print(button.is_pressed)
        # if button.is_pressed:
        #     # line_one, line_two, line_three = realtime_firebase.clearTable()
        #     # # display_message(line_one, line_two, line_three)
        #     # set_red_light()
        display_message(line_one, line_two, line_three)

        #     print("testestt")
        #     break

        uniqueInteger += 1
    except KeyboardInterrupt:
        break