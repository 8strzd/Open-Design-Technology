# Import the Pin class to work with ESP32 GPIO pins
from machine import Pin

# Import time module to add delays in the program
import time

Pbj = Pin(22, Pin.IN, Pin.PULL_UP)
Pbg = Pin(25, Pin.IN, Pin.PULL_UP)

while True:
    val_1 = Pbj.value()
    val_2 = Pbg.value()
    
    if val_1 == 0 and val_2 == 0:
        print("Both buttons pressed")

    
    elif val_1 == 0:
        print("1 button pressed")
    elif val_2 == 0:
        print("2 button pressed")
    time.sleep(0.1)
        