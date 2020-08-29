from PythonSimConnect import *


class INPUT_GROUP_ID(SIMCONNECT_INPUT_GROUP_ID):  # client-defined input group ID
	pass


class CLIENT_DATA_ID(SIMCONNECT_CLIENT_DATA_ID):  # client-defined client data ID
	pass


class CLIENT_DATA_DEFINITION_ID(SIMCONNECT_CLIENT_DATA_DEFINITION_ID):  # client-defined client data definition ID
	pass


class EVENT_ID(SIMCONNECT_CLIENT_EVENT_ID):  # client-defined client event ID
	EVENT_SIM_START = 1
	GEAR_Down = 2
	GEAR_Up = 3
	GEAR_TOGGLE = 4


class GROUP_ID(SIMCONNECT_NOTIFICATION_GROUP_ID):  # client-defined notification group ID
	GROUP_A = 0


class DATA_DEFINE_ID(SIMCONNECT_DATA_DEFINITION_ID):  # client-defined data definition ID
	DEFINITION_1 = 0
	DEFINITION_2 = 1


class DATA_REQUEST_ID(SIMCONNECT_DATA_REQUEST_ID):   # client-defined request data ID
	REQUEST_1 = 10
	REQUEST_2 = 22


class outputData(Structure):
	_fields_ = [
		("altitude", c_double),
		("latitude", c_double),
		("longitude", c_double),
		("kohlsmann", c_double),
		("GEAR", c_double)
	]


myRequest = Request(
	_DATA_DEFINITION_ID=DATA_DEFINE_ID.DEFINITION_1,
	_DATA_REQUEST_ID=DATA_REQUEST_ID.REQUEST_1,
	_outputData=outputData
)
myRequest.definitions.append((b'Plane Altitude', b'feet'))
myRequest.definitions.append((b'Plane Latitude', b'degrees'))
myRequest.definitions.append((b'Plane Longitude', b'degrees'))
myRequest.definitions.append((b'Kohlsman setting hg', b'inHg'))
myRequest.definitions.append((b'GEAR HANDLE POSITION', b'bool'))


class outData2(Structure):
	_fields_ = [
		("altitude", c_double),
		("gear", c_double)
	]


myRequest2 = Request(
	_DATA_DEFINITION_ID=DATA_DEFINE_ID.DEFINITION_2,
	_DATA_REQUEST_ID=DATA_REQUEST_ID.REQUEST_2,
	_outputData=outData2
)
myRequest2.definitions.append((b'PRESSURE ALTITUDE', b'feet'))
myRequest2.definitions.append((b'GEAR HANDLE POSITION', b'bool'))


sm = PythonSimConnect(
	_CLIENT_EVENT_ID=EVENT_ID,
	_NOTIFICATION_GROUP_ID=GROUP_ID,
	_DATA_DEFINITION_ID=DATA_DEFINE_ID,
	_DATA_REQUEST_ID=DATA_REQUEST_ID
)

sm.setup()
sm.Add_Definition(myRequest)
sm.Add_Definition(myRequest2)

sm.MapToSimEvent(b'GEAR_DOWN', EVENT_ID.GEAR_Down)
sm.MapToSimEvent(b'GEAR_UP', EVENT_ID.GEAR_Up)
sm.MapToSimEvent(b'GEAR_TOGGLE', EVENT_ID.GEAR_TOGGLE)

sentTest = False
gear = False
ct_r = millis()
ct_r2 = millis()
ct_g = millis()

while sm.quit == 0:
	if (ct_r + 5000) < millis():
		sm.RequestData(myRequest)
		ct_r = millis()

	if (ct_r2 + 10000) < millis():
		sm.RequestData(myRequest2)
		ct_r2 = millis()

	sm.run()

	data = sm.out_data[myRequest.DATA_REQUEST_ID]
	if data is not None:
		print("Lat=%f  Lon=%f  Alt=%f Kohlsman=%.2f GEAR=%d" % (
			data.latitude,
			data.longitude,
			data.altitude,
			data.kohlsmann,
			data.GEAR
		))

	data = sm.out_data[myRequest2.DATA_REQUEST_ID]
	if data is not None:
		print("Alt=%f GEAR=%d" % (
			data.altitude,
			data.gear
		))

	if ct_g + 10000 < millis():
		sm.SendData(EVENT_ID.GEAR_TOGGLE)
		print("GEAR TOGGLE")
		ct_g = millis()

sm.exit()
