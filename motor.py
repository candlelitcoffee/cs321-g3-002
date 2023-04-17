import Adafruit_BBIO.PWM as PWM
import time

DRIVE_PIN = "P9_16"

#set up PWM pins
PWM.start(DRIVE_PIN, 7.5, 50)

def changeRPM(dutyCycle):
    dutyCycle = float(dutyCycle)
    if 10.0 >= dutyCycle >= 5.0:
        PWM.set_duty_cycle(DRIVE_PIN, dutyCycle)

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
    #callibrating ESC
    calibrate()

    #setting to stop position so car doesn't fly to space
    changeRPM(7.5)

    print("Enter duty cycle value & increment by 0.5 (press enter to exit)")
    inp = input()
    while(inp != ''):
        changeRPM(inp)
        time.sleep(1)
        inp = input()

    #setting to stop position so car doesn't fly to space
    changeRPM(7.5)

if __name__ == "__main__":
    main()
