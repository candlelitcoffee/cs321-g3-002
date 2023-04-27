# first of all import the socket library
import socket
import time
import Adafruit_BBIO.PWM as PWM
DRIVE_PIN = "P9_16"
SERVO_PIN = "P9_14"

#starting position
PWM.start(DRIVE_PIN,7.5,50)
PWM.start(SERVO_PIN,3,50)
starting = (0.055*(float(90)) + 3)
PWM.set_duty_cycle(SERVO_PIN,starting)


#____________________________

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

# reserve a port on your computer 
    port = 55334

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
        print("calibrate 5")
        #time.sleep(5)
        #calibrate()
        #calibrate('')
        direction = 'i'
        servo_pos = 90
        drive_pos = 7.5
        servo_cycle = 0.0
        while(direction != 'q'):
            direction = c.recv(1024).decode()
            print("the buf is "+direction)
            #drive(num)
            
            if(direction == 'l'): #left
                if(servo_pos < 180):
                    print("i am turning left")
                    servo_pos += 2
                    servo_cycle = (0.055*(float(servo_pos)) + 2)
                    PWM.set_duty_cycle(SERVO_PIN, servo_cycle)
                    print("the servo pos and cycle "+ str(servo_pos) + " " + str(servo_cycle))
            elif(direction == 'r'): #right
                if(servo_pos > 0):
                    print("I am turning right")
                    servo_pos -= 2
                    servo_cycle = (0.055*(float(servo_pos)) + 2)
                    PWM.set_duty_cycle(SERVO_PIN, servo_cycle)
                    print("the servo pos and cycle "+ str(servo_pos) + " " + str(servo_cycle))
            elif(direction == 'c'): #center the wheels
                starting = (0.055*(float(90)) + 3)
                PWM.set_duty_cycle(SERVO_PIN,starting)
            elif(direction == 'w'): #forward
                print("I am going forward")
                drive_pos += 0.05
                if 10.0 >= drive_pos >= 5.0:
                    PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
            elif(direction == 's'): #backward
                print("I am going backward")
                drive_pos -= 0.05
                if 10.0 >= drive_pos >= 5.0:
                    PWM.set_duty_cycle(DRIVE_PIN, drive_pos)

        c.close()
        break
main()
