import socket
import cv2
import numpy as np
def main():

# next create a socket object
    s = socket.socket()
    print ("Socket successfully created") 
    port = 55534
    s.bind(('', port))
    print ("socket binded to %s" %(port))

# put the socket into listening mode
    s.listen(5)
    print ("socket is listening")
    # Open the camera
    cap = cv2.VideoCapture(0)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while True:

# Establish connection with client.
        c, addr = s.accept()
        print ('Got connection from', addr )

# send a thank you message to the client. encoding to send byte type.
        c.send('Thank you for connecting'.encode())
        #calibrate('')
        direction = 'i'
        test =0
        servo_pos = 3
        drive_pos = 7.5
        # Convert the frame to bytes
        data = cv2.imencode('.jpg', frame)[1].tobytes()
    
        # Send the data to the client
        c.send(data)
    
        # Display the frame
        cv2.imshow('frame', frame)
        while(direction != 'q' and test < 10):
            direction = c.recv(1024).decode()
            test= test+1
            #strings = buf.decode()
            print("the buf is "+direction)
            #drive(num)
            if(direction == 'a'): #left
                print("i am turning left")
                servo_pos += 0.05
                servo_cycle = (0.055*(float(servo_pos)) + 3)
               # PWM.set_duty_cycle(SERVO_PIN, servo_cycle)
            elif(direction == 'd'): #right
                print("I am truning right")
                servo_pos -= 0.05
                servo_cycle = (0.055*(float(servo_pos)) + 3)
               # PWM.set_duty_cycle(SERVO_PIN, servo_cycle)
            elif(direction == 'w'): #forward
                print("I am going forward")
                drive_pos += 0.05
                if 10.0 >= drive_pos >= 5.0:
                    print("whatever")
        #            PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
            elif(direction == 's'): #backward
                print("I am going backward")
                drive_pos -= 0.05
                if 10.0 >= drive_pos >= 5.0:
                    print("whatever 2")
         #           PWM.set_duty_cycle(DRIVE_PIN, drive_pos)

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        c.close()
        break
main()
