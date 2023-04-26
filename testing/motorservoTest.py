import Adafruit_BBIO.PWM as PWM
import time
servoPin="P9_14"

DRIVE_PIN = "P9_16"

#set up PWM pins
PWM.start(DRIVE_PIN, 7.5, 50)
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
            
def changeRPM(dutyCycle):
    dutyCycle = float(dutyCycle)
    if 10.0 >= dutyCycle >= 5.0:
        PWM.set_duty_cycle(DRIVE_PIN, dutyCycle)

def turnStraight():
    servoPin = "P9_14"
    PWM.start(servoPin,3,50)
    starting = (0.055*(float(90)) + 3)
    PWM.set_duty_cycle(servoPin, starting)

def turnLeft( angle: int):
    servoPin = "P9_14"
    dutyCycle=0.055*(float(angle)) + 3
    PWM.set_duty_cycle(servoPin,dutyCycle)

def turnRight(angle:int):
    servoPin = "P9_14"
    dutyCycle=0.055*(float(angle)) + 3
    PWM.set_duty_cycle(servoPin,dutyCycle)

def main():
    calibrate()
    print("I am running! input a speed\n")
    changeRPM(7.5)
    inp = input()
    while (inp != ''):
        if (input == '2'):
            break
            
        turnStraight()
        print("potato\n")
        time.sleep(2)
        turnLeft(45)
        print("potato2\n")
        time.sleep(2)
        print("turnright\n")
        turnRight(90)
        changeRPM(inp)
        time.sleep(2)
        print("input new speed\n")
        inp = input()
    
main()
