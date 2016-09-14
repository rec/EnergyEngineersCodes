
###############################################################

# This is a demo program for the Energy Engineers.

###############################################################

from bibliopixel import *
from bibliopixel.drivers.LPD8806 import *
from bibliopixel import LEDStrip

import time

from numpy import random

# ### Shell commands to reset spidev

from subprocess import call
call(["sudo", "chmod", "a+rw", "/dev/spidev0.0"])


# ### Initial setup
numStrips = 1
numLeds= 10 * numStrips

driver=DriverLPD8806(numLeds, ChannelOrder.BRG, False)
led=LEDStrip(driver)

# ### Each LED turns on serially
# ####Once done they all flash ON & OFF till user ends the program with CTRL + C

# In[ ]:

led.fillRGB(0,0,0) # turns everything off
led.update()


# Pick Random Color

color = (random.randint(1,180), random.randint(1,180), random.randint(1,180))

for i in range (numLeds):
    print ('LED '+str(i+1))
    led.set(i, color)
    led.update()
    time.sleep(0.25)

print ('All LEDs!')

# Pre-defining colors in Red Green Blue order

Off = (0, 0, 0)
On = (255, 255, 255)
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


