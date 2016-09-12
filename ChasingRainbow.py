
from LEDsetup import*

while(True):
	
	for x in range(0,85):
		led.set(x,Red)
		led.set(x-1,Orange)
		led.set(x-2,Yellow)
		led.set(x-3,Green)
		led.set(x-4,Blue)
		led.set(x-5,Purple)
		led.update()
		time.sleep(0.03)
		led.set(x-5,Off)
		led.update()
