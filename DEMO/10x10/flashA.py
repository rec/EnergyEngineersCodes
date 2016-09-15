from LEDsetup import*

def flashA(color,TimeOn,TimeOff):
	a=[11,12,13,14,15,21,22,23,24,25,26,33,36,37,43,47,53,57,63,66,71,72,73,74,75]
	for i in a:
		led.set(i,color)
	led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)




