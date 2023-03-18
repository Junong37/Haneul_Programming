import socket
import time
from imutils.video import VideoStream
import imagezmq
import time
# Accept connections on all tcp addresses, port 5555
sender = imagezmq.ImageSender(connect_to='tcp://*:5555', REQ_REP=False)

rpi_name = socket.gethostname() # send RPi hostname with each image
picam = VideoStream(usePiCamera=True).start()
time.sleep(2.0)  # allow camera sensor to warm up
while True:  # send images until Ctrl-C
    image = picam.read()
    sender.send_image(rpi_name, image)  
    time.sleep(0.05)
    print('sent')    # The execution loop will continue even if no subscriber is connected