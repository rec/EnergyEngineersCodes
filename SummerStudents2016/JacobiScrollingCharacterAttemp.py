from LEDsetup import*
from flash_c import*
led.fill(Off)
led.update()


#while True:
      #a=[11,12,13,14,15,21,22,23,24,25,26,33,36,37,43,47,53,57,63,66,71,72,73,74,75]

      #counter = 0

      #while counter < 90:
            #for i in a:
              #    led.set(i + counter, Purple)
            #led.update()
           # time.sleep(0.2)
           # led.fill(Off)
            #led.update()
           # counter = counter + 10


#while True:
     # b=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,34,37,41,44,47,51,54,57,61,64,65,66,67,71,72,73,74]

      #counter = 0

    #  while counter < 90:
            #for i in b:
           #       led.set(i + counter, Purple)
           # led.update()
           # time.sleep(0.2)
            #led.fill(Off)
            #led.update()
            #counter = counter + 10

while True:
      #c=[11,12,13,14,15,16,17,21,22,23,24,25,26,27,37,47,57,67,77,76,66,72,71,62,61,51,41,31,21]
      flash_c()
      counter = 0

      while counter < 90:
            for i in flash_c:
                  led.set(i + counter, Purple)
            led.update()
            time.sleep(0.2)
            led.fill(Off)
            led.update()
            counter = counter + 10

