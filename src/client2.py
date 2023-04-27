# Import socket module
from __future__ import print_function
from inputs import get_gamepad	
import socket		
import pygame
from pygame.locals import *

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 55334			

# connect to the server on local computer
s.connect(('192.168.170.44', port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
data=''

pygame.init()
joystick = pygame.joystick.Joystick(0)  
joystick.init()

x_axis = 0
deadzone = 0.05
maxval = 1.0
prevAxisL = 0
prevAxisR = 0
prevAxis = 0

while True: 
    for event in pygame.event.get():
        if event.type == JOYAXISMOTION:
            if event.axis == 0:
                print("Joystick: " + str(joystick.get_axis(0)))
                print("current prevAxis: " + str(prevAxis))
                
                #dead zone checking
                #if(abs(joystick.get_axis(0)) > deadzone * maxval):
                if joystick.get_axis(0) > 0:#prevAxis:
                    #turn right
                    print("R")
                    s.send('r'.encode())
                    #prevAxis = joystick.get_axis(0)
                    print("new prevAxis: " + str(prevAxis))
                if joystick.get_axis(0) < 0:#prevAxis:
                    #turn left 
                    print("L")
                    s.send('l'.encode())  
                    #prevAxis = joystick.get_axis(0) 
                    print("current prevAxis: " + str(prevAxis))     
            if event.axis == 4:
                print("Left Trigger: " + str(joystick.get_axis(4)))
                if joystick.get_axis(4) > 0.2:
                    #move backward
                    print("S")
                    s.send('s'.encode())
            if event.axis == 5:
                print("Right Trigger: " + str(joystick.get_axis(5)))
                if joystick.get_axis(5) > 0.2:
                    #move forward
                    print("W")
                    s.send('w'.encode())
        if event.type == JOYBUTTONDOWN:
            print("Button Number: " + str(event.button))
            if event.button == 1: #Button B
                #gradually decrease speed
                print("B")
                s.send('b'.encode())
            if event.button == 3: #Button Y
                #Center wheels
                print("C")
                s.send('c'.encode())
            if event.button == 0: #Button A
                #Sudden stop
                print("brake")
                s.send('x'.encode())
# close the connection
s.close()	

'''
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
                '''

'''elif('BTN_TR' in event.code and event.state==1):
            print("W")
            s.send('w'.encode())        
        elif('BTN_TL' in event.code and event.state==1):
            print("S")
            s.send('s'.encode())'''