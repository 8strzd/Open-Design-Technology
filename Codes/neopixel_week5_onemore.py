from machine import Pin
import neopixel

my_np = neopixel.NeoPixel(Pin(32, Pin.OUT),16)

for anything in range(0,15,1):#range(start,ends,increments)
    my_np[anything]=(0,0,100)
    