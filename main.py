import RPi.GPIO as GPIO
import serial as serial
from flask import Flask, render_template, jsonify

ser_obj = serial.Serial("/dev/ttyACM0", 9600)
app = Flask(__name__)

def get_data():
    line = b""
    if(ser_obj.inWaiting() > 0):
        line = ser_obj.readline()
    return line.decode("utf-8")


@app.route("/api/v1/get_data")
def api_get_data():
    # Read Sensors Status
    tempval = get_data().split("=")[-1].strip()
    humval = get_data().split("=")[-1].strip()
    mq3val = get_data().split("=")[-1].strip()
    mq135val = get_data().split("=")[-1].strip()
    mq9val = get_data().split("=")[-1].strip()
    mq2val = get_data().split("=")[-1].strip()
    mq4val = get_data().split("=")[-1].strip()
    get_data()
    templateData = {
        'title': 'AIR QUALITY INDEX!',
        'tempt': tempval,
        'Hum': humval,
        'MQ3': mq3val,
        'MQ135': mq135val,
        'MQ9': mq9val,
        'MQ2': mq2val,
        'MQ4': mq4val
    }
    return jsonify(templateData)

@app.route("/")
def home():
	return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
