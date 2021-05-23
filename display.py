# Configuration for data calls
from datetime import datetime

# Configuration for oled
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Setup display 
i2c = busio.I2C(board.SCL, board.SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c, reset=None)
disp.poweron()

# Define fonts on display
smallfont = ImageFont.truetype('FreeSans.ttf', 13)
largefont = ImageFont.truetype('FreeSans.ttf', 20)

# Clear display
disp.fill(0)
disp.show()

# Make object for draw
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

def display_message(top_line, line_2, line_3):
    disp.poweron()
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 0), top_line, font=largefont, fill=255)
    draw.text((0, 35), line_2, font=smallfont, fill=255)
    draw.text((0, 50), line_3, font=smallfont, fill=255)
    disp.image(image)
    disp.show()

def shut_oled():
    disp.poweroff()