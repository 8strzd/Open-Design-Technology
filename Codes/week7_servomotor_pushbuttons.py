from machine import Pin, PWM
import time

pb1 = Pin(26, Pin.IN, Pin.PULL_UP)
pb2 = Pin(14, Pin.IN, Pin.PULL_UP)

vari = [40, 60, 90, 110]


servo = PWM(Pin(22), freq=50)

while True:
    button1 = pb1.value()
    button2 = pb2.value()
    
    if button1 == 0 and button2 == 1:
        for i in vari:
            servo.duty(i)
            time.sleep(0.5)
    
    if button1 == 1 and button2 == 0:
        for i in reversed(vari):
            servo.duty(i)
            time.sleep(0.5)