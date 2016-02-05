
# coding: utf-8

# ### Importing Libraries

# In[1]:

from bibliopixel import *
from bibliopixel.drivers.LPD8806 import *
from bibliopixel import LEDStrip

import time


# ### Shell commands to reset spidev

# In[ ]:

from subprocess import call
call(["sudo", "chmod", "a+rw", "/dev/spidev0.0"])


# ### Initial setup

# In[ ]:

numLeds=64
driver=DriverLPD8806(numLeds)
led=LEDStrip(driver)

r = (0, 180, 0) # LEDs are GRB; 255 is too bright
g = (180, 0, 0)
b = (0, 0, 180)


# ### Each LED turns on serially
# ####Once done they all flash ON & OFF till user ends the program with CTRL + C

# In[ ]:

led.fillRGB(0,0,0) # turns everything off
led.update()

for i in range (numLeds):
    print ('LED '+str(i+1))
    led.set(i, b)
    led.update()
    time.sleep(0.25)

print ('All LEDs!')

