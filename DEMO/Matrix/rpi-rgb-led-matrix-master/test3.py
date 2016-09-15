from bibliopixel import *
import bibliopixel.colors as colors
from adamatrix import DriverAdaMatrix

driver = DriverAdaMatrix(rows=32, chain=1)
driver.SetPWMBits(6) #decrease bit-depth for better performance
#MUST use serpentine=False because rgbmatrix handles the data that way
led = LEDMatrix(driver, 32, 32, serpentine=False)

#Must have code downloaded from GitHub for matrix_animations
from matrix_animations import *
import bibliopixel.log as log
log.setLogLevel(log.DEBUG)

try:
    anim = ScrollText(led, text = 'Energy Engineers! ', yPos = 4, color = colors.Green, size = 3)
    anim.run(fps = 25, max_steps = 1000)
except KeyboardInterrupt:
    led.all_off()
    led.update()

try:
    anim = Bloom(led)
    anim.run(fps = 25, max_steps = 100)
except KeyboardInterrupt:
    led.all_off()
    led.update()

try:
    anim = MatrixRainBow(led)
    anim.run(fps = 25, max_steps = 200)
except KeyboardInterrupt:
    led.all_off()
    led.update()

try:
    anim = SpiningTriangle(led, 15,15, 10)
    anim.run(fps = 50, max_steps = 500)
except KeyboardInterrupt:
    led.all_off()
    led.update()

try:
    anim = ScrollText(led, text = 'Energy Engineers! ', yPos = 4, color = colors.Blue, size = 3)
    anim.run(fps = 25, max_steps = 1000)
except KeyboardInterrupt:
    led.all_off()
    led.update()


