#Import necessary modules
#Import Class Pin from module machine
#import a module to give delay
from machine import Pin
import time
import neopixel #import module for neopixel
#Make an object for the neopixel
my_np = neopixel.NeoPixel(Pin(32, Pin.OUT),16)

for my_np[1,0] in range (0,5)
    my_np[1]=(100,0,0)
    my_np[2]=(0,0,100)
    my_np[3]=(0,100,0)
    my_np[4]=(10,20,10)
    my_np[5]=(0, 100, 100)
    my_np[6]=(100,100,100)
    my_np[7]=(100,0,100)
    my_np[8]=(100,0,50)
    my_np[9]=(50,50,50)
    my_np.write()
    time.sleep(1)
    
    my_np[10]=(100,0,0)
    my_np[11]=(0,0,100)
    my_np[12]=(0,100,0)
    my_np[13]=(10,20,10)
    my_np[14]=(0, 100, 100)
    my_np[15]=(100,100,100)
    my_np[0]=(100,0,100)
    my_np.write()
    time.sleep(3)
    
    my_np[1]=(100,0,0)
    my_np[2]=(0,0,100)
    my_np[3]=(0,100,0)
    my_np[4]=(10,20,10)
    my_np[5]=(0, 100, 100)
    my_np[6]=(100,100,100)
    my_np[7]=(100,0,100)
    my_np[8]=(100,0,50)
    my_np[9]=(50,50,50)
    my_np[10]=(100,0,0)
    my_np[11]=(0,0,100)
    my_np[12]=(0,100,0)
    my_np[13]=(10,20,10)
    my_np[14]=(0, 100, 100)
    my_np[15]=(100,100,100)
    my_np[0]=(100,0,100)
    time.sleep(1)
  