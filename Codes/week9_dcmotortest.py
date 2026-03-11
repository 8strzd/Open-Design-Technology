from machine import Pin, time_pulse_us
import time
trig = Pin(12, Pin.OUT)
echo = Pin(13, Pin.IN)

while True:
    # STEP 1: Send 10 µs Trigger Pulse
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()
    duration = time_pulse_us(echo, 1, 30000)  # 30 ms timeout
    # STEP 3: Check for Timeout Errors
    if duration < 0:
        print("No object detected (Timeout)")
    else:
        # STEP 4: Convert Duration to Distance (cm)
        # distance(cm) = duration / 58
        # Derived from:
        # Distance = (Speed of Sound × Time) / 2
        distance = duration / 58
        print("Distance:", distance, "cm")

    time.sleep(1)