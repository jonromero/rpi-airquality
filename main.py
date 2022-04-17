from flask import Flask, render_template
import time
from sds011 import *

sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)

app = Flask(__name__)

@app.route("/")
def main():
    (pm25, pm10) = sensor.query()
    return render_template('index.html', p25=pm25, p10=pm10)



