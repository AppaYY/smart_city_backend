# IMPORT MODULES
import Adafruit_ADS1x15
import time

GAIN = 1
ANALOG_PORT = 0

adc = Adafruit_ADS1x15.ADS1115()

adc.start_adc(ANALOG_PORT, gain=GAIN)
time.sleep(0.1)

def check_container_status():
    value = adc.get_last_result()

    # print (value)
    if value > 24000:
        return "OPEN"
    else:
        return "CLOSE"

# print(check_container_status())