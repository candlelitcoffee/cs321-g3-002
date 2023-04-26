from flask import Flask, render_template,request,redirect,url_for
import Adafruit_BBIO.PWM as PWM

servoPin = "P9_14"
PWM.start(servoPin,3,50)

app = Flask(__name__)
title = "BeagleBoneBlackCar"
heading = "ToDo Reminder"

@app.route("/")
def tasks():
	return render_template('index.html')

@app.route("/forward")
def forward():
    servoPin = "P9_14"
    PWM.start(servoPin,3,50)
    starting = (0.055*(float(90)) + 3)
    PWM.set_duty_cycle(servoPin, starting)
    return redirect("/")
	
@app.route("/backwards")
@app.route("/backward")
def backward():
    servoPin = "P9_14"
    PWM.start(servoPin,3,50)
    starting = (0.055*(float(90)) + 3)
    PWM.set_duty_cycle(servoPin, starting)
    return redirect("/")

@app.route("/left")
def left():	
	servoPin = "P9_14"
	PWM.start(servoPin,3,50)
	dutyCycle=0.055*(float(170)) + 3
	PWM.set_duty_cycle(servoPin,dutyCycle)
	return redirect("/")
	
@app.route("/right")
def right():
	servoPin = "P9_14"
	PWM.start(servoPin,3,50)
	dutyCycle=0.055*(float(10)) + 3
	PWM.set_duty_cycle(servoPin,dutyCycle)
	return redirect("/")
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)