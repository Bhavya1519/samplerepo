import RPi.GPIO as GPIO
import serial as ser
from flask import Flask, render_template

ser_obj = ser.Serial("/dev/ttyACM0", 9600)
app = Flask(__name__)


def get_data():
	line = ""
	if(ser_obj.in_waiting > 0):
		line = ser_obj.readline()
		print(line)
		return line


@app.route("/")
def index():
    # Read Sensors Status
    tempval = get_data().split("=")[-1].strip()
    humval = get_data().split("=")[-1].strip()
    mq3val = get_data().split("=")[-1].strip()
    mq135val = get_data().split("=")[-1].strip()
    mq9val = get_data().split("=")[-1].strip()
    mq2val = get_data().split("=")[-1].strip()
    mq4val = get_data().split("=")[-1].strip()
    templateData = {
        'title': 'AIR QUALITY INDEX!',
        'tempt': tempval,
        'Hum': tempval,
        'MQ3': mq3val,
        'MQ135': mq135val,
        'MQ9': mq9val,
        'MQ2': mq2val,
        'MQ4': mq4val

    }
    return render_template('index2.html', **templateData)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
