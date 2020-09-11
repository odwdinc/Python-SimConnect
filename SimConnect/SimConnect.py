from ctypes import *
from ctypes.wintypes import *
import logging
import time
from .Enum import *
from .Constants import *
from .Attributes import *
import os
_library_path = os.path.abspath(__file__).replace(".py", ".dll")

LOGGER = logging.getLogger(__name__)


def millis():
	return int(round(time.time() * 1000))


class SimConnect:

	def IsHR(self, hr, value):
		_hr = ctypes.HRESULT(hr)
		return ctypes.c_ulong(_hr.value).value == value

	# TODO: update callbackfunction to expand functions.
	def my_dispatch_proc(self, pData, cbData, pContext):
		dwID = pData.contents.dwID
		self.pS = None
		if dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT:
			evt = cast(pData, POINTER(SIMCONNECT_RECV_EVENT))
			uEventID = evt.contents.uEventID
			if uEventID == self.dll.EventID.EVENT_SIM_START:
				LOGGER.info("SIM START")

		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_SIMOBJECT_DATA_BYTYPE:
			pObjData = cast(
				pData, POINTER(SIMCONNECT_RECV_SIMOBJECT_DATA_BYTYPE)
			).contents
			dwRequestID = pObjData.dwRequestID
			for _request in self.Requests:
				if dwRequestID == _request.DATA_REQUEST_ID.value:
					# print(_request.definitions[0][1])
					rtype = _request.definitions[0][1].decode()
					if 'String' in rtype or 'string' in rtype:
						pS = cast(pObjData.dwData, c_char_p)
						self.out_data[_request.DATA_REQUEST_ID] = [pS.value]
						# self.dll.RetrieveString(pObjData.dwData, cbData, strings, &pszTitle;, &cbTitle;)
					else:
						self.out_data[_request.DATA_REQUEST_ID] = cast(
							pObjData.dwData, POINTER(c_double * len(_request.definitions))
						).contents
		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_OPEN:
			LOGGER.info("SIM OPEN")
			self.ok = True
		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EXCEPTION:
			LOGGER.warn("ID EXCEPTION")
		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_QUIT:
			self.quit = 1
		else:
			LOGGER.debug("Received:", dwID)
		return

	def __init__(self, auto_connect=True, library_path=_library_path):

		self.Requests = []
		self.out_data = {}
		self.dll = SimConnectDll(library_path)
		self.hSimConnect = HANDLE()
		self.quit = 0
		self.ok = False
		self.DEFINITION_POS = None
		self.my_dispatch_proc_rd = self.dll.DispatchProc(self.my_dispatch_proc)
		if auto_connect:
			self.connect()

	def connect(self):
		try:
			err = self.dll.Open(
				byref(self.hSimConnect), LPCSTR(b"Request Data"), None, 0, 0, 0
			)
			if self.IsHR(err, 0):
				LOGGER.debug("Connected to Flight Simulator!")
				# Set up the data definition, but do not yet do anything with itd
				# Request an event when the simulation starts
				self.dll.SubscribeToSystemEvent(
					self.hSimConnect, self.dll.EventID.EVENT_SIM_START, b"SimStart"
				)
				while self.ok is False:
					self.run()
		except OSError:
			LOGGER.debug("Did not find Flight Simulator running.")
			exit(0)

	def run(self):
		time.sleep(.01)
		self.dll.CallDispatch(self.hSimConnect, self.my_dispatch_proc_rd, None)

	def exit(self):
		self.dll.Close(self.hSimConnect)

	def map_to_sim_event(self, name):
		for m in self.dll.EventID:
			if name.decode() == m.name:
				LOGGER.debug("Already have event: ", m)
				return m

		names = [m.name for m in self.dll.EventID] + [name.decode()]
		self.dll.EventID = Enum(self.dll.EventID.__name__, names)
		evnt = list(self.dll.EventID)[-1]
		err = self.dll.MapClientEventToSimEvent(self.hSimConnect, evnt.value, name)
		if self.IsHR(err, 0):
			return evnt
		else:
			LOGGER.error("Error: MapToSimEvent")
			return None

	def add_to_notification_group(self, group, evnt, bMaskable=False):
		self.dll.AddClientEventToNotificationGroup(
			self.hSimConnect, group, evnt, bMaskable
		)

	def request_data(self, _Request):
		self.out_data[_Request.DATA_REQUEST_ID] = None
		self.dll.RequestDataOnSimObjectType(
			self.hSimConnect,
			_Request.DATA_REQUEST_ID.value,
			_Request.DATA_DEFINITION_ID.value,
			0,
			SIMCONNECT_SIMOBJECT_TYPE.SIMCONNECT_SIMOBJECT_TYPE_USER,
		)

	def set_data(self, _Request):
		_data = _Request.outData
		pyarr = list(_data.values())
		dataarray = (ctypes.c_double * len(pyarr))(*pyarr)
		pObjData = cast(
			dataarray, c_void_p
		)
		err = self.dll.SetDataOnSimObject(
			self.hSimConnect,
			_Request.DATA_DEFINITION_ID.value,
			SIMCONNECT_SIMOBJECT_TYPE.SIMCONNECT_SIMOBJECT_TYPE_USER,
			0,
			0,
			sizeof(ctypes.c_double) * len(pyarr),
			pObjData
		)
		if self.IsHR(err, 0):
			# LOGGER.debug("Request Sent")
			return True
		else:
			return False

	def get_data(self, _Request):
		self.request_data(_Request)
		self.run()
		attemps = 0
		while self.out_data[_Request.DATA_REQUEST_ID] is None and attemps < 4:
			self.run()
			attemps += 1

		if self.out_data[_Request.DATA_REQUEST_ID] is None:
			return False

		newData = self.out_data[_Request.DATA_REQUEST_ID]
		for od in _Request.outData:
			index = list(_Request.outData.keys()).index(od)
			_Request.outData[od] = newData[index]
		self.out_data[_Request.DATA_REQUEST_ID] = None
		return True

	def send_event(self, evnt, data=DWORD(0)):
		err = self.dll.TransmitClientEvent(
			self.hSimConnect,
			SIMCONNECT_OBJECT_ID_USER,
			evnt.value,
			data,
			SIMCONNECT_GROUP_PRIORITY_HIGHEST,
			DWORD(16),
		)
		if self.IsHR(err, 0):
			# LOGGER.debug("Event Sent")
			return True
		else:
			return False

	def new_def_id(self, _name):
		names = [m.name for m in self.dll.DATA_DEFINITION_ID] + [_name]
		self.dll.DATA_DEFINITION_ID = Enum(self.dll.DATA_DEFINITION_ID.__name__, names)
		return list(self.dll.DATA_DEFINITION_ID)[-1]

	def new_request_id(self):
		name = "Request" + str(len(self.Requests))
		DEFINITION_ID = self.new_def_id(name)

		names = [m.name for m in self.dll.DATA_REQUEST_ID] + [name]
		self.dll.DATA_REQUEST_ID = Enum(self.dll.DATA_REQUEST_ID.__name__, names)
		REQUEST_ID = list(self.dll.DATA_REQUEST_ID)[-1]

		return (DEFINITION_ID, REQUEST_ID)

	def set_pos(
		self,
		_Altitude,
		_Latitude,
		_Longitude,
		_Airspeed,
		_Pitch=0.0,
		_Bank=0.0,
		_Heading=0,
		_OnGround=0,
	):
		Init = SIMCONNECT_DATA_INITPOSITION()
		Init.Altitude = _Altitude
		Init.Latitude = _Latitude
		Init.Longitude = _Longitude
		Init.Pitch = _Pitch
		Init.Bank = _Bank
		Init.Heading = _Heading
		Init.OnGround = _OnGround
		Init.Airspeed = _Airspeed

		if self.DEFINITION_POS is None:
			self.DEFINITION_POS = self.new_def_id("DEFINITION_POS")
			err = self.dll.AddToDataDefinition(
				self.hSimConnect,
				self.DEFINITION_POS.value,
				b'Initial Position',
				b'',
				SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_INITPOSITION,
				0,
				SIMCONNECT_UNUSED,
			)

		hr = self.dll.SetDataOnSimObject(
			self.hSimConnect,
			self.DEFINITION_POS.value,
			SIMCONNECT_OBJECT_ID_USER,
			0,
			0,
			sizeof(Init),
			pointer(Init)
		)
		if self.IsHR(err, 0):
			return True
		else:
			return False
