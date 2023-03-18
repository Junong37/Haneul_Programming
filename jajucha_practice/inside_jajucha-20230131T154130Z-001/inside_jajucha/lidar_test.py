import pigpio
import adafruit_vl53l0x
import busio
import board
i2c = busio.I2C(board.SCL, board.SDA)

while True:
    lidar = adafruit_vl53l0x.VL53L0X(i2c)
    print(lidar.range)
