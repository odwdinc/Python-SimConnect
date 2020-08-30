from PythonSimConnect import *


class INPUT_GROUP_ID(SIMCONNECT_INPUT_GROUP_ID):  # client-defined input group ID
	pass


class CLIENT_DATA_ID(SIMCONNECT_CLIENT_DATA_ID):  # client-defined client data ID
	pass


class CLIENT_DATA_DEFINITION_ID(SIMCONNECT_CLIENT_DATA_DEFINITION_ID):  # client-defined client data definition ID
	pass


class GROUP_ID(SIMCONNECT_NOTIFICATION_GROUP_ID):  # client-defined notification group ID
	GROUP_A = auto()


# user date deffintion override
class DATA_DEFINE_ID(SIMCONNECT_DATA_DEFINITION_ID):  # client-defined data definition ID
	DEFINITION_1 = auto()
	DEFINITION_2 = auto()


# user output event class override
class DATA_REQUEST_ID(SIMCONNECT_DATA_REQUEST_ID):   # client-defined request data ID
	REQUEST_1 = auto()
	REQUEST_2 = auto()


# Data output structure for myRequest
class outputData(Structure):
	_fields_ = [
		("altitude", c_double),
		("latitude", c_double),
		("longitude", c_double),
		("kohlsmann", c_double),
	]


# creat Request
myRequest = Request(
	_DATA_DEFINITION_ID=DATA_DEFINE_ID.DEFINITION_1,
	_DATA_REQUEST_ID=DATA_REQUEST_ID.REQUEST_1,
	_outputData=outputData,
	_time=2000  # set auto data collection time @ 2s
)
# add instreaded definitions
myRequest.definitions.append((b'Plane Altitude', b'feet'))
myRequest.definitions.append((b'Plane Latitude', b'degrees'))
myRequest.definitions.append((b'Plane Longitude', b'degrees'))
myRequest.definitions.append((b'Kohlsman setting hg', b'inHg'))


# Data output structure for myRequest2
class outData2(Structure):
	_fields_ = [
		("altitude", c_double),
		("gear", c_double)
	]


# creat Request
myRequest2 = Request(
	_DATA_DEFINITION_ID=DATA_DEFINE_ID.DEFINITION_2,
	_DATA_REQUEST_ID=DATA_REQUEST_ID.REQUEST_2,
	_outputData=outData2,
)

# add instreaded definitions
myRequest2.definitions.append((b'PRESSURE ALTITUDE', b'feet'))
myRequest2.definitions.append((b'GEAR HANDLE POSITION', b'bool'))


# creat simconnection and pass used user classes
sm = PythonSimConnect(
	_NOTIFICATION_GROUP_ID=GROUP_ID,
	_DATA_DEFINITION_ID=DATA_DEFINE_ID,
	_DATA_REQUEST_ID=DATA_REQUEST_ID
)

# Start up Sim and check for connection.
sm.setup()

# add data request Definition
sm.Add_Definition(myRequest)
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
			data.latitude,
			data.longitude,
			data.altitude,
			data.kohlsmann,
		))

	# check for data from myRequest2
	data = sm.GetData(myRequest2)
	if data is not None:
		print("Alt=%f GEAR=%d" % (
			data.altitude,
			data.gear
		))

sm.Exit()
