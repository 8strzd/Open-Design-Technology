from machine import Pin,PWM
import time

servo_list = [20, 80, 40, 90]

Chocolate = servo_list[0] #20
Candies = servo_list[1]#80
Cake = servo_list[2]#40
Dessert = servo_list[3]#90

ser = PWM (Pin(22), freq = 50)

for a in servo_list :
    servo.duty(a)
    time.sleep(0.3)