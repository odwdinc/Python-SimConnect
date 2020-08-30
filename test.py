from PythonSimConnect import *


class GROUP_ID(SIMCONNECT_NOTIFICATION_GROUP_ID):  # client-defined notification group ID
	GROUP_A = auto()


# creat simconnection and pass used user classes
sm = PythonSimConnect(_NOTIFICATION_GROUP_ID=GROUP_ID)
# Start up Sim and check for connection.
sm.setup()

# creat Request
myRequest = sm.newRequest("request1", time=2000)  # set auto data collection time @ 2s
# add instreaded definitions output data name, definition form SDK
myRequest.append('altitude', (b'Plane Altitude', b'feet'))
myRequest.append('Latitude', (b'Plane Latitude', b'degrees'))
myRequest.append('Longitude', (b'Plane Longitude', b'degrees'))
myRequest.append('Kohlsman', (b'Kohlsman setting hg', b'inHg'))

# add data request Definition
sm.Add_Definition(myRequest)

# creat Request
myRequest2 = sm.newRequest("request2")
# add instreaded definitions output data name, definition form SDK
myRequest2.append('ALTITUDE', (b'PRESSURE ALTITUDE', b'feet'))
myRequest2.append('GEAR', (b'GEAR HANDLE POSITION', b'bool'))

# add data request Definition
sm.Add_Definition(myRequest2)


# add input events
GEAR_DOWN = sm.MapToSimEvent(b'GEAR_DOWN')
GEAR_UP = sm.MapToSimEvent(b'GEAR_UP')
GEAR_TOGGLE = sm.MapToSimEvent(b'GEAR_TOGGLE')

# time holder for inline commands
ct_r2 = millis()
ct_g = millis()

while sm.quit == 0:

	# send request for new data inine @ 10s
	if (ct_r2 + 10000) < millis():
		sm.RequestData(myRequest2)
		ct_r2 = millis()

	# send input Data @ 15s
	if ct_g + 15000 < millis():
		sm.SendData(GEAR_TOGGLE)
		print("GEAR TOGGLE")
		ct_g = millis()

	# updated system
	sm.Run()

	# check for data from myRequest
	data = sm.GetData(myRequest)
	if data is not None:
		print("Lat=%f  Lon=%f  Alt=%f Kohlsman=%.2f" % (
			data.Latitude,
			data.Longitude,
			data.altitude,
			data.Kohlsman
		))

	# check for data from myRequest2
	data = sm.GetData(myRequest2)
	if data is not None:
		print("Alt=%f GEAR=%d" % (
			data.ALTITUDE,
			data.GEAR
		))

sm.Exit()
