from flask import Flask, jsonify, render_template, request
from SimConnect import *
from time import sleep
import random
import asyncio

app = Flask(__name__)

# SIMCONNECTION RELATED STARTUPS

# Create simconnection
sm = SimConnect()
ae = AircraftEvents(sm)
aq = AircraftRequests(sm)

# Create request holders

# Note: I have commented out request_ui as I don't think it makes sense to replicate the ui interface through JSON given the /ui endpoint returns a duplicate of this anyway
# I have not deleted it yet as it's handy to have this list of helpful variables here
#
#request_ui = [
#	'PLANE_ALTITUDE',
#	'PLANE_LATITUDE',
#	'PLANE_LONGITUDE',
#	'AIRSPEED_INDICATED',
#	'MAGNETIC_COMPASS',  # Compass reading
#	'VERTICAL_SPEED',  # Vertical speed indication
#	'FLAPS_HANDLE_PERCENT',  # Percent flap handle extended
#	'FUEL_TOTAL_QUANTITY',  # Current quantity in volume
#	'FUEL_TOTAL_CAPACITY',  # Total capacity of the aircraft
#	'GEAR_HANDLE_POSITION',  # True if gear handle is applied
#	'AUTOPILOT_MASTER',
#	'AUTOPILOT_NAV_SELECTED',
#	'AUTOPILOT_WING_LEVELER',
#	'AUTOPILOT_HEADING_LOCK',
#	'AUTOPILOT_HEADING_LOCK_DIR',
#	'AUTOPILOT_ALTITUDE_LOCK',
#	'AUTOPILOT_ALTITUDE_LOCK_VAR',
#	'AUTOPILOT_ATTITUDE_HOLD',
#	'AUTOPILOT_GLIDESLOPE_HOLD',
#	'AUTOPILOT_PITCH_HOLD_REF',
#	'AUTOPILOT_APPROACH_HOLD',
#	'AUTOPILOT_BACKCOURSE_HOLD',
#	'AUTOPILOT_VERTICAL_HOLD',
#	'AUTOPILOT_VERTICAL_HOLD_VAR',
#	'AUTOPILOT_PITCH_HOLD',
#	'AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE',
#	'AUTOPILOT_AIRSPEED_HOLD',
#	'AUTOPILOT_AIRSPEED_HOLD_VAR'
#]

request_location = [
	'PLANE_ALTITUDE',
	'PLANE_LATITUDE',
	'PLANE_LONGITUDE',
	'KOHLSMAN_SETTING_HG',
]

request_airspeed = [
	'AIRSPEED_TRUE',
	'AIRSPEED_INDICATE',
	'AIRSPEED_TRUE CALIBRATE',
	'AIRSPEED_BARBER POLE',
	'AIRSPEED_MACH',
]

request_compass = [
	'WISKEY_COMPASS_INDICATION_DEGREES',
	'PARTIAL_PANEL_COMPASS',
	'ADF_CARD',  # ADF compass rose setting
	'MAGNETIC_COMPASS',  # Compass reading
	'INDUCTOR_COMPASS_PERCENT_DEVIATION',  # Inductor compass deviation reading
	'INDUCTOR_COMPASS_HEADING_REF',  # Inductor compass heading
]

request_vertical_speed = [
	'VELOCITY_BODY_Y',  # True vertical speed, relative to aircraft axis
	'RELATIVE_WIND_VELOCITY_BODY_Y',  # Vertical speed relative to wind
	'VERTICAL_SPEED',  # Vertical speed indication
	'GPS_WP_VERTICAL_SPEED',  # Vertical speed to waypoint
]

request_fuel = [
	'FUEL_TANK_CENTER_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_CENTER2_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_CENTER3_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_LEFT_MAIN_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_LEFT_AUX_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_LEFT_TIP_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_RIGHT_MAIN_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_RIGHT_AUX_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_RIGHT_TIP_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_EXTERNAL1_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_EXTERNAL2_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_CENTER_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_CENTER2_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_CENTER3_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_LEFT_MAIN_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_LEFT_AUX_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_LEFT_TIP_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_RIGHT_MAIN_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_RIGHT_AUX_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_RIGHT_TIP_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_EXTERNAL1_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_EXTERNAL2_CAPACITY',  # Maximum capacity in volume
	'FUEL_LEFT_CAPACITY',  # Maximum capacity in volume
	'FUEL_RIGHT_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_CENTER_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_CENTER2_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_CENTER3_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_LEFT_MAIN_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_LEFT_AUX_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_LEFT_TIP_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_RIGHT_MAIN_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_RIGHT_AUX_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_RIGHT_TIP_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_EXTERNAL1_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_EXTERNAL2_QUANTITY',  # Current quantity in volume
	'FUEL_LEFT_QUANTITY',  # Current quantity in volume
	'FUEL_RIGHT_QUANTITY',  # Current quantity in volume
	'FUEL_TOTAL_QUANTITY',  # Current quantity in volume
	'FUEL_WEIGHT_PER_GALLON',  # Fuel weight per gallon
	'FUEL_TOTAL_CAPACITY',  # Total capacity of the aircraft
	'FUEL_SELECTED_QUANTITY_PERCENT',  # Percent or capacity for selected tank
	'FUEL_SELECTED_QUANTITY',  # Quantity of selected tank
	'FUEL_TOTAL_QUANTITY_WEIGHT',  # Current total fuel weight of the aircraft
	'NUM_FUEL_SELECTORS',  # Number of selectors on the aircraft
	'UNLIMITED_FUEL',  # Unlimited fuel flag
	'ESTIMATED_FUEL_FLOW',  # Estimated fuel flow at cruise
]

request_flaps = [
	'FLAPS_HANDLE_PERCENT',  # Percent flap handle extended
	'FLAPS_HANDLE_INDEX',  # Index of current flap position
	'FLAPS_NUM_HANDLE_POSITIONS',  # Number of flap positions
	'TRAILING_EDGE_FLAPS_LEFT_PERCENT',  # Percent left trailing edge flap extended
	'TRAILING_EDGE_FLAPS_RIGHT_PERCENT',  # Percent right trailing edge flap extended
	'TRAILING_EDGE_FLAPS_LEFT_ANGLE',  # Angle left trailing edge flap extended. Use TRAILING EDGE FLAPS LEFT PERCENT to set a value.
	'TRAILING_EDGE_FLAPS_RIGHT_ANGLE',  # Angle right trailing edge flap extended. Use TRAILING EDGE FLAPS RIGHT PERCENT to set a value.
	'LEADING_EDGE_FLAPS_LEFT_PERCENT',  # Percent left leading edge flap extended
	'LEADING_EDGE_FLAPS_RIGHT_PERCENT',  # Percent right leading edge flap extended
	'LEADING_EDGE_FLAPS_LEFT_ANGLE',  # Angle left leading edge flap extended. Use LEADING EDGE FLAPS LEFT PERCENT to set a value.
	'LEADING_EDGE_FLAPS_RIGHT_ANGLE',  # Angle right leading edge flap extended. Use LEADING EDGE FLAPS RIGHT PERCENT to set a value.
	'FLAPS_AVAILABLE',  # True if flaps available
	'FLAP_DAMAGE_BY_SPEED',  # True if flagps are damaged by excessive speed
	'FLAP_SPEED_EXCEEDED',  # True if safe speed limit for flaps exceeded
]

request_throttle = [
	'AUTOPILOT_THROTTLE_ARM',  # Autothrottle armed
	'AUTOPILOT_TAKEOFF_POWER_ACTIVE',  # Takeoff / Go Around power mode active
	'AUTOTHROTTLE_ACTIVE',  # Auto-throttle active
	'FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO',  # Full throttle thrust to weight ratio
	'THROTTLE_LOWER_LIMIT',
	'GENERAL_ENG_THROTTLE_LEVER_POSITION:index',  # Percent of max throttle position
	'AUTOPILOT_THROTTLE_ARM',  # Autothrottle armed
	'AUTOTHROTTLE_ACTIVE',  # Auto-throttle active
	'FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO',  # Full throttle thrust to weight ratio
]

request_gear = [
	'IS_GEAR_RETRACTABLE',  # True if gear can be retracted
	'IS_GEAR_SKIS',  # True if landing gear is skis
	'IS_GEAR_FLOATS',  # True if landing gear is floats
	'IS_GEAR_SKIDS',  # True if landing gear is skids
	'IS_GEAR_WHEELS',  # True if landing gear is wheels
	'GEAR_HANDLE_POSITION',  # True if gear handle is applied
	'GEAR_HYDRAULIC_PRESSURE',  # Gear hydraulic pressure
	'TAILWHEEL_LOCK_ON',  # True if tailwheel lock applied
	'GEAR_CENTER_POSITION',  # Percent center gear extended
	'GEAR_LEFT_POSITION',  # Percent left gear extended
	'GEAR_RIGHT_POSITION',  # Percent right gear extended
	'GEAR_TAIL_POSITION',  # Percent tail gear extended
	'GEAR_AUX_POSITION',  # Percent auxiliary gear extended
	'GEAR_TOTAL_PCT_EXTENDED',  # Percent total gear extended
	'AUTO_BRAKE_SWITCH_CB',  # Auto brake switch position
	'WATER_RUDDER_HANDLE_POSITION',
	'WATER_LEFT_RUDDER_EXTENDED',  # Percent extended
	'WATER_RIGHT_RUDDER_EXTENDED',  # Percent extended
	'GEAR_CENTER_STEER_ANGLE',  # Center wheel angle, negative to the left, positive to the right.
	'GEAR_LEFT_STEER_ANGLE',  # Left wheel angle, negative to the left, positive to the right.
	'GEAR_RIGHT_STEER_ANGLE',  # Right wheel angle, negative to the left, positive to the right.
	'GEAR_AUX_STEER_ANGLE',  # Aux wheel angle, negative to the left, positive to the right. The aux wheel is the fourth set of gear, sometimes used on helicopters.
	'WATER_LEFT_RUDDER_STEER_ANGLE',  # Water left rudder angle, negative to the left, positive to the right.
	'WATER_RIGHT_RUDDER_STEER_ANGLE',  # Water right rudder angle, negative to the left, positive to the right.
	'GEAR_CENTER_STEER_ANGLE_PCT',  # Center steer angle as a percentage
	'GEAR_LEFT_STEER_ANGLE_PCT',  # Left steer angle as a percentage
	'GEAR_RIGHT_STEER_ANGLE_PCT',  # Right steer angle as a percentage
	'GEAR_AUX_STEER_ANGLE_PCT',  # Aux steer angle as a percentage
	'WATER_LEFT_RUDDER_STEER_ANGLE_PCT',  # Water left rudder angle as a percentage
	'WATER_RIGHT_RUDDER_STEER_ANGLE_PCT',  # Water right rudder as a percentage
	'CENTER_WHEEL_RPM',  # Center landing gear rpm
	'LEFT_WHEEL_RPM',  # Left landing gear rpm
	'RIGHT_WHEEL_RPM',  # Right landing gear rpm
	'AUX_WHEEL_RPM',  # Rpm of fourth set of gear wheels.
	'CENTER_WHEEL_ROTATION_ANGLE',  # Center wheel rotation angle
	'LEFT_WHEEL_ROTATION_ANGLE',  # Left wheel rotation angle
	'RIGHT_WHEEL_ROTATION_ANGLE',  # Right wheel rotation angle
	'AUX_WHEEL_ROTATION_ANGLE',  # Aux wheel rotation angle
	'GEAR_EMERGENCY_HANDLE_POSITION',  # True if gear emergency handle applied
	'ANTISKID_BRAKES_ACTIVE',  # True if antiskid brakes active
	'RETRACT_FLOAT_SWITCH',  # True if retract float switch on
	'RETRACT_LEFT_FLOAT_EXTENDED',  # If aircraft has retractable floats.
	'RETRACT_RIGHT_FLOAT_EXTENDED',  # If aircraft has retractable floats.
	'STEER_INPUT_CONTROL',  # Position of steering tiller
	'GEAR_DAMAGE_BY_SPEED',  # True if gear has been damaged by excessive speed
	'GEAR_SPEED_EXCEEDED',  # True if safe speed limit for gear exceeded
	'NOSEWHEEL_LOCK_ON',  # True if the nosewheel lock is engaged.
]

request_trim = [
	'ROTOR_LATERAL_TRIM_PCT',  # Trim percent
	'ELEVATOR_TRIM_POSITION',  # Elevator trim deflection
	'ELEVATOR_TRIM_INDICATOR',
	'ELEVATOR_TRIM_PCT',  # Percent elevator trim
	'AILERON_TRIM',  # Angle deflection
	'AILERON_TRIM_PCT',  # The trim position of the ailerons. Zero is fully retracted.
	'RUDDER_TRIM_PCT',  # The trim position of the rudder. Zero is no trim.
	'RUDDER_TRIM',  # Angle deflection
]

request_autopilot = [
	'AUTOPILOT_MASTER',
	'AUTOPILOT_AVAILABLE',
	'AUTOPILOT_NAV_SELECTED',
	'AUTOPILOT_WING_LEVELER',
	'AUTOPILOT_NAV1_LOCK',
	'AUTOPILOT_HEADING_LOCK',
	'AUTOPILOT_HEADING_LOCK_DIR',
	'AUTOPILOT_ALTITUDE_LOCK',
	'AUTOPILOT_ALTITUDE_LOCK_VAR',
	'AUTOPILOT_ATTITUDE_HOLD',
	'AUTOPILOT_GLIDESLOPE_HOLD',
	'AUTOPILOT_PITCH_HOLD_REF',
	'AUTOPILOT_APPROACH_HOLD',
	'AUTOPILOT_BACKCOURSE_HOLD',
	'AUTOPILOT_VERTICAL_HOLD_VAR',
	'AUTOPILOT_PITCH_HOLD',
	'AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE',
	'AUTOPILOT_FLIGHT_DIRECTOR_PITCH',
	'AUTOPILOT_FLIGHT_DIRECTOR_BANK',
	'AUTOPILOT_AIRSPEED_HOLD',
	'AUTOPILOT_AIRSPEED_HOLD_VAR',
	'AUTOPILOT_MACH_HOLD',
	'AUTOPILOT_MACH_HOLD_VAR',
	'AUTOPILOT_YAW_DAMPER',
	'AUTOPILOT_RPM_HOLD_VAR',
	'AUTOPILOT_THROTTLE_ARM',
	'AUTOPILOT_TAKEOFF_POWER ACTIVE',
	'AUTOTHROTTLE_ACTIVE',
	'AUTOPILOT_VERTICAL_HOLD',
	'AUTOPILOT_RPM_HOLD',
	'AUTOPILOT_MAX_BANK',
	'FLY_BY_WIRE_ELAC_SWITCH',
	'FLY_BY_WIRE_FAC_SWITCH',
	'FLY_BY_WIRE_SEC_SWITCH',
	'FLY_BY_WIRE_ELAC_FAILED',
	'FLY_BY_WIRE_FAC_FAILED',
	'FLY_BY_WIRE_SEC_FAILED'
]

request_cabin = [
	'CABIN_SEATBELTS_ALERT_SWITCH',
	'CABIN_NO_SMOKING_ALERT_SWITCH'
]


def thousandify(x):
	return f"{x:,}"


@app.route('/')
def glass():
	return render_template("glass.html")


@app.route('/attitude-indicator')
def AttInd():
	return render_template("attitude-indicator/index.html")


def get_dataset(data_type):
	if data_type == "navigation": request_to_action = request_location
	if data_type == "airspeed": request_to_action = request_airspeed
	if data_type == "compass": request_to_action = request_compass
	if data_type == "vertical_speed": request_to_action = request_vertical_speed
	if data_type == "fuel": request_to_action = request_fuel
	if data_type == "flaps": request_to_action = request_flaps
	if data_type == "throttle": request_to_action = request_throttle
	if data_type == "gear": request_to_action = request_gear
	if data_type == "trim": request_to_action = request_trim
	if data_type == "autopilot": request_to_action = request_autopilot
	if data_type == 'cabin': request_to_action = request_cabin
	#if data_type == "ui": request_to_action = request_ui   # see comment above as to why I've removed this

	return request_to_action

async def ui_dictionary(ui_friendly_dictionary):
	# Fuel
	ui_friendly_dictionary["FUEL_PERCENTAGE"] = round((await aq.get("FUEL_TOTAL_QUANTITY") / await aq.get("FUEL_TOTAL_CAPACITY")) * 100)
	ui_friendly_dictionary["AIRSPEED_INDICATE"] = round(await aq.get("AIRSPEED_INDICATED"))
	ui_friendly_dictionary["ALTITUDE"] = thousandify(round(await aq.get("PLANE_ALTITUDE")))
	# Control surfaces
	if await aq.get("GEAR_HANDLE_POSITION") == 1:
		ui_friendly_dictionary["GEAR_HANDLE_POSITION"] = "DOWN"
	else:
		ui_friendly_dictionary["GEAR_HANDLE_POSITION"] = "UP"
	ui_friendly_dictionary["FLAPS_HANDLE_PERCENT"] = round(await aq.get("FLAPS_HANDLE_PERCENT") * 100)

	ui_friendly_dictionary["ELEVATOR_TRIM_PCT"] = round(await aq.get("ELEVATOR_TRIM_PCT") * 100)
	ui_friendly_dictionary["RUDDER_TRIM_PCT"] = round(await aq.get("RUDDER_TRIM_PCT") * 100)

	# Navigation
	ui_friendly_dictionary["LATITUDE"] = await aq.get("PLANE_LATITUDE")
	ui_friendly_dictionary["LONGITUDE"] = await aq.get("PLANE_LONGITUDE")
	ui_friendly_dictionary["MAGNETIC_COMPASS"] = round(await aq.get("MAGNETIC_COMPASS"))
	ui_friendly_dictionary["MAGVAR"] = round(await aq.get("MAGVAR"))
	ui_friendly_dictionary["VERTICAL_SPEED"] = round(await aq.get("VERTICAL_SPEED"))

	# Autopilot
	ui_friendly_dictionary["AUTOPILOT_MASTER"] = await aq.get("AUTOPILOT_MASTER")
	ui_friendly_dictionary["AUTOPILOT_NAV_SELECTED"] = await aq.get("AUTOPILOT_NAV_SELECTED")
	ui_friendly_dictionary["AUTOPILOT_WING_LEVELER"] = await aq.get("AUTOPILOT_WING_LEVELER")
	ui_friendly_dictionary["AUTOPILOT_HEADING_LOCK"] = await aq.get("AUTOPILOT_HEADING_LOCK")
	ui_friendly_dictionary["AUTOPILOT_HEADING_LOCK_DIR"] = round(await aq.get("AUTOPILOT_HEADING_LOCK_DIR"))
	ui_friendly_dictionary["AUTOPILOT_ALTITUDE_LOCK"] = await aq.get("AUTOPILOT_ALTITUDE_LOCK")
	ui_friendly_dictionary["AUTOPILOT_ALTITUDE_LOCK_VAR"] = thousandify(round(await aq.get("AUTOPILOT_ALTITUDE_LOCK_VAR")))
	ui_friendly_dictionary["AUTOPILOT_ATTITUDE_HOLD"] = await aq.get("AUTOPILOT_ATTITUDE_HOLD")
	ui_friendly_dictionary["AUTOPILOT_GLIDESLOPE_HOLD"] = await aq.get("AUTOPILOT_GLIDESLOPE_HOLD")
	ui_friendly_dictionary["AUTOPILOT_APPROACH_HOLD"] = await aq.get("AUTOPILOT_APPROACH_HOLD")
	ui_friendly_dictionary["AUTOPILOT_BACKCOURSE_HOLD"] = await aq.get("AUTOPILOT_BACKCOURSE_HOLD")
	ui_friendly_dictionary["AUTOPILOT_VERTICAL_HOLD"] = await aq.get("AUTOPILOT_VERTICAL_HOLD")
	ui_friendly_dictionary["AUTOPILOT_VERTICAL_HOLD_VAR"] = await aq.get("AUTOPILOT_VERTICAL_HOLD_VAR")
	ui_friendly_dictionary["AUTOPILOT_PITCH_HOLD"] = await aq.get("AUTOPILOT_PITCH_HOLD")
	ui_friendly_dictionary["AUTOPILOT_PITCH_HOLD_REF"] = await aq.get("AUTOPILOT_PITCH_HOLD_REF")
	ui_friendly_dictionary["AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE"] = await aq.get("AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE")
	ui_friendly_dictionary["AUTOPILOT_AIRSPEED_HOLD"] = await aq.get("AUTOPILOT_AIRSPEED_HOLD")
	ui_friendly_dictionary["AUTOPILOT_AIRSPEED_HOLD_VAR"] = round(await aq.get("AUTOPILOT_AIRSPEED_HOLD_VAR"))

	# Cabin
	ui_friendly_dictionary["CABIN_SEATBELTS_ALERT_SWITCH"] = await aq.get("CABIN_SEATBELTS_ALERT_SWITCH")
	ui_friendly_dictionary["CABIN_NO_SMOKING_ALERT_SWITCH"] = await aq.get("CABIN_NO_SMOKING_ALERT_SWITCH")

@app.route('/ui')
def output_ui_variables():
	# Initialise dictionaru
	ui_friendly_dictionary = {}
	ui_friendly_dictionary["STATUS"] = "success"
	asyncio.run(ui_dictionary(ui_friendly_dictionary))
	return jsonify(ui_friendly_dictionary)


async def _dictionary(data_dictionary):
	dataset_map = {}  # I have renamed map to dataset_map as map is used elsewhere
	for datapoint_name in data_dictionary:
		print(datapoint_name)
		dataset_map[datapoint_name] = await aq.get(datapoint_name)
	return jsonify(dataset_map)

@app.route('/dataset/<dataset_name>/', methods=["GET"])
def output_json_dataset(dataset_name):
	data_dictionary = get_dataset(dataset_name)
	return asyncio.run(_dictionary(data_dictionary))


async def get_datapoint(datapoint_name, index=None):
	# This function actually does the work of getting the datapoint

	if index is not None and ':index' in datapoint_name:
		dp = aq.find(datapoint_name)
		if dp is not None:
			dp.setIndex(int(index))

	return await aq.get(datapoint_name)


@app.route('/datapoint/<datapoint_name>/get', methods=["GET"])
def get_datapoint_endpoint(datapoint_name):
	# This is the http endpoint wrapper for getting a datapoint

	ds = request.get_json() if request.is_json else request.form
	index = ds.get('index')

	output = asyncio.run(get_datapoint(datapoint_name, index))

	if isinstance(output, bytes):
		output = output.decode('ascii')

	return jsonify(output)


def set_datapoint(datapoint_name, index=None, value_to_use=None):
	# This function actually does the work of setting the datapoint

	if index is not None and ':index' in datapoint_name:
		clas = aq.find(datapoint_name)
		if clas is not None:
			clas.setIndex(int(index))

	sent = False
	if value_to_use is None:
		sent = aq.set(datapoint_name, 0)
	else:
		sent = aq.set(datapoint_name, int(value_to_use))

	if sent is True:
		status = "success"
	else:
		status = "Error with sending request: %s" % (datapoint_name)

	return status


@app.route('/datapoint/<datapoint_name>/set', methods=["POST"])
def set_datapoint_endpoint(datapoint_name):
	# This is the http endpoint wrapper for setting a datapoint
	ds = request.get_json() if request.is_json else request.form
	index = ds.get('index')
	value_to_use = ds.get('value_to_use')
	status = set_datapoint(datapoint_name, index, value_to_use)
	return jsonify(status)


def trigger_event(event_name, value_to_use=None):
	# This function actually does the work of triggering the event

	EVENT_TO_TRIGGER = ae.find(event_name)
	if EVENT_TO_TRIGGER is not None:
		if value_to_use is None:
			EVENT_TO_TRIGGER()
		else:
			EVENT_TO_TRIGGER(int(value_to_use))

		status = "success"
	else:
		status = "Error: %s is not an Event" % (event_name)

	return status


@app.route('/event/<event_name>/trigger', methods=["POST"])
def trigger_event_endpoint(event_name):
	# This is the http endpoint wrapper for triggering an event

	ds = request.get_json() if request.is_json else request.form
	value_to_use = ds.get('value_to_use')

	status = trigger_event(event_name, value_to_use)

	return jsonify(status)


async def get_engen_ct():
	return await aq.get("NUMBER_OF_ENGINES")

@app.route('/custom_emergency/<emergency_type>', methods=["GET", "POST"])
def custom_emergency(emergency_type):

	text_to_return = "No valid emergency type passed"

	if emergency_type == "random_engine_fire":
		# Calculate number of engines
		number_of_engines = asyncio.run(get_engen_ct())

		if number_of_engines < 0:
			return "error, no engines found - is sim running?"
		engine_to_set_on_fire = random.randint(1, number_of_engines)

		set_datapoint("ENG_ON_FIRE:index", engine_to_set_on_fire, 1)

		text_to_return = "Engine " + str(engine_to_set_on_fire) + " on fire"

	return text_to_return


app.run(host='0.0.0.0', port=5000, debug=True)
