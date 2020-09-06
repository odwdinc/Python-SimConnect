from SimConnect import *

from unittest import TestCase


import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

LOGGER.info("START")

# creat simconnection and pass used user classes
sm = SimConnect()

# creat Request
myRequest = sm.new_request(time=2000)  # set auto data collection time @ 2s
# add instreaded definitions output data name, definition form SDK
myRequest.add('Altitude', (b'Plane Altitude', b'feet'))
myRequest.add('Latitude', (b'Plane Latitude', b'degrees'))
myRequest.add('Longitude', (b'Plane Longitude', b'degrees'))
myRequest.add('Kohlsman', (b'Kohlsman setting hg', b'inHg'))

# creat Request
myRequest2 = sm.new_request()
# add instreaded definitions output data name, definition form SDK
myRequest2.add('ALTITUDE', (b'PRESSURE ALTITUDE', b'feet'))
myRequest2.add('GEAR', (b'GEAR HANDLE POSITION', b'bool'))
# Add data request Definition


# creat Request
THROTTLERequest = sm.new_request(time=5000)  # set auto data collection time @ 5s
# add instreaded definitions output data name, definition form SDK
THROTTLERequest.add('THROTTLE', (b'GENERAL ENG THROTTLE LEVER POSITION:1', b'Percent'))


# add input events
GEAR_DOWN = sm.map_to_sim_event(b'GEAR_DOWN')
GEAR_UP = sm.map_to_sim_event(b'GEAR_UP')
GEAR_TOGGLE = sm.map_to_sim_event(b'GEAR_TOGGLE')
AP_MASTER = sm.map_to_sim_event(b'AP_MASTER')
THROTTLE1_SET = sm.map_to_sim_event(b'THROTTLE1_SET')

# time holder for inline commands
ct_r2 = millis()
ct_g = millis()

temp_THROTTLE = 0

while not sm.quit:
	# send request for new data inine @ 10s
	if (ct_r2 + 10000) < millis():
		sm.request_data(myRequest2)
		ct_r2 = millis()

	# send request for new data inine @ 15s
	if ct_g + 5000 < millis():
		print("THROTTLE1_SET")
		sm.send_event(THROTTLE1_SET, DWORD(temp_THROTTLE))
		temp_THROTTLE += 100
		ct_g = millis()

	# updated system
	sm.run()

	# check for data from myRequest
	if sm.get_data(myRequest):
		print("Lat=%f  Lon=%f  Alt=%f Kohlsman=%.2f" % (
			myRequest.outData["Latitude"],
			myRequest.outData["Longitude"],
			myRequest.outData["Altitude"],
			myRequest.outData["Kohlsman"]
		))

	# check for data from myRequest2
	if sm.get_data(myRequest2):
		print("Alt=%f GEAR=%d" % (
			myRequest2.outData["ALTITUDE"],
			myRequest2.outData["GEAR"]
		))

	# check for data from THROTTLERequest
	if sm.get_data(THROTTLERequest):
		print("THROTTLE: %f" % (
			THROTTLERequest.outData["THROTTLE"]
		))

sm.exit()
