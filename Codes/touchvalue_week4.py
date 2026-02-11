from machine import Pin, TouchPad

#initialization

tp = TouchPad(Pin(12))

while true :
    touch_value = tp.read()
    if touch_value < 300 :
        print("touched")
    print(touch_value)
    time.sleep(0.2)    
    