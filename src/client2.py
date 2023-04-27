# Import socket module
from __future__ import print_function
from inputs import get_gamepad	
import socket		

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 55334			

# connect to the server on local computer
s.connect(('192.168.7.2', port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
data=''

x_axis = 0
deadzone = 0.2
maxval = 32768
prevAxis = 0

while 1:
    events = get_gamepad()
    for event in events:
        if('ABS_X' in event.code):  
            print("event.state: " + str(event.state))
            if abs(event.state) > deadzone * maxval:      
                #turn right 
                if(event.state > prevAxis):
                    print("R")
                    s.send('r'.encode())        
                #turn  left
                elif(event.state < prevAxis):
                    print("L")
                    s.send('l'.encode())

                #storing previous axis number 
                axisNum = event.state
            elif (event.state < (deadzone * maxval)) and (event.state > -(deadzone * maxval)):
                #turn straight
                print("Steering center")
                s.send('c'.encode())
        if('BTN_TR' in event.code and event.state==1):
            print("W")
            s.send('w'.encode())
                
        if('BTN_TL' in event.code and event.state==1):
            print("S")
            s.send('s'.encode())
# close the connection
s.close()	
