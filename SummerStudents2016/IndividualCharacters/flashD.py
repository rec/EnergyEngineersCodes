from LEDsetup import*

def flashD(color,TimeOn,TimeOff):
	d=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,37,41,47,51,57,66,61,71,72,73,74,75]
	for i in d:
		led.set(i,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)
