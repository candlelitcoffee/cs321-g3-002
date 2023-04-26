from servo import servo
import Adafruit_BBIO.PWM as PWM
import pytest

def test_turnStraight():
    car = servo()
    assert car.turnStraight() == (0.055*(float(90)) + 3)

def test_start_pwm():
    PWM.cleanup()
    duty = 3
    PWM.start("P9_14",duty,50)
    assert int(duty) == 3
    PWM.cleanup()

def test_turnRight():
    car = servo()
    assert car.turnRight(45) == 0.055*(float(45)) + 3

def test_turnLeft():
    car = servo()
    assert car.turnLeft(130) == 0.055*(float(45)) + 3

def test_invalid_duty_cycle_negative():
    PWM.cleanup()
    with pytest.raises(ValueError):
        PWM.start("P9_14", -1)

def test_stop_pwm():
    PWM.stop("P9_14")
    pass
