import pygame
from pygame.locals import *

def main():
    pygame.init()
    joystick = pygame.joystick.Joystick(0)  
    joystick.init()

    while True:
        for event in pygame.event.get():
            if event.type == JOYAXISMOTION:
                print("event number: " + str(event.axis))
                #if event.axis == 0 or event.axis == 4 or event.axis == 5:
                    #print("Joystick: " + str(joystick.get_axis(0)))
                    #print("Joystick: " + str(joystick.get_axis(4)))
                    #print("RT: " + str(joystick.get_axis(5)))
            if event.type == JOYBUTTONDOWN:
                print(event)
                print("event.button: " + str(event.button))        
            if event.type == JOYBUTTONUP:
                print(event)

if __name__ == "__main__":
    main()