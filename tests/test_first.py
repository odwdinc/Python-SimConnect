from SimConnect import *

from unittest import TestCase

class TestSimple(TestCase):
	def test_first_test(self):
		# creat simconnection and pass used user classes
		sm = SimConnect()

		# creat Request
		myRequest = sm.newRequest(time=2000)  # set auto data collection time @ 2s
		# add instreaded definitions output data name, definition form SDK
		myRequest.add('Altitude', (b'Plane Altitude', b'feet'))
		myRequest.add('Latitude', (b'Plane Latitude', b'degrees'))
		myRequest.add('Longitude', (b'Plane Longitude', b'degrees'))
		myRequest.add('Kohlsman', (b'Kohlsman setting hg', b'inHg'))

		# creat Request
		myRequest2 = sm.newRequest()
		# add instreaded definitions output data name, definition form SDK
		myRequest2.add('ALTITUDE', (b'PRESSURE ALTITUDE', b'feet'))
		myRequest2.add('GEAR', (b'GEAR HANDLE POSITION', b'bool'))
		# Add data request Definition


		# creat Request
		AUTOPILOTRequest = sm.newRequest(time=5000)  # set auto data collection time @ 5s
		# add instreaded definitions output data name, definition form SDK
		AUTOPILOTRequest.add('AUTOPILOT_MASTER', (b'AUTOPILOT MASTER', b'Bool'))


		# add input events
		GEAR_DOWN = sm.MapToSimEvent(b'GEAR_DOWN')
		GEAR_UP = sm.MapToSimEvent(b'GEAR_UP')
		GEAR_TOGGLE = sm.MapToSimEvent(b'GEAR_TOGGLE')
		AP_MASTER = sm.MapToSimEvent(b'AP_MASTER')


		# time holder for inline commands
		ct_r2 = millis()
		ct_g = millis()

		while not sm.quit:
			# send request for new data inine @ 10s
			if (ct_r2 + 10000) < millis():
				sm.RequestData(myRequest2)
				ct_r2 = millis()

			# send request for new data inine @ 15s
			if ct_g + 15000 < millis():
				print("TOGGLE GEAR")
				sm.SendData(GEAR_TOGGLE)
				ct_g = millis()

			# updated system
			sm.Run()

			# check for data from myRequest
			data = sm.GetData(myRequest)
			if data is not None:
				print("Lat=%f  Lon=%f  Alt=%f Kohlsman=%.2f" % (
					data.Latitude,
					data.Longitude,
					data.Altitude,
					data.Kohlsman
				))

			# check for data from myRequest2
			data = sm.GetData(myRequest2)
			if data is not None:
				print("Alt=%f GEAR=%d" % (
					data.ALTITUDE,
					data.GEAR
				))

			# check for data from AUTOPILOTRequest
			data = sm.GetData(AUTOPILOTRequest)
			if data is not None:
				print("AUTOPILOT_MASTER: %d" % (
					data.AUTOPILOT_MASTER
				))

		sm.Exit()

		self.assertTrue(True)
