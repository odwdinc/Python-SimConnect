from SimConnect import *

from unittest import TestCase
from time import sleep


import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

LOGGER.info("START")

# creat simconnection and pass used user classes
sm = SimConnect()

# creat Request
ThrottleRequest = sm.new_request()  # set auto data collection time @ 5s
# add instreaded definitions output data name, definition form SDK
ThrottleRequest.add('ThrL_p1', (b'GENERAL ENG THROTTLE LEVER POSITION:1', b'Percent'))

while not sm.quit:
	# updated system
	sm.run()

	if ThrottleRequest.outData['ThrL_p1'] < 100:
		# update the with new value
		ThrottleRequest.outData['ThrL_p1'] += 10
		sm.set_data(ThrottleRequest)
		sleep(2)

sm.exit()
