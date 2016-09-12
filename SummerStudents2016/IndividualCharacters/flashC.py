from LEDsetup import*

def flashC(color,TimeOn,TimeOff):
	c=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,37,47,57,67,77,76,66,72,71,62,61,51,41,31,21,11]
	for i in c:
		led.set(i,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)
