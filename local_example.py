from SimConnect import *
import logging
from SimConnect.Enum import *
from time import sleep

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.info("START")

# creat simconnection and pass used user classes
sm = SimConnect()
aq = AircraftRequests(sm)


# sm.exit()
# quit()

AI_OBJECT_ID = 1
pa = aq.find("PLANE_ALTITUDE")
pa.OBJECT_ID = AI_OBJECT_ID

phdyt = aq.find("PLANE_HEADING_DEGREES_TRUE")
phdyt.OBJECT_ID = AI_OBJECT_ID

pla = aq.find("PLANE_LATITUDE")
pla.OBJECT_ID = AI_OBJECT_ID

plo = aq.find("PLANE_LONGITUDE")
plo.OBJECT_ID = AI_OBJECT_ID


while not sm.quit:
	print("PLANE ALTITUDE:", pa.value)
	print("PLANE HEADING DEGREES TRUE:", phdyt.value)
	print("PLANE LATITUDE:", pla.value)
	print("PLANE LONGITUDE:", plo.value)
	sleep(2)

sm.exit()
quit()