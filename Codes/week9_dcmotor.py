from machine import Pin
import time

in1 = Pin(22,Pin.OUT)
in2 = Pin(23,Pin.OUT)

while True:
    in1.on()
    in2.off()
    time.sleep(3)
    in1.off()
    in2.on()
    time.sleep(3)