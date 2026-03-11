from machine import Pin, PWM
import time
servo_list = [20, 80]

Front = servo_list[0]
Back = servo_list[1]

serv = PWM(Pin(18), freq = 50)
pb1 = Pin(26, Pin.IN, Pin.PULL_UP)

while True:
    pbval = pb1.value()
    
    if pbval == 0:
        time.sleep(1)
        serv.duty(Front)
        time.sleep(1)
        serv.duty(Back)
        time.sleep(1)
        