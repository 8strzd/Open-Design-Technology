from machine import Pin
import time

wes = time.ticks_us()
for i in range (5): 
    print ("falak")
    time.sleep (0.1)
anderson = time.ticks_us()
print ( anderson - wes )
