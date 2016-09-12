from LEDsetup import *

count = 0










while(count < 50):


	count = count + 1


	led.fill(Maroon)


	led.update()
	time.sleep(0.5)
	led.fill(Off)
	led.update()
	time.sleep(0.5)
	



	led.fill(Gold)
	led.update()
	time.sleep(0.5)






