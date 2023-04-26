
import Adafruit_BBIO.PWM as PWM
class servo:

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
