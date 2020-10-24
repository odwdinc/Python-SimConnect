from SimConnect import *
import logging
from time import sleep
import asyncio
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.info("START")
sm = SimConnect()
aq = AircraftRequests(sm)

Data = {}


async def pintVal(name):
	global Data
	Data[name] = await aq.get(name)


async def main():
	while not sm.quit:
		temp = {}
		for ed in aq.PositionandSpeedData.list:
			temp[ed] = asyncio.create_task(pintVal(ed))

		for ed in aq.PositionandSpeedData.list:
			await temp[ed]

		print(Data)
		sleep(2)
	sm.exit()
	quit()


asyncio.run(main())