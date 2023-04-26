# call socket over and over. (damien bot)
#from flask import Flask, render_template
#what is thread needed for
#from threading import Thread
#import inputs
#app = Flask('')
#@app.route('/')
#def main():
#html = render_template('index.html')
#return html, "Your Bot Is Ready"
#def run():
#app.run()
#(host="0.0.0.0", port=8000)
#def keep_alive():
#server = Thread(target=run)
#server.start()

from flask import Flask, render_template,request,redirect,url_for
import Adafruit_BBIO.PWM as PWM

#what is this
#PWM.start(servoPin,3,50)

app = Flask(__name__)
title = "BeagleBoneBlackCar"
heading = "ToDo Reminder"
servoPin = "P9_16"

@app.route("/")
def tasks():
	return render_template('index.html')

@app.route("/forward")
def forward():
    PWM.start(servoPin,3,50)
    starting = (0.055*(float(90)) + 3)
    PWM.set_duty_cycle(servoPin, starting)
    return redirect("/")
  
@app.route("/backward")
def backward():
    PWM.start(servoPin,3,50)
    starting = (0.055*(float(90)) + 3)
    PWM.set_duty_cycle(servoPin, starting)
    return redirect("/")

@app.route("/left")
def left():	
	PWM.start(servoPin,3,50)
	dutyCycle=0.055*(float(170)) + 3
	PWM.set_duty_cycle(servoPin,dutyCycle)
	return redirect("/")
	
@app.route("/right")
def right():
	PWM.start(servoPin,3,50)
	dutyCycle=0.055*(float(10)) + 3
	PWM.set_duty_cycle(servoPin,dutyCycle)
	return redirect("/")
	
if __name__ == "__main__":
  app.run()
