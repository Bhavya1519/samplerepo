import RPi.GPIO as GPIO
import serial as ser
from flask import Flask, render_template
app = Flask(__name__)


while 1:
    if(ser.in_waiting > 0):
        line = ser.readline()
        print(line)

    @app.route("/")
    def index():
        # Read Sensors Status
        tempval = line[o]
        humval = line[1]
        mq3val = line[3]
        mq135val = line[4]
        mq9val = line[5]
        mq2val = line[6]
        mq4val = line[7]
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
