import turtle
from controller_pytest import XboxController

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 50
speed = 10
speed_less = 5

# Initialize Turtle screen
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.title("Turtle Go BRRRR")
turtle.bgcolor("white")

# Initialize Xbox controller
joy = XboxController()

# Create a Turtle square
square = turtle.Turtle()
square.shape("square")
square.color("black")
square.shapesize(SQUARE_SIZE / 20) # Divide by 20 to convert from pixels to Turtle units

# Move the square based on Xbox controller input
def move_square():
    x, y, a, b, rb = joy.read()

    square.setx(square.xcor() + x * 10) # Scale the joystick input by 10 to adjust movement speed
    square.sety(square.ycor() + y * 10) # Invert y-axis since Turtle has y-axis pointing upwards
    turtle.ontimer(move_square, 5) # Call the function every 10 milliseconds

    if (a == 1) :
        turtle.bgcolor("red")
        
    elif (b == 1) :
        turtle.bgcolor("white")


# Start moving the square
move_square()

# Start the Turtle event loop
turtle.mainloop()

