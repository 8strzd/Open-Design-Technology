from machine import Pin
import time

#Initialize Push Button
pb1 = Pin(4, Pin.IN, Pin.PULL_UP)
pb2 = Pin(14, Pin.IN, Pin.PULL_UP)

#initialization of Pin
red = Pin(25, Pin.OUT)
yellow = Pin(33, Pin.OUT)
red2 = Pin(32, Pin.OUT)
yellow2 = Pin(35,Pin.OUT)

while True:
    
    con = pb1.value()
    print(con)
    if con == 0:
        red.on()
        time.sleep(0.2)
        yellow.on()
        time.sleep(0.2)
        red2.on()
        time.sleep(0.2)
        yellow2.on()
        time.sleep(0.2)
    else :
        red.off()
        yellow.off()
        red2.off()
        yellow2.off()
        
        
        lol = pb2.value()
    print(lol)
    if lol == 0:
        red.on()
        time.sleep(0.2)
        yellow.on()
        time.sleep(0.2)
        red2.on()
        time.sleep(0.2)
        yellow2.on()
        time.sleep(0.2)
    else :
        red.off()
        yellow.off()
        red2.off()
        yellow2.off()