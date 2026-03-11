from machine import Pin, PWM
import time
servo = PWM(Pin(33), freq=50)
pb1 = Pin(13, Pin.IN, Pin.PULL_UP)

while True:

    if pb1.value() == 0:
        servo.duty(80)     
        time.sleep(1)
        servo.duty(23)   
        time.sleep(1)
        
        while pb1.value() == 0:
            time.sleep(0.1)

    else:
        time.sleep(0.1)