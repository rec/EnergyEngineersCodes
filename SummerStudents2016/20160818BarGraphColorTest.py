

from LEDsetup import*

led.fill(Off)
led.update()
time.sleep(0.1)

        
for i in range(0,100,10):
    led.set(i,Green)
for x in range(1,100,10):
    led.set(x,(135,215,0))
    
for y in range(2,100,10):
    led.set(y,(155,185,0))
    
for z in range(3,100,10):
    led.set(z,(180,175,0))
    
for a in range(4,100,10):
    led.set(a,(201,155,0))
    
for b in range(5,100,10):
    led.set(b,Yellow)
    
for c in range(6,100,10):
    led.set(c,Orange)
    
for d in range(7,100,10):
    led.set(d,(255,65,0))
    
for e in range(8,100,10):
    led.set(e,(255,50,0))
    
for f in range(9,100,10):
    led.set(f,Red)


led.update()

