from SimConnect import *
import logging
from SimConnect.Enum import *
from time import sleep


logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.info("START")
# time holder for inline commands
ct_g = millis()

# creat simconnection and pass used user classes
sm = SimConnect()
aq = AircraftRequests(sm)
ae = AircraftEvents(sm)

# Set pos arund space nedle in WA.
sm.set_pos(
	_Altitude=1000.0,
	_Latitude=47.614699,
	_Longitude=-122.358473,
	_Airspeed=130,
	_Heading=70.0,
	# _Pitch=0.0,
	# _Bank=0.0,
	# _OnGround=0
)

# PARKING_BRAKES = Event(b'PARKING_BRAKES', sm)
# long path
PARKING_BRAKES = ae.Miscellaneous_Systems.PARKING_BRAKES
# using get
GEAR_TOGGLE = ae.Miscellaneous_Systems.get("GEAR_TOGGLE")
# Using find to lookup Event
AP_MASTER = ae.find("AP_MASTER")

# THROTTLE1 Event
THROTTLE1 = ae.Engine.THROTTLE1_SET


# THROTTLE1 Request
Throttle = aq.find('GENERAL_ENG_THROTTLE_LEVER_POSITION:1')

# If useing
# Throttle = aq.find('GENERAL_ENG_THROTTLE_LEVER_POSITION:index')
# Need to set index befor read/write
# Note to set index 2 vs 1 just re-run
# Throttle.setIndex(1)


# print the built in description
# AP_MASTER Toggles AP on/off
print("AP_MASTER", AP_MASTER.description) 
# Throttle Percent of max throttle position
print("Throttle", Throttle.description)
# THROTTLE1 Set throttle 1 exactly (0 to 16383)
print("THROTTLE1", THROTTLE1.description)


while not sm.quit:
	print("Throttle:", Throttle.value)
	print("Alt=%f Lat=%f Lon=%f Kohlsman=%.2f" % (
		aq.PositionandSpeedData.get('PLANE_ALTITUDE'),
		aq.PositionandSpeedData.get('PLANE_LATITUDE'),
		aq.PositionandSpeedData.get('PLANE_LONGITUDE'),
		aq.FlightInstrumentationData.get('KOHLSMAN_SETTING_HG')
	))
	sleep(2)

	# Send Event with value
	# THROTTLE1(1500)

	# Send Event toggle AP_MASTER
	# AP_MASTER()

	# PARKING_BRAKES()

	# send new data inine @ 5s
	if ct_g + 5000 < millis():
		if Throttle.value < 100:
			Throttle.value += 5
			print("THROTTLE SET")
		ct_g = millis()

sm.exit()
