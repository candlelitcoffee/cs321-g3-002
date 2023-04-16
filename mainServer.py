# first of all import the socket library
import socket
import Adafruit_BBIO.PWM as PWM

def turn(num):
    servoPin = "P9_14"
    PWM.start(servoPin,3,50)
    starting = (0.055*(float(num)) + 3)
    PWM.set_duty_cycle(servoPin, starting)
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
        buf = ''
        num =1
        while(num >= 0):
            buf = c.recv(1024)
            strings = buf.decode('utf8')
            print("the data is "+strings)
            num = int(strings)
            print(num)
            turn(num)
        c.close()
        break
main()