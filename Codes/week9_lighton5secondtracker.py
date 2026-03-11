from machine import Pin
import time

pb1 = Pin (14, Pin.IN, Pin.PULL_UP)
pb2 = Pin (18, Pin.IN, Pin.PULL_UP)
red = Pin (32, Pin.OUT, Pin.PULL_UP)

while True:
    star = pb1.value()
    light = pb2.value()
    
    if star == 0 :
        print ("Start Estimating 5 seconds!")
        red.on()
        start = time.ticks_ms()
        time.sleep(0.5)
    
    if light == 0 :
        end = time.ticks_ms()
        time.sleep(0.5)
        d = time.ticks_diff(end,start)
        print (5000 - start)
        red.off()
        
    time.sleep (0.5)