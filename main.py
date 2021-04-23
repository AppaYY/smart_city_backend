from gpiozero import Button
import time

from display import display_message
from firebase import Firebase
from led import set_blue_light, set_green_light, set_red_light

realtime_firebase = Firebase(1, 2)

# Config shit
buttonPin = 17
button = Button(buttonPin)

uniqueInteger = 0
while True:
    time.sleep(1)

    try:
        line_one, line_two, line_three = realtime_firebase.insertFirebaseRow(uniqueInteger)
        display_message(line_one, line_two, line_three)

        set_blue_light()

        if button.is_pressed:
            line_one, line_two, line_three = realtime_firebase.clearTable()
            display_message(line_one, line_two, line_three)
            set_red_light()
            break

        uniqueInteger += 1
    except KeyboardInterrupt:
        break