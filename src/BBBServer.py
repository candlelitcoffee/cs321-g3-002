# first of all import the socket library
import socket
import time
import Adafruit_BBIO.PWM as PWM
import subprocess

DRIVE_PIN = "P9_16"
SERVO_PIN = "P9_14"

#ffmpeg video stream flags
ffmpegCmd = ["ffmpeg", "-c:v", "mjpeg", "-s", "640x360", "-i", "/dev/video0",
             "-nostdin", "-loglevel", "panic", "-c:v", "copy", "-tune", "zerolatency",
             "-muxdelay", "0.1", "-g", "0", "-f", "mjpeg", "INDEX 20: LINK GOES HERE"]

#starting position
PWM.start(DRIVE_PIN,7.5,50)
PWM.start(SERVO_PIN,3,50)
starting = (0.055*(float(90)) + 3)
PWM.set_duty_cycle(SERVO_PIN,starting)


#____________________________

def get_ip(): 
    # From StackOverflow - https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('8.8.8.8', 80))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


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
   
    global ffmpegCmd
    IP = get_ip()
    port = 55334
    udp_link = ""

    print("Your BeagleBone's IP is: " + IP + "\n")

    laptopID = "Zephyrus-G14"
    laptopIP = socket.gethostbyname(laptopID)
    print("This is laptop's IP: " + laptopIP)
    BeagleBone_IP = f"!{IP}".encode()
    print("BB_IP after formatting: " + str(BeagleBone_IP))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, port))  # Receive the UDP link from server.
    sock.sendto(BeagleBone_IP, (laptopIP, port))  # Send BB IP to server.

    
    #getting udp link
    udp_link = ""
    while True:  # Program will block here until we send a link to stream to. Use reconnect in mainL, press start.
        message = sock.recv(30)
        decoded = message.decode()
        if decoded.startswith("L"):  # This happens when we send controller data when reconnecting, just ignore it.
            continue
        if decoded.startswith("u"):  # This means we received a UDP link to stream to.
            udp_link = decoded
            sock.sendto(b"Received", (laptopIP, port))  # Confirm to ControlTower that we received a video link.
            break
        elif decoded.startswith("N"):
            sock.sendto(b"Received", (laptopIP, port))
            udp_link = "No video link supplied. Will not be streaming."
            break

    if not udp_link.startswith("N"):  # This means that we have an actual UDP link to stream to. Run ffmpeg command.
        ffmpegCmd[20] = udp_link  # Put UDP link into ffmpegCmd list.
        p = subprocess.Popen(ffmpegCmd)  # Run ffmpeg as a background task, no logs. Will not block.
        print(f"Ffmpeg command ran, streaming to {ffmpegCmd[20]}")
    


    #direction = 'i'
    servo_pos = 90.0
    drive_pos = 7.5
    servo_cycle = 0.0

    # a forever loop until we interrupt it or
    # an error occurs
    while True:

        message = sock.recv(30)
        decode = message.decode()

        print("Decoded message: " + decode)

        #if message contains buttons
        if len(decode) <= 2:
            if decode is "B":
                if drive_pos != 7.5:
                    if drive_pos > 7.5:
                        while drive_pos > 7.5:
                            drive_pos -= 0.1
                            PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
                            print("motor halting duty cycle: " + str(drive_pos))
                            time.sleep(0.1)
                        drive_pos = 7.5
                        PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
                    elif drive_pos < 7.5:
                        while drive_pos < 7.5:
                            drive_pos += 0.1
                            PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
                            print("motor halting duty cycle: " + str(drive_pos))
                            time.sleep(0.1)
                        drive_pos = 7.5
                        PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
            elif decode is "C":
                starting = (0.055*(float(90)) + 3)
                PWM.set_duty_cycle(SERVO_PIN,starting)
            elif decode is "X":
                drive_pos = 7.5
                PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
        else:    
            servo_pos = float(decode[2:decode.find("L")])
            lt = float(decode[decode.find("L")+1:decode.find("R")]) # 7.5 to 5 for accelerate
            rt = float(decode[decode.find("R")+1:]) # 7.5 to 8.5 for reverse

        #Servo changes
        servo_cycle = (0.055*(float(servo_pos)) + 3)
        PWM.set_duty_cycle(SERVO_PIN, servo_cycle)
        print("the servo pos and cycle "+ str(servo_pos) + " " + str(servo_cycle))

        
        if lt != 0.0 and rt == 0.0:  # Reversing only allowed if right trigger is off and left trigger is not off.
            print("I am going backward")
            if 7.7 > drive_pos:     #might wanna include 7.7 too here
                drive_pos += lt
                PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
                print("motor forward duty cycle: " + str(drive_pos))
        else:
            print("I am going forward")
            if 5.0 < drive_pos:     #might wanna include 5.0 too here
                drive_pos -= rt
                PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
                print("motor backward duty cycle: " + str(drive_pos))


        #time.sleep(5)
        #calibrate()
        #calibrate('')
        
        #c.close()
        


if __name__ == "__main__":
    main()




'''    # next create a socket object
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
    '''


'''# Establish connection with client.
        c, addr = s.accept()
        print ('Got connection from', addr )

        # send a thank you message to the client. encoding to send byte type.
        c.send('Thank you for connecting'.encode())
        print("calibrate 5")
        '''


'''direction = c.recv(1024).decode()
            print("the buf is "+direction)
            #drive(num)
            
            if(direction == 'l'): #left
                if(servo_pos < 180):
                    print("i am turning left")
                    servo_pos += 35
                    servo_cycle = (0.055*(float(servo_pos)) + 3)
                    PWM.set_duty_cycle(SERVO_PIN, servo_cycle)
                    print("the servo pos and cycle "+ str(servo_pos) + " " + str(servo_cycle))
            elif(direction == 'r'): #right
                if(servo_pos > 0):
                    print("I am turning right")
                    servo_pos -= 35
                    servo_cycle = (0.055*(float(servo_pos)) + 3)
                    PWM.set_duty_cycle(SERVO_PIN, servo_cycle)
                    print("the servo pos and cycle "+ str(servo_pos) + " " + str(servo_cycle))
            elif(direction == 's'): #backward
                print("I am going backward")
                if 7.7 >= drive_pos >= 5.0:
                    drive_pos += 0.05
                    PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
                    print("motor forward duty cycle: " + str(drive_pos))
            elif(direction == 'w'): #forward
                print("I am going forward")
                if 10.0 >= drive_pos >= 6.0:
                    drive_pos -= 0.05
                    PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
                    print("motor backward duty cycle: " + str(drive_pos))
                    '''


'''while(direction != 'q'):
            
            elif(direction == 'b'): #halt car gradually
                if drive_pos != 7.5:
                    if drive_pos > 7.5:
                        while drive_pos > 7.5:
                            drive_pos -= 0.1
                            PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
                            print("motor halting duty cycle: " + str(drive_pos))
                            time.sleep(0.1)
                        drive_pos = 7.5
                        PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
                    elif drive_pos < 7.5:
                        while drive_pos < 7.5:
                            drive_pos += 0.1
                            PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
                            print("motor halting duty cycle: " + str(drive_pos))
                            time.sleep(0.1)
                        drive_pos = 7.5
                        PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
            elif(direction == 'c'): #center wheels
                starting = (0.055*(float(90)) + 3)
                PWM.set_duty_cycle(SERVO_PIN,starting)
            elif(direction == 'x'): #Sudden brake
                drive_pos = 7.5
                PWM.set_duty_cycle(DRIVE_PIN, drive_pos)
                '''