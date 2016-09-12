from LEDsetup import*
led.fill(Off)
led.update()

def Equal(Color):
    equal=[15,25,35,45,55,65,75,13,23,33,43,53,63,73]
    for i in equal:
        led.set(i,Color)
        led.update()
    return

Equal(Gold)

