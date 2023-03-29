#This code is for testing image capturing on the beaglebone via a webcam

#OpenCV imports
import cv2

#Setting camera object (if more than one webcam connected, pass in the respective cam number) 
cam = cv2.VideoCapture(0)

#Setting frame size and resolution
cam.set (cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
cam.set (cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 720)

#Reading frames
cam.read()

cv2.waitKey(10)

#Showing image on screen for testing
cv2.imshow("Test Picture", img)

#Saving image file
cv2.imwrite("demopic.bmp", img)
