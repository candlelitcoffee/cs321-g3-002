"""Simple example showing how to get gamepad events."""
from __future__ import print_function

from inputs import get_gamepad
def main():
    """Just print out some event infomation when the gamepad is used."""
 
    while 1:
        events = get_gamepad()
        for event in events:
            if('ABS_X' in event.code):
                
                #turn right
                if(event.state > 0):
                    print("R")
                    
                #turn  left
                if(event.state < 0):
                    print("L")
            if('BTN_SOUTH' in event.code and event.state==1):
                print("W")
                
            if('BTN_EAST' in event.code and event.state==1):
                print("S")


if __name__ == "__main__":
    main()
