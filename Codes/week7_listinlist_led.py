from machine import Pin
import time

pos = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

led1= Pin(21,Pin.OUT)
led2=Pin(32,Pin.OUT)
led3=Pin(25,Pin.OUT)
led4=Pin(14,Pin.OUT)
my_t = 0.5

while True:
    for i in pos:
        led1.value(i[0])
        led2.value(i[1])
        led3.value(i[2])
        led4.value(i[3])
        time.sleep(my_t)