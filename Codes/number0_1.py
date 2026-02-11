from machine import Pin
import time

#initializion
pb =Pin (32,Pin.IN,Pin.PULL_UP)

while True:
    con = pb.value()
    print(con)
    if con== 0:
        print("Button Pressed")
    time.sleep(0.2)
    