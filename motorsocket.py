# first of all import the socket library
import socket
import time
import Adafruit_BBIO.PWM as PWM
DRIVE_PIN = "P9_16"
#starting position
PWM.start(DRIVE_PIN,7.5,50)

def drive(num):
    if 10.0 >= num >= 5.0:
        PWM.set_duty_cycle(DRIVE_PIN, num)

def calibrate():
    PWM.set_duty_cycle(DRIVE_PIN, 0.0)
    print("Make sure battery is connected but switch is OFF.  Press ENTER to continue")
    inp = input()
    if inp == '':
        PWM.set_duty_cycle(DRIVE_PIN, 10.0)
        print("Turn the switch ON now. You will hear two beeps then press Enter")
        inp = input()
        if inp == '':            
            PWM.set_duty_cycle(DRIVE_PIN, 5.0)
            print ("Working...")
            time.sleep(7)
            print ("Wait for it ....")
            time.sleep (5)
            print ("Almost there.....")
            PWM.set_duty_cycle(DRIVE_PIN, 0.0)
            time.sleep(2)
            print ("Arming ESC now...")
            PWM.set_duty_cycle(DRIVE_PIN, 5.0)
            time.sleep(1)
            print ("ESC is armed (You should have heard another beep).  You can now drive the car")
            PWM.set_duty_cycle(DRIVE_PIN, 7.5)
            print("I have finished running\n")

def main():

# next create a socket object
    s = socket.socket()
    print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
    port = 55555

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
    s.bind(('', port))
    print ("socket binded to %s" %(port))

# put the socket into listening mode
    s.listen(5)
    print ("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
    while True:

# Establish connection with client.
        c, addr = s.accept()
        print ('Got connection from', addr )

# send a thank you message to the client. encoding to send byte type.
        c.send('Thank you for connecting'.encode())
        print("here what I got: ")
        calibrate()
        buf = ''
        num =1
        while(num >= 0):
            buf = c.recv(1024)
            strings = buf.decode('utf8')
            print("the data is "+strings)
            num = int(strings)
            print(num)
            drive(num)
        c.close()
        break
main()
