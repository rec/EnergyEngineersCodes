from LEDsetup import*

def flashSpace(color,TimeOn,TimeOff):
        led.fill(Off)
        led.update()
        time.sleep(TimeOn)
        led.fill(Off)
        led.update()
        time.sleep(TimeOff)
