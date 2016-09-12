# This program makes a square scroll left to right. Shizil dizil.

from LEDsetup import*
led.fill(Off)
led.update()


while True:
      letter = [6,16,5,15]

      counter = 0

      while counter < 90:
            for i in letter:
                  led.set(i + counter, Purple)
            led.update()
            time.sleep(0.1)
            led.fill(Off)
            led.update()
            counter = counter + 10
     
      















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                                                                                                















