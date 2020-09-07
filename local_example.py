from SimConnect import *
import logging
from SimConnect.Enum import *
from time import sleep


logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.info("START")


# creat simconnection and pass used user classes
sm = SimConnect()

Throttle = Request((b'GENERAL ENG THROTTLE LEVER POSITION:1', b'Percent'), sm, _time=500)
Altitude = Request((b'Plane Altitude', b'feet'), sm)
Latitude = Request((b'Plane Latitude', b'degrees'), sm)
Longitude = Request((b'Plane Longitude', b'degrees'), sm)
Kohlsman = Request((b'Kohlsman setting hg', b'inHg'), sm)

PARKING_BRAKES = Event(b'PARKING_BRAKES', sm)
GEAR_DOWN = Event(b'GEAR_DOWN', sm)
GEAR_UP = Event(b'GEAR_UP', sm)
GEAR_TOGGLE = Event(b'GEAR_TOGGLE', sm)
AP_MASTER = Event(b'AP_MASTER', sm)
THROTTLE1_SET = Event(b'THROTTLE1_SET', sm)

# time holder for inline commands
ct_r2 = millis()
ct_g = millis()

while not sm.quit:
	print("Throttle:", Throttle.value)
	print("Lat=%f  Lon=%f  Alt=%f Kohlsman=%.2f" % (
		Latitude.value,
		Longitude.value,
		Altitude.value,
		Kohlsman.value
	))
	sleep(2)

	# Send Event with value
	# THROTTLE1_SET(1500).

	# Send Event
	# AP_MASTER()

	# send new data inine @ 5s
	if ct_g + 5000 < millis():
		if Throttle.value < 100:
			Throttle.value += 5
			print("THROTTLE SET")
		ct_g = millis()

sm.exit()
