import cv2
from picamera2 import Picamera2
import time

pi_camera=Picamera2()
#convert the color mode to rgb
config=pi_camera.create_preview_configuration(main={"format":"RGB888"})
pi_camera.configure(config)

#start the pi camera and give it a second to set up
pi_camera.start()
time.sleep(1)

while True:
    #get a impage frame as a numpy array
    image=pi_camera.capture_array()

    #display the image
    cv2.imshow("VIdeo",image)

    #this waits for 1ms and if the 'q' key is pressed it breaks the loop
    if cv2.waitKey(1)==ord('q'):
        break
#close all the windows
cv2.destroyAllWindows()