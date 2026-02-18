from machine import Pin, PWM
import time

ser = PWM(Pin(22), freq=50)
ser.duty(35)
time.sleep(0.5)
ser.duty(77)
time.sleep(0.5)
ser.duty(180)
time.sleep(0.5)