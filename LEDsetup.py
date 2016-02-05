
# coding: utf-8

# In[1]:

# The lines reset a driver called spidev, 
# that is used to drive the signal sent to the lights from the raspberry pi
from subprocess import call
call(["sudo", "chmod", "a+rw", "/dev/spidev0.0"])

# Importing some parts of a 'library' of programs called bibliopixel
# Bibliopixel has the all the functions we use to light up LEDs 
# like led.set(), led.fill() etc

from bibliopixel import *
from bibliopixel.drivers.LPD8806 import *
from bibliopixel.drivers.driver_base import *
from bibliopixel import LEDStrip

# Importing the library that has the function time.sleep()

import time


# In[2]:

# numLeds is the number of LEDs in our lamp
# we set the driver to the specific one that drives our LED lights 
# along with the information about how many lights there are
# Each color is a set of 3 numbers, 
# ChannelOrder says in what order the 3 colors Red, Green, Blue are organized
# in our case it is Blue Red Green (BRG)


numLeds=8*8
driver=DriverLPD8806(numLeds, ChannelOrder.BRG)

# We name our LEDstrips 'led'. 
# We tell the driver that it is a long string of LEDs, not a rectangle or any other shape

led=LEDStrip(driver)


# In[1]:

# Pre-defining colors in Red Green Blue order

Off = (0, 0, 0)
Blue = (0, 0, 255)
Pink = (255, 20, 147)
Purple = (128, 0, 128)
Fuchsia = (255, 0, 255)
Crimson = (220, 20, 60)
White = (255, 255, 255)
Brown = (110,45,10)
Yellow = (255, 155, 0)
Orange = (255, 100, 0)
Red = (255, 0, 0)
Gray = (50, 50, 30)
Green = (0, 255, 0)
Violet = (238, 130, 238)
Beige = (245, 145, 100)
Black = (0, 0, 0)
Turquoise = (64, 224, 188)
Indigo = (75, 0, 130)
Lime = (0, 255, 75)
Khaki = (240, 150, 60)
Maroon = (70, 0, 0)
Gold = (255, 140, 0)

