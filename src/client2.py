# Import socket module
from __future__ import print_function
from inputs import get_gamepad	
import socket		

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 55554
			

# connect to the server on local computer
s.connect(('192.168.7.2', port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
data=''
while 1:
    events = get_gamepad()
    for event in events:
        if('ABS_X' in event.code):        
            #turn right
            if(event.state > 0):
                print("R")
                s.send('c'.encode())        
            #turn  left
            if(event.state < 0):
                print("L")
                s.send('a'.encode())
        if('BTN_SOUTH' in event.code and event.state==1):
            print("W")
            s.send('w'.encode())
                
        if('BTN_EAST' in event.code and event.state==1):
            print("S")
            s.send('s'.encode())
# close the connection
s.close()	
	

