from machine import Pin,PWM
import time

servo_list = [20, 80, 40, 90]

Chocolate = servo_list[0] #20
Candies = servo_list[1]#80
Cake = servo_list[2]#40
Dessert = servo_list[3]#90

serv = PWM (Pin(22), freq = 50)

while True :
    serv.duty(servo_list[0])
    time.sleep(0.5)
    serv.duty(servo_list[1])
    time.sleep(0.5)
    serv.duty(servo_list[2])
    time.sleep(0.5)
    serv.duty(servo_list[3])
    time.sleep(0.5)
    
    
    