from SimConnect import *
from time import sleep

# create simconnection
sm = SimConnect()

# create Request
myRequest = sm.newRequest(time=2000)  # set auto data collection time @ 2s

# add required definitions output data name, definition from SDK
myRequest.add('Altitude', (b'Plane Altitude', b'feet'))
myRequest.add('Latitude', (b'Plane Latitude', b'degrees'))
myRequest.add('Longitude', (b'Plane Longitude', b'degrees'))
myRequest.add('Kohlsman', (b'Kohlsman setting hg', b'inHg'))

while 1:
	sm.RequestData(myRequest)
	sm.Run()
	data = sm.GetData(myRequest)

	if data is not None:
		print("Lat=%f  Lon=%f  Alt=%f Kohlsman=%.2f" % (
			data.Latitude,
			data.Longitude,
			data.Altitude,
			data.Kohlsman
		))

	sleep (1)

sm.Exit()
