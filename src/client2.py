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
prevAxisL = 0
prevAxisR = 0

while 1:
    events = get_gamepad()
    for event in events:
        if('ABS_X' in event.code):  
            print("event.state LJS: " + str(event.state))
            if abs(event.state) > deadzone * maxval:      
                #turn right 
                if(event.state > prevAxisL):
                    print("R")
                    s.send('r'.encode())        
                #turn  left
                elif(event.state < prevAxisL):
                    print("L")
                    s.send('l'.encode())
                #storing previous axis number 
                prevAxisL = event.state
        if('ABS_RY' in event.code):
            print("event.state: RJS" + str(event.state))
            if abs(event.state) > deadzone * maxval:      
                #turn right 
                if(event.state > prevAxisR):
                    print("W")
                    s.send('w'.encode())        
                #turn  left
                elif(event.state < prevAxisR):
                    print("S")
                    s.send('s'.encode())
                #storing previous axis number 
                prevAxisR = event.state
# close the connection
s.close()	


'''elif('BTN_TR' in event.code and event.state==1):
            print("W")
            s.send('w'.encode())        
        elif('BTN_TL' in event.code and event.state==1):
            print("S")
            s.send('s'.encode())'''