#
# This is a dummy server which does not connect to MSFS2020
# It just serves up random data which allows testing of the front end without MSFS2020 running
# If you want to connect to MSFS2020 then you are looking for glass_server.py


from flask import Flask, jsonify, render_template, request
from time import sleep
import random

app = Flask(__name__)

latitude = 47.606209
longitude = -122.332069

def thousandify(x):
    return f"{x:,}"


@app.route('/ajaxtest')
def ajax_test():
    return render_template("ajaxtest3.html")


@app.route ('/glass')
def glass():
    return render_template("glass.html")

@app.route('/ui')
def output_ui_variables():
    global latitude, longitude

    ui_friendly_dictionary = {}
    ui_friendly_dictionary["STATUS"] = "success"
    ui_friendly_dictionary["ALTITUDE"] = thousandify(random.randint(5000,35000))
    ui_friendly_dictionary["LATITUDE"] = latitude
    ui_friendly_dictionary["LONGITUDE"] = longitude
    ui_friendly_dictionary["AIRSPEED_INDICATE"] = random.randint(50,400)
    ui_friendly_dictionary["MAGNETIC_COMPASS"] = random.randint(1,360)
    ui_friendly_dictionary["VERTICAL_SPEED"] = random.randint(-2000,2000)
    ui_friendly_dictionary["FUEL_PERCENTAGE"] = random.randint(0,100)

    longitude = longitude + 0.01

    return jsonify(ui_friendly_dictionary)


app.run(host='0.0.0.0', port=5000, debug=True)