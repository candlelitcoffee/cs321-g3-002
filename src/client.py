# Import socket module
from __future__ import print_function
#from inputs import get_gamepad	
import socket		
import pygame
from pygame.locals import *
import racer


laptopID = "Zephyrus-G14"
BeagleBone_IP = "None"
video_feed_test = "None"

def main():

    global BeagleBone_IP

    # Define the port on which you want to connect
    port = 55334

    #RM connections, DO NOT CHANGE ANYTHING
    RMName = "localhost" #Should be G17
    RaceManagement = racer.RaceConnection(RMName)  # Establish connection to Race Management
    RaceManagement.start()  # Will prompt for name, number, and send an integer indicating what stream to record to.

    #Connecting to BBB
    fromBB = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    fromBB.bind((socket.gethostbyname(laptopID), port))
    toBB = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("outside of while")
    #Sending UDP video link to BBB.
    while True:
        print("inside of while")
        data = fromBB.recv(30)
        decoded = data.decode()
        print("message: " + decoded)
        if decoded.startswith("!"):
            BeagleBone_IP = decoded[1:]  # Now BeagleBone_IP has been loaded with BeagleBone's IP.
            print(f"Got BeagleBone_IP: {BeagleBone_IP}")
            bytes_udp = RaceManagement.sendFeed.encode()
            fromBB.sendto(bytes_udp, (BeagleBone_IP, port))  # Send UDP video link to BeagleBone.
        elif decoded.startswith("R"):
            break  # UDP Address received by the BBB.
    
    
    #Car controls loop
    
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
                if event.axis == 0 or event.axis == 4 or event.axis == 5:
                    print("Joystick: " + str(joystick.get_axis(0)))
                    #print("current prevAxis: " + str(prevAxis))
                    joy_stick = joystick.get_axis(0) * 10 + 105
                    rounded_stick = round(joy_stick, 4)
                    string_Stick = "{:04f}".format(rounded_stick)
                    print("string_Stick: " + string_Stick)

                    print("Left Trigger: " + str(joystick.get_axis(4)))
                    left_trigger = joystick.get_axis(4) + 1    # setting values to 0-2, once joystick values reach 0 increase motor speed by only 0.2
                    string_left_trigger = "{:03f}".format(left_trigger)
                    print("string_left_trigger: " + string_left_trigger)
                    RaceManagement.send_throttle(round(left_trigger * -50)) 
                
                    print("Right Trigger: " + str(joystick.get_axis(5)))
                    right_trigger = joystick.get_axis(5) + 1    # setting values to 0-2, once joystick values reach 0 increase motor speed by only 0.2
                    string_right_trigger = "{:03f}".format(right_trigger)
                    print("string_right_trigger: " + string_right_trigger)
                    RaceManagement.send_throttle(round(right_trigger * 50)) 

                    s = f"S{string_Stick}L{string_left_trigger}R{string_right_trigger}"  
                    bytes_s = s.encode()
                    toBB.sendto(bytes_s, (BeagleBone_IP, port))

            if event.type == JOYBUTTONDOWN:
                print("Button Number: " + str(event.button))
                if event.button == 1: #Button B
                    #gradually decrease speed
                    print("B")
                    tempButton = "B" 
                    bytes_s = tempButton.encode()
                    toBB.sendto(bytes_s, (BeagleBone_IP, port))
                    RaceManagement.send_throttle(0) 
                if event.button == 3: #Button Y
                    #Center wheels
                    print("C")
                    tempButton = "C" 
                    bytes_s = tempButton.encode()
                    toBB.sendto(bytes_s, (BeagleBone_IP, port))
                if event.button == 0: #Button A
                    #Sudden stop
                    print("brake")
                    tempButton = "X" 
                    bytes_s = tempButton.encode()
                    toBB.sendto(bytes_s, (BeagleBone_IP, port))
                    RaceManagement.send_throttle(0) 
                    
    # close the connection
    #toBB.close()	


if __name__ == "__main__":
    main()

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



''' # Create a socket object
    s = socket.socket()		
			
    # connect to the server on local computer
    s.connect(('192.168.170.44', port))

    # receive data from the server and decoding to get the string.
    print (s.recv(1024).decode())
    data=''
    '''


'''#dead zone checking
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
                        '''


'''if joystick.get_axis(4) > 0.2:
                        #move backward
                        print("S")
                        RaceManagement.send_throttle(joystick.get_axis(4)) #temp command
                        s.send('s'.encode())
                        '''


'''if joystick.get_axis(5) > 0.2:
                        #move forward
                        print("W")
                        RaceManagement.send_throttle(joystick.get_axis(5)) #temp command
                        s.send('w'.encode())
                        '''