import socket
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

        c.close()
        break
main()

