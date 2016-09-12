from LEDsetup import*
led.fill(Off)
led.update()

def W(Color):
     w=[11,17,22,23,27,29,31,37,3,42,44,45,47,52,55,59,63,69,73,79,83,90]
     for i in w:
         led.set(i,Color)
         led.update()
     return

W(Gold)





# just goofing off below here
time.sleep(0.5)
W(Blue)
time.sleep(0.5)
W(White)

