from SimConnect import *
from time import sleep

# create simconnection
sm = SimConnect()

# create Request
myRequest = sm.new_request(time=2000)  # set auto data collection time @ 2s
# add required definitions output data name, definition from SDK
myRequest.add('Altitude', (b'Plane Altitude', b'feet'))
myRequest.add('Latitude', (b'Plane Latitude', b'degrees'))
myRequest.add('Longitude', (b'Plane Longitude', b'degrees'))
myRequest.add('Kohlsman', (b'Kohlsman setting hg', b'inHg'))

while 1:
	sm.request_data(myRequest)
	sm.run()

	data = sm.get_data(myRequest)
	if data is not None:
		print(data)
	else:
		print("Data is none")

	sleep(1)
sm.Exit()
