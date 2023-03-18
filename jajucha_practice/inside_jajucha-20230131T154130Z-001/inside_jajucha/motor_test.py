import pigpio

ENABLE = 14
SLEEP = 15
pi = pigpio.pi()
pi.set_mode(17, pigpio.OUTPUT)
pi.set_mode(27, pigpio.OUTPUT)
pi.set_mode(22, pigpio.OUTPUT)
pi.set_mode(23, pigpio.OUTPUT)
pi.write(17, 1)
pi.write(27, 1)
pi.write(22, 1)
pi.write(23, 0)
pi.write(ENABLE, 1)
pi.write(SLEEP, 1)

while True:
    pi.hardware_PWM(13,0, 28000)