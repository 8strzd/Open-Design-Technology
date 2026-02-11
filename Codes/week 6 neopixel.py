from machine import Pin
import time
import neopixel

my_pbone = Pin (22, Pin.PULL_UP)
my_pbtwo = Pin (18, Pin.PULL_UP)
my_np = neopixel.NeoPixel(Pin(25, Pin.OUT),16)
count = 0

 for anything in range(0,16,1):#range(start,ends,increments)
    my_np[count]=(0,0,100)
    
while True:
    my_pbone_value = my_pbone.value
    my_pbtwo_value = my_pbtwo.value
    if my_pbone_value==(0):
    print("color glows")
    count= count+1
    print ("color")
        
    time.sleep(0.5)
    if my_pbtwo_value==(0):
    print("color doesnt glow")
    count= count-1
    print("removed")
    
        