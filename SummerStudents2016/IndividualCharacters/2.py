from LEDsetup import*
led.fill(Off)
led.update()

def Two(Color):
        two=[11,12,16,17,21,22,26,27,31,33,37,41,43,47,51,54,55,56,57,61,64,65,66,67,71]
        for i in two:
            led.set(i,Color)
            led.update()
        return
Two(Green)
