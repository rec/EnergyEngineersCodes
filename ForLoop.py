
from LEDsetup import*

while(True):

	for x in range(0,40):
		led.set(x,Red)
		led.set(x+45,Gold) 
		led.update()		
		time.sleep(0.03)
		led.set(x,Off)
		led.set(x+40,Off)
		led.update()	
		time.sleep(0.03)
		









