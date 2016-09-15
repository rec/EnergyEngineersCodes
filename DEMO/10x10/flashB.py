from LEDsetup import*

def flashB(color,TimeOn,TimeOff):
	b=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,34,37,41,44,47,51,54,57,61,64,65,66,67,71,72,73,74]
	for i in b:
		led.set(i,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)
