import Adafruit_BBIO.PWM as PWM
import time
servoPin="P9_14"
PWM.start(servoPin,3,50)
#setting steering angle to 90 for straight wheels at start
starting = (0.055*(float(90)) + 3)
PWM.set_duty_cycle(servoPin, starting)

starting_angle = 90
while True: #turning right
    if(float(starting_angle) > 0):
        starting_angle -= 0.05
        dutyCycle=0.055*(float(starting_angle)) + 3
        PWM.set_duty_cycle(servoPin,dutyCycle)
    else:
        break
print(starting_angle)
time.sleep(2)
#start steering at middle
starting = (0.055*(float(90)) + 3)
PWM.set_duty_cycle(servoPin, starting)
starting_angle = 90
time.sleep(2)

while True: #turning left
    if(float(starting_angle) < 180):
        starting_angle += 0.05
        dutyCycle=0.055*(float(starting_angle)) + 3
        PWM.set_duty_cycle(servoPin,dutyCycle)
    else:
        break

print(starting_angle)