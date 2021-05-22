import RPi.GPIO as GPIO
import serial as serial
from flask import Flask, render_template, jsonify, send_from_directory, send_file
from flask_cors import CORS
from datetime import datetime

ser_obj = serial.Serial("/dev/ttyACM0", 9600)
app = Flask(__name__)
CORS(app)


def get_data():
    line = b""
    if(ser_obj.inWaiting() > 0):
        line = ser_obj.readline()
    return line.decode("utf-8")

@app.route("/get_data")
def get_file_data():
    return send_file("/static/data.csv", as_attachment=True)

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
    now = datetime.now().strftime('%m/%d/%Y-%H:%M:%S')
    with open("static/data.csv", "a") as f:
        f.write("{},{},{},{},{},{},{},{}\n"
        .format(now, templateData['tempt'], templateData['Hum'], templateData['MQ3'], templateData['MQ135'], templateData['MQ9'], templateData['MQ2'], templateData['MQ4']))
    return jsonify(templateData)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
