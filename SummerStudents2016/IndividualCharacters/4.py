from LEDsetup import*
led.fill(Off)
led.update()

def Four(Color):
    four=[15,16,17,25,26,27,35,45,51,52,53,54,55,61,62,63,64,65,66,67]
    for i in four:
        led.set(i,Color)
        led.update()
    return
Four(Pink)
