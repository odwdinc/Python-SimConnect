from SimConnect import *
import logging
from SimConnect.Enum import *
from time import sleep
import signal
import sys

def signal_handler(sig, frame):
	print('Received SIGINT! Exiting now...')
	sm.exit()
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.info("START")
# time holder for inline commands
ct_g = millis()

# creat simconnection and pass used user classes
sm = SimConnect()
aq = AircraftRequests(sm)
ae = AircraftEvents(sm)

atc_id = aq.find('ATC_ID')

print(atc_id.value)

atc_id.value = b'OE-XXX'

while not sm.quit:
	print("Alt=%f Lat=%f Lon=%f Kohlsman=%.2f" % (
		aq.PositionandSpeedData.get('PLANE_ALTITUDE'),
		aq.PositionandSpeedData.get('PLANE_LATITUDE'),
		aq.PositionandSpeedData.get('PLANE_LONGITUDE'),
		aq.FlightInstrumentationData.get('KOHLSMAN_SETTING_HG')
	))
	sleep(2)

sm.exit()
