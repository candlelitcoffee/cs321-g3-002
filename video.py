#Code for capturing videos on the BBB via a webcam (EMeet c950)
#Needs testing


#OpenCV imports
import cv2

#Setting camera object (if more than one webcam connected, pass in the respective cam number) 
cam = cv2.VideoCapture(0)

#Checking if camera opened successfully
if (cam.isOpened() == False):
    print("Error opening camera")

#Setting resolution
width = int(cam.get(3))
height = int(cam.get(4))
size = (width, height)
print(size)

#Creating and saving a video
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
video = cv2.VideoWriter('frame.avi', cv2.VideoWriter_fourcc(*'MJPG'), 12, size)

#Recording for 5 seconds
i = 0
while i < 500:

    temp, frame = cam.read()

    #While a frame is read, adding it to the frame.avi video file
    if temp == True:
        video.write(frame)

        #Display frame for checking
        cv2.imshow('Frame', frame)

        i += 1
        print(i)
    else:
        break
        
cam.release()
video.release()

#Closing all frames
cv2.destroyAllWindows()

print("video saved successfully")

