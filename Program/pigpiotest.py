import pigpio


pi = pigpio.pi()
pi.set_servo_pulsewidth(12, 1500)
while True:
    pass