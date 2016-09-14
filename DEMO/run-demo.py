
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

# Pick Random Color

color = (random.randint(1,180), random.randint(1,180), random.randint(1,180))

# ### Each LED turns on serially
# ####Once done they all flash ON & OFF till user ends the program with CTRL + C

# In[ ]:

led.fillRGB(0,0,0) # turns everything off
led.update()

for i in range (numLeds):
    print ('LED '+str(i+1))
    led.set(i, color)
    led.update()
    time.sleep(0.25)

print ('All LEDs!')

