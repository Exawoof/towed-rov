import pigpio


pi = pigpio.pi()
pi.set_servo_pulsewidth(18, 1400)
while True:
    pass