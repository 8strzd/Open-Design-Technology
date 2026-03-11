from machine import Pin

import time
import random

led1 = Pin(13, Pin.OUT)
pb1 = Pin(14, Pin.IN, Pin.PULL_UP)
pb2 = Pin(27, Pin.IN, Pin.PULL_UP)
randomdelay = random.randint(1000,5000)
    
while True:
# Stage 1
    led1.on()
    time.sleep(0.1)
    led1.off()
    time.sleep(0.1)
    
    control = pb1.value()
    if control == 0:
        led1.on()
        time.sleep(2)
        led1.off()
        
        time.sleep_ms(randomdelay)
        led1.on()
        
        t1 = time.ticks_ms()
        
        while pb2.value() == 1:
            pass
        
        t2 = time.ticks_ms()

        result = time.ticks_diff(t2, t1)
        print("Reaction Time")
        print(result)