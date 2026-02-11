from machine import Pin, Touchpad
import time
#Initializion
tp = TouchPad(Pin (4))
strzd = Pin(23, Pin.OUT)
while True:  
 touch_value = tp.read()
 if touch_value < 100 :
     strzd.on()
     time.sleep(2)
     strzd.off()
     print (touched)
     time.sleep(0.2)
     
