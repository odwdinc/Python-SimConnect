from PythonSimConnect import *
from serial import Serial
# ser = Serial('COM29', 115200)
# data = b"Lat=%f\nLon=%f\r" % (0.0, 0.0)
# ser.write(data)


class EVENT_ID(CtypesEnum):
	EVENT_SIM_START = 1
	GEAR_Down = 2
	GEAR_Up = 3
	GEAR_TOGGLE = 4


class outputData(Structure):
	_fields_ = [
		("altitude", c_double),
		("latitude", c_double),
		("longitude", c_double),
		("kohlsmann", c_double),
		("GEAR", c_double),
		("GEARpos", c_double)
	]


sm = PythonSimConnect(outputData, EVENT_ID)
sm.setup()
sm.Add_Definition(b'Plane Altitude', b'feet')
sm.Add_Definition(b'Plane Latitude', b'degrees')
sm.Add_Definition(b'Plane Longitude', b'degrees')
sm.Add_Definition(b'Kohlsman setting hg', b'inHg')
sm.Add_Definition(b'GEAR HANDLE POSITION', b'bool')

sm.MapToSimEvent(b'GEAR_DOWN', EVENT_ID.GEAR_Down)
sm.MapToSimEvent(b'GEAR_UP', EVENT_ID.GEAR_Up)
sm.MapToSimEvent(b'GEAR_TOGGLE', EVENT_ID.GEAR_TOGGLE)

sentTest = False
gear = False
ct_r = millis()
ct_g = millis()

while sm.quit == 0:
	if (ct_r + 5000) < millis():
		sm.RequestData()
		ct_r = millis()
	sm.run()
	data = sm.out_struct_data
	if data is not None:
		print("Lat=%f  Lon=%f  Alt=%f Kohlsman=%.2f GEAR=%d" % (
			data.latitude,
			data.longitude,
			data.altitude,
			data.kohlsmann,
			data.GEAR
		))
		data = b"Lat=%f\nLon=%f\r" % (data.latitude, data.longitude)
		if ser:
			ser.write(data)
	# if ct_g + 10000 < millis():
	#	sm.SendData(EVENT_ID.GEAR_TOGGLE)
	#	print("GEAR TOGGLE")
	#	ct_g = millis()

sm.exit()
