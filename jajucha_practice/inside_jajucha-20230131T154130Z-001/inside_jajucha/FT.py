import socket
import time
from imutils.video import VideoStream
import imagezmq
import time
import threading
import cv2
import pigpio
import adafruit_vl53l0x
import busio
import board
import zmq
import pigpio


#motor pin setting
ENABLE = 14
SLEEP = 15
MS1 = 17
MS2 = 27
MS3 = 22
SERVO = 18
DIR = 23

#GPIO init
pi = pigpio.pi()

#pin mode seeting
pi.set_mode(ENABLE, pigpio.OUTPUT)
pi.set_mode(SLEEP, pigpio.OUTPUT)
pi.set_mode(SERVO, pigpio.OUTPUT)
pi.set_mode(DIR, pigpio.OUTPUT)

#stop the motor and set the diretion
pi.write(ENABLE, 1)
pi.write(SLEEP, 0)
pi.write(DIR, 0)

#lidar sensor setting
i2c = busio.I2C(board.SCL, board.SDA)
lidar = adafruit_vl53l0x.VL53L0X(i2c)

sender = imagezmq.ImageSender(connect_to='tcp://*:11205', REQ_REP=False)
rpi_name = socket.gethostname() # send RPi hostname with each image
print(rpi_name)
picam = VideoStream(usePiCamera=True,resolution = (320,240)).start()
time.sleep(2.0)  # allow camera sensor to warm up

#zmq setting
context = zmq.Context()
socket = context.socket(zmq.SUB)

class Jajcha_rpi:
    def __init__(self):
        print('initiated')
        socket.connect('tcp://192.168.0.101:10523')
        #socket.connect('tcp://*:6000')
        socket.setsockopt_string(zmq.SUBSCRIBE,"command!")
        sending_thread = threading.Thread(target = self.image_lidar_sending)    
        sending_thread.start() #starting main thread(image_transmitting)
        getting_thread = threading.Thread(target = self.getting_command_control)  
        getting_thread.daemon = True #if the main thread ends, the sub thread will end simultaneously  
        getting_thread.start() #starting sub thread(robot_controlling thread)

    def init_motor(self):
        pi.set_mode(MS1, pigpio.OUTPUT)
        pi.set_mode(MS2, pigpio.OUTPUT)
        pi.set_mode(MS3, pigpio.OUTPUT)

        pi.write(MS1,1) #microstepping pin 1 setting
        pi.write(MS2,1) #microstepping pin 2 setting
        pi.write(MS3,1) #microstepping pin 3 setting
    
    def enable_motor(self):
        pi.write(ENABLE, 0)
        pi.write(SLEEP, 1)

    def disable_motor(self):
        pi.write(ENABLE, 1)
        pi.write(SLEEP, 0)
    

    ######################## Main function1 ######################
    def image_lidar_sending(self):
        while True:  # send images until Ctrl-C
            front_frame = picam.read()
            jpeg_quality= 20
            ret_code, jpg_buffer= cv2.imencode(".jpg", front_frame, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality])     
            sender.send_jpg(lidar.range ,jpg_buffer) # send lidar,image
            time.sleep(0.01)
    ###############################################################


    ######################## Main function2 ######################
    def getting_command_control(self):
        while True:
            command = socket.recv()
            command = str(command)
            sp = command.split('!')
            speed = sp[1]
            steer = sp[2].replace("'","")
            self.motor_control(speed) #Calling stepper motor control function
            self.servo_control(steer) #Calling servo motor control function
            print(speed,steer)      
    ###############################################################


    
    def motor_control(self,speed):
        speed = int(speed)
        self.init_motor()
        if(speed == 0):
            self.disable_motor()
        elif(speed != 0):
            self.enable_motor()
            input_value = int(int(speed) * 100)
            pi.hardware_PWM(13,input_value, input_value*2)
        
    def servo_control(self,steer):
        steer = int(steer)
        pi.set_mode(SERVO, pigpio.OUTPUT)
        pi.set_servo_pulsewidth(SERVO, steer * 10)
        pass

if __name__=='__main__':
    jr = Jajcha_rpi() # Make the instance(only __init_ function will called)







