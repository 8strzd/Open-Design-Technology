#Entering the room and reach the Switch Board
from machine import Pin
import time

#Finding the associated Switch
astro = Pin(18, Pin.OUT)
strzd = Pin(15, Pin.OUT)
green = Pin(22, Pin.OUT)
bluey = Pin(21, Pin.OUT)

#Press the switch to ON the tubelight
count = 5
while count > -5 :
  astro.on()
  time.sleep(1)
  astro.off()
  strzd.on()
  time.sleep(1)
  strzd.off()
  green.on()
  time.sleep(1)
  green.off()
  bluey.on()
  time.sleep(1)
  bluey.off()
  count = count+1
  
  time.sleep(2)
  strzd.off()
  bluey.off()
  green.off()
  astro.off()