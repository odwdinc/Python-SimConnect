from SimConnect import *
import logging
from SimConnect.Enum import *
from time import sleep
import asyncio

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.info("START")


# creat simconnection and pass used user classes
sm = SimConnect()
aq = AircraftRequests(sm, _time=10, _attemps=10)
ae = AircraftEvents(sm)

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


async def main():
	# time holder for inline commands
	ct_g = millis()
	while not sm.quit:
		print("Throttle:", await Throttle.value)
		print("Alt=%f Lat=%f Lon=%f Kohlsman=%.2f" % (
			await aq.PositionandSpeedData.get('PLANE_ALTITUDE'),
			await aq.PositionandSpeedData.get('PLANE_LATITUDE'),
			await aq.PositionandSpeedData.get('PLANE_LONGITUDE'),
			await aq.FlightInstrumentationData.get('KOHLSMAN_SETTING_HG')
		))
		sleep(2)

		# Send Event with value
		# THROTTLE1(1500)

		# Send Event toggle AP_MASTER
		# AP_MASTER()

		# PARKING_BRAKES()

		# send new data inine @ 5s
		if ct_g + 5000 < millis():
			if await Throttle.value < 100:
				Throttle.set(await Throttle.value + 5)
				print("THROTTLE SET")
			ct_g = millis()
	sm.exit()

asyncio.run(main())
