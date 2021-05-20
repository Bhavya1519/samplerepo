import RPi.GPIO as GPIO
from flask import Flask, render_template
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = 20
senPIR = 16
buttonSts = GPIO.LOW
senPIRSts = GPIO.LOW
   
# Set button and PIR sensor pins as an input
GPIO.setup(button, GPIO.IN)   
GPIO.setup(senPIR, GPIO.IN)
	
@app.route("/")
def index():
	# Read Sensors Status
	buttonSts = 32
	senPIRSts = 59
	mq3val =  120
	mq135val = 548
	mq9val = 700
	mq2val =200
	mq4val =90
	templateData = {
	'title' : 'AIR QUALITY INDEX!',
	'button'  : buttonSts,
	'senPIR'  : senPIRSts,
	'MQ3'     : mq3val,
	'MQ135'   : mq135val,
	'MQ9'     : mq9val,
	'MQ2'     : mq2val,
	'MQ4'     : mq4val
        
      }
	return render_template('index2.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
