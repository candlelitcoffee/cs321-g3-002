import pygame
import socket

# Create socket object
s = socket.socket()

# Define the port 
port = 55334

# connect to the server on local computer
s.connect(('172.20.10.7', port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
data=''

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (252, 106, 106)
ORANGE = (237, 125, 45)
YELLOW = (255, 252, 71)
PINK = (255, 196, 209)
LIME = (197, 233, 155)
BLUE = (62, 190, 237)
DBLUE = (8, 27, 201)
GREY = (182, 184, 182)


# Define window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Define box size
BOX_SIZE = 100

# Define joystick dead zone
JOYSTICK_DEAD_ZONE = 0.1

# Create a Pygame window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the window title
pygame.display.set_caption("૮ ⚆ﻌ⚆ა  zoom zoom  ૮ ⚆ﻌ⚆ა")

# Initialize Xbox controller
joystick = None
for i in range(pygame.joystick.get_count()):
    if "Xbox" in pygame.joystick.Joystick(i).get_name():
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

# Define button names and box positions
button_names = ['A', 'B', 'X', 'Y', 'LB', 'RB', 'Up', 'Down', 'LT', 'RT']
box_positions = [(600, 600), (650, 500), (550, 500), (600, 400), (100, 660), (210, 660), (400, 550), (400, 660), (100, 250), (600, 250)]
button_boxes = {}

for i in range(len(button_names)):
    button_boxes[button_names[i]] = pygame.Rect(box_positions[i], (BOX_SIZE, BOX_SIZE))

def draw_buttons(screen, color, button):
    pygame.draw.rect(screen, color, button_boxes[button])
    font = pygame.font.SysFont('menlo', 24)
    text = font.render(button, True, WHITE)
    screen.blit(text, (button_boxes[button].x + BOX_SIZE/2 - text.get_width()/2, button_boxes[button].y + BOX_SIZE/2 - text.get_height()/2))

def draw_button_background():
    draw_buttons(screen, GREY, 'A')
    draw_buttons(screen, GREY, 'B')
    draw_buttons(screen, GREY, 'X')
    draw_buttons(screen, GREY, 'Y')
    draw_buttons(screen, GREY, 'LB')
    draw_buttons(screen, GREY, 'RB')
    draw_buttons(screen, GREY, 'Up')
    draw_buttons(screen, GREY, 'Down')
    draw_buttons(screen, GREY, 'LT')
    draw_buttons(screen, GREY, 'RT')
    pygame.draw.polygon(screen, GREY, ((200, 450), (200, 500), (300, 500), (300, 530), (350, 475), (300, 420), (300, 450)))
    pygame.draw.polygon(screen,GREY, ((180, 450), (180, 500), (80, 500), (80, 530), (30, 475), (80, 420), (80, 450)))

    pygame.display.update()


pygame.display.update()

# metrics display variables
throttle_percentage = 0 # stopped
throttle = 0 
#Go with Full Reverse = -100% ... 0 = stopped or no signal ... +100% = Full Forward.

# game loop ("main method sorta")-----------------------------
run = True
while run:

    # handle events
    for event in pygame.event.get():

        # chck for quit event
        if event.type == pygame.QUIT:
            run = False

    # clear the screen & draw button backgrounds
    screen.fill(WHITE)
    draw_button_background()


    # draw boxes for joystick and button input
    if joystick is not None:

        # get joystick axes values
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)

        #get trigger values (rt and lt)
        rt = joystick.get_axis(5)
        lt = joystick.get_axis(4)

        # check if joystick is in the dead zone
        if abs(x_axis) < JOYSTICK_DEAD_ZONE:
            print("in deadzone x_axis")
            x_axis = 0
        if abs(y_axis) < JOYSTICK_DEAD_ZONE:
            print("in deadzone y_axis")
            y_axis = 0

        # get button values
        a_button = joystick.get_button(0)
        b_button = joystick.get_button(1)
        x_button = joystick.get_button(2)
        y_button = joystick.get_button(3)
        lb_button = joystick.get_button(9)
        rb_button = joystick.get_button(10)
        dpad_down_button = joystick.get_button(12)
        dpad_up_button = joystick.get_button(11)

        # draw boxes and text
        if a_button:
            draw_buttons(screen, BLUE, 'A')
        if b_button:
           draw_buttons(screen, BLUE, 'B')
        if x_button: # sudden stop
            draw_buttons(screen, BLUE, 'X')
            print("x: brake/ sudden stop")
            s.send('x'.encode())
        if y_button: #center wheels
            draw_buttons(screen, BLUE, 'Y')
            print("c: center")
            s.send('c'.encode())
        if lb_button:
            draw_buttons(screen, BLUE, 'LB')
        if rb_button:
            draw_buttons(screen, BLUE, 'RB')
        if dpad_up_button:
            draw_buttons(screen, BLUE, 'Up')
        if dpad_down_button:
            draw_buttons(screen, BLUE, 'Down')
        if rt != -1.0 and rt != 0: # forward
            draw_buttons(screen, DBLUE, 'RT')
            print(f"rt: {rt}")
            print("w: foward")
            s.send('w'.encode())
        if lt != -1.0 and rt != 0: # backward
            draw_buttons(screen, DBLUE, 'LT')
            print(f"lt: {lt}")
            print("s: backward")
            s.send('s'.encode())
        if x_axis > 0:
            pygame.draw.polygon(screen,LIME, ((200, 450), (200, 500), (300, 500), (300, 530), (350, 475), (300, 420), (300, 450)))
            print("right")
            s.send('r'.encode())
        if x_axis < 0:
            pygame.draw.polygon(screen,RED, ((180, 450), (180, 500), (80, 500), (80, 530), (30, 475), (80, 420), (80, 450)))
            print("left")
            s.send('l'.encode())
    # update the screen
    pygame.display.update()

#sending quit signal to the socket
print("sending quit")
s.send('q'.encode())
# quit window
pygame.quit()

# close socket connection
s.close()
