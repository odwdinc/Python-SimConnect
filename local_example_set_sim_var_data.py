from SimConnect import *

from unittest import TestCase


import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

LOGGER.info("START")

# creat simconnection and pass used user classes
sm = SimConnect()

# creat Request
ThrottleRequest = sm.new_request(time=2000)  # set auto data collection time @ 5s
# add instreaded definitions output data name, definition form SDK
ThrottleRequest.add('ThrL_p1', (b'GENERAL ENG THROTTLE LEVER POSITION:1', b'Percent'))

while not sm.quit:
	# updated system
	sm.run()

	# check for data from THROTTLERequest
	data = sm.get_data(ThrottleRequest)
	if data is not None:
		print("THROTTLE 1: %f" % (
			data['ThrL_p1']
		))
		# update the with new value
		data['ThrL_p1'] += 10
		sm.set_data(ThrottleRequest, data)

sm.exit()
