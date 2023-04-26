"""Simple example showing how to get gamepad events."""
from __future__ import print_function
from inputs import get_gamepad
import Adafruit_BBIO.PWM as PWM
servoPin = "P9_14"

def main():
    """Just print out some event infomation when the gamepad is used."""
    angle = (0.055*(float(90)) + 3)
    PWM.set_duty_cycle(servoPin, angle)
    PWM.start(servoPin,3,50)
    while 1:
        events = get_gamepad()
        for event in events:
            if('ABS_X' in event.code):
                print(event.ev_type, event.code, event.state)
                #turn right
                if(event.state > 0 and float(angle)>0):
                    angle -= 0.05
                    dutyCycle=0.055*(float(angle)) + 3
                    PWM.set_duty_cycle(servoPin,dutyCycle)
                #turn  left
                if(event.state < 0 and float(angle) < 180):
                    angle += 0.05
                    dutyCycle=0.055*(float(angle)) + 3
                    PWM.set_duty_cycle(servoPin,dutyCycle)


if __name__ == "__main__":
    main()
