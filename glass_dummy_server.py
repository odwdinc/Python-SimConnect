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



@app.route ('/')
def glass():
    return render_template("glassp.html")

@app.route('/ui')
def output_ui_variables():
    global latitude, longitude

    ui_friendly_dictionary = {}
    ui_friendly_dictionary["STATUS"] = "success"
    ui_friendly_dictionary["ALTITUDE"] = thousandify(random.randint(7995,8005))
    ui_friendly_dictionary["LATITUDE"] = latitude
    ui_friendly_dictionary["LONGITUDE"] = longitude
    ui_friendly_dictionary["AIRSPEED_INDICATE"] = random.randint(395,405)
    ui_friendly_dictionary["MAGNETIC_COMPASS"] = random.randint(89,91)
    ui_friendly_dictionary["VERTICAL_SPEED"] = random.randint(-5,5)
    ui_friendly_dictionary["FUEL_PERCENTAGE"] = random.randint(79,81)

    ui_friendly_dictionary["AUTOPILOT_HEADING_LOCK"] = random.randint(0,1)
    ui_friendly_dictionary["AUTOPILOT_HEADING_LOCK_DIR"] = random.randint(1,360)

    ui_friendly_dictionary["AUTOPILOT_ALTITUDE_LOCK"] = random.randint(0,1)
    ui_friendly_dictionary["AUTOPILOT_ALTITUDE_LOCK_VAR"] = thousandify(random.randint(5000,25000))

    ui_friendly_dictionary["AUTOPILOT_AIRSPEED_HOLD"] = random.randint(0,1)
    ui_friendly_dictionary["AUTOPILOT_AIRSPEED_HOLD_VAR"] = thousandify(random.randint(100,350))

    ui_friendly_dictionary["AUTOPILOT_PITCH_HOLD"] = random.randint(0,1)
    ui_friendly_dictionary["AUTOPILOT_PITCH_HOLD_REF"] = thousandify(random.randint(-25,25))

    if random.randint(0,1) == 1:
        ui_friendly_dictionary["GEAR_HANDLE_POSITION"] = "UP"
    else:
        ui_friendly_dictionary["GEAR_HANDLE_POSITION"] = "DOWN"

    longitude = longitude + 0.01

    return jsonify(ui_friendly_dictionary)


@app.route('/datapoint/<datapoint_name>/set', methods=["POST"])
def set_datapoint(datapoint_name):

    value_to_use = request.form.get('value_to_use')

    if value_to_use == None:
        print(datapoint_name + ": " + "No value passed")
    else:
        print(datapoint_name + ": " + value_to_use)

    status = "success"
    return jsonify(status)


app.run(host='0.0.0.0', port=5000, debug=True)