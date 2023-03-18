import pigpio

SERVO = 18
pi = pigpio.pi()

pi.set_mode(SERVO, pigpio.OUTPUT)
pi.set_servo_pulsewidth(SERVO, 1500)