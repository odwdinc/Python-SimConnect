from SimConnect import *

from unittest import TestCase
from time import sleep


import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

LOGGER.info("START")

# creat simconnection and pass used user classes
sm = SimConnect()

# creat Request just for sending data
ThrottleRequest = sm.new_request()  # set auto data collection time @ 5s
# add instreaded definitions output data name, definition form SDK
ThrottleRequest.add('ThrL_p1', (b'GENERAL ENG THROTTLE LEVER POSITION:1', b'Percent'))
# Note: the data need to be Settable per the SDK see
# https://docs.microsoft.com/en-us/previous-versions/microsoft-esp/cc526981(v=msdn.10)

# sm.request_data(ThrottleRequest)  # get curent data not neede but nice to see the update.

while not sm.quit:
	# updated system
	# sm.run()

	# Check for data from ThrottleRequest
	# returns true if new data was avable.
	# Need to set time varable on new request
	# or a call to request_data is needed.

	# if sm.get_data(ThrottleRequest):
	# 	print("THROTTLE: %f" % (
	# 		ThrottleRequest.outData["ThrL_p1"]
	# 	))

	# Check if curent data is less then 100%
	if ThrottleRequest.outData['ThrL_p1'] < 100:
		# update the with new value
		ThrottleRequest.outData['ThrL_p1'] += 10
		# set the data for next run to send to
		sm.set_data(ThrottleRequest)
		# sm.request_data(ThrottleRequest)
		sleep(2)

sm.exit()
