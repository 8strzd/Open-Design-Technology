from machine import Pin
import time

pb1 = Pin (14, Pin.IN, Pin.PULL_UP)
pb2 = Pin (18, Pin.IN, Pin.PULL_UP)


while True :
    val1 = pb1.value()
    val2 = pb2.value()
    
    if val1 == 0 :
        t1 = time.ticks_us()
        
    if val2 == 0 :
        t2 = time.ticks_us()
        d = time.ticks_diff(t2,t1)
        print (d)
    
    time.sleep(0.1)

        
        