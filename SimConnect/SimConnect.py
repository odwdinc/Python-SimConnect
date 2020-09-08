from ctypes import *
from ctypes.wintypes import *
import logging
import time
from .Enum import *
from .Constants import *
from .Attributes import *

LOGGER = logging.getLogger(__name__)


def IsHR(hr, value):
	_hr = ctypes.HRESULT(hr)
	return ctypes.c_ulong(_hr.value).value == value


def millis():
	return int(round(time.time() * 1000))


class Event(object):

	def __call__(self, value=0):
		if self.event is None:
			self.event = self.sm.map_to_sim_event(self.deff)
		self.sm.send_event(self.event, DWORD(value))

	def __init__(self, _deff, _sm, _dec=''):
		self.deff = _deff
		self.event = None
		self.description = _dec
		self.sm = _sm


class Request(object):

	@property
	def value(self):
		if self._deff_test():
			self.sm.run()
			if (self.LastData + self.time) < millis():
				if self.sm.get_data(self):
					self.LastData = millis()
				else:
					return -999999
			return self.outData[self.name]
		else:
			return None

	@value.setter
	def value(self, val):
		if self._deff_test():
			self.outData[self.name] = val
			self.sm.set_data(self)
			self.sm.run()

	def __init__(self, _deff, _sm, _time=2000, _dec=None):
		self.DATA_DEFINITION_ID = None
		self.definitions = []
		self.description = _dec
		self.definitions.append(_deff)
		self.name = "_name"
		self.outData = {self.name: 0}
		self.sm = _sm
		self.time = _time
		self.defined = False
		self.LastData = 0
		if ':index' in str(self.definitions[0][0]):
			self.lastIndex = b':index'

	def setIndex(self, index):
		(dec, stype) = self.definitions[0]
		newindex = str(":" + str(index)).encode()
		dec = dec.replace(self.lastIndex, newindex)
		self.lastIndex = newindex
		self.definitions[0] = (dec, stype)
		self.redefine()

	def redefine(self):
		if self.DATA_DEFINITION_ID is not None:
			self.sm.dll.ClearDataDefinition(
				self.sm.hSimConnect,
				self.DATA_DEFINITION_ID.value,
			)
			self.defined = False
			self.sm.run()
		if self._deff_test():
			self.sm.run()
			self.sm.get_data(self)

	def _deff_test(self):
		if ':index' in str(self.definitions[0][0]):
			self.lastIndex = b':index'
			return False
		if self.defined is True:
			return True
		if self.DATA_DEFINITION_ID is None:
			(self.DATA_DEFINITION_ID, self.DATA_REQUEST_ID) = self.sm.new_request_id()
			self.sm.out_data[self.DATA_REQUEST_ID] = None
			self.sm.Requests.append(self)

		err = self.sm.dll.AddToDataDefinition(
			self.sm.hSimConnect,
			self.DATA_DEFINITION_ID.value,
			self.definitions[0][0],
			self.definitions[0][1],
			SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_FLOAT64,
			0,
			SIMCONNECT_UNUSED,
		)
		if IsHR(err, 0):
			self.defined = True
			return True
		else:
			LOGGER.error("SIM def" + str(self.definitions[0]))
			return False


class requestHolder:
	def __init__(self, _sm, _time=2000):
		self._sm = _sm
		self._time = _time
		self.dic = []

	def json(self):
		map = {}
		for att in self.dic:
			val = self.get(att)
			if val is not None:
				map[att] = val
		return map

	def add(self, name, _deff, _dec=''):
		self.dic.append(name)
		setattr(
			self,
			name,
			Request(_deff, self._sm, self._time, _dec)
		)

	def obj(self, _name):
		return getattr(self, _name)

	def get(self, _name, _dec=False):
		if _dec is True and getattr(self, _name).description is not None:
			return (getattr(self, _name).value, getattr(self, _name).description)
		return getattr(self, _name).value

	def set(self, _name, _value):
		temp = getattr(self, _name)
		setattr(temp, "value", _value)


class SimConnect:

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
					self.out_data[_request.DATA_REQUEST_ID] = cast(
						pObjData.dwData, POINTER(c_double * len(_request.definitions))
					).contents
		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_OPEN:
			LOGGER.info("SIM OPEN")
			self.ok = True
		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EXCEPTION:
			pass  # LOGGER.warn("ID EXCEPTION")
		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_QUIT:
			self.quit = 1
		else:
			LOGGER.debug("Received:", dwID)
		return

	def __init__(self, auto_connect=True, library_path="./SimConnect.dll"):

		self.Requests = []
		self.out_data = {}
		self.dll = SimConnectDll(library_path)
		self.hSimConnect = HANDLE()
		self.quit = 0
		self.ok = False
		self.my_dispatch_proc_rd = self.dll.DispatchProc(self.my_dispatch_proc)
		if auto_connect:
			self.connect()

	def connect(self):
		try:
			err = self.dll.Open(
				byref(self.hSimConnect), LPCSTR(b"Request Data"), None, 0, 0, 0
			)
			if IsHR(err, 0):
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
		if IsHR(err, 0):
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
		if IsHR(err, 0):
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
		if IsHR(err, 0):
			# LOGGER.debug("Event Sent")
			return True
		else:
			return False

	def new_request_id(self):
		name = "Request" + str(len(self.Requests))
		names = [m.name for m in self.dll.DATA_DEFINITION_ID] + [name]
		self.dll.DATA_DEFINITION_ID = Enum(self.dll.DATA_DEFINITION_ID.__name__, names)
		DEFINITION_ID = list(self.dll.DATA_DEFINITION_ID)[-1]

		names = [m.name for m in self.dll.DATA_REQUEST_ID] + [name]
		self.dll.DATA_REQUEST_ID = Enum(self.dll.DATA_REQUEST_ID.__name__, names)
		REQUEST_ID = list(self.dll.DATA_REQUEST_ID)[-1]

		return (DEFINITION_ID, REQUEST_ID)

	def new_request_holder(self, _time=2000):
		return requestHolder(self, _time)
