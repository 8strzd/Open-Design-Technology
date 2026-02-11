from machine import Pin
import time

led = Pin(14, Pin.OUT)

while True:
    led.on()
    time.sleep(0.25)
    led.off()
    time.sleep(0.75)
    
while True:
    led.on()
    time.sleep(0.50)
    led.off()
    time.sleep(0.50)
    
