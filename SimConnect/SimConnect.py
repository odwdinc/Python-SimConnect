from ctypes import *
from ctypes.wintypes import *
import logging
import time
from .Enum import *
from .Constants import *

LOGGER = logging.getLogger(__name__)

SIMCONNECT_OBJECT_ID = DWORD


def IsHR(hr, value):
	_hr = ctypes.HRESULT(hr)
	return ctypes.c_ulong(_hr.value).value == value


def millis():
	return int(round(time.time() * 1000))


class sData(dict):
	__getattr__ = dict.__getitem__
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__


class Request:
	def __init__(
		self,
		_name,
		_time=None,
		_DATA_DEFINITION_ID=SIMCONNECT_DATA_DEFINITION_ID,
		_DATA_REQUEST_ID=SIMCONNECT_DATA_REQUEST_ID,
		_psc=None,
	):
		self.DATA_DEFINITION_ID = _DATA_DEFINITION_ID
		self.DATA_REQUEST_ID = _DATA_REQUEST_ID
		self.definitions = []
		self.time = _time
		self.timeout = millis()
		self.name = _name
		self.outData = {}
		self.psc = _psc
		self.psc.out_data[self.DATA_REQUEST_ID] = None

	def add(self, name, deff):
		self.definitions.append(deff)
		self.outData[name] = len(self.outData)
		self.psc.AddToDataDefinition(
			self.psc.hSimConnect,
			self.DATA_DEFINITION_ID.value,
			deff[0],
			deff[1],
			SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_FLOAT64,
			0,
			SIMCONNECT_UNUSED,
		)


class SimConnect:

	# TODO: update callbackfunction to expand functions.
	def my_dispatch_proc(self, pData, cbData, pContext):
		dwID = pData.contents.dwID
		self.pS = None
		if dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT:
			evt = cast(pData, POINTER(SIMCONNECT_RECV_EVENT))
			uEventID = evt.contents.uEventID
			if uEventID == self.EventID.EVENT_SIM_START:
				LOGGER.info("SIM START")

		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_SIMOBJECT_DATA_BYTYPE:
			pObjData = cast(
				pData, POINTER(SIMCONNECT_RECV_SIMOBJECT_DATA_BYTYPE)
			).contents
			dwRequestID = pObjData.dwRequestID
			for _request in self.Requests:
				if dwRequestID == _request.DATA_REQUEST_ID.value:
					self.out_data[_request.DATA_REQUEST_ID] = cast(
						pObjData.dwData, POINTER(c_double * 200)
					).contents
		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_OPEN:
			LOGGER.info("SIM OPEN")

		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_QUIT:
			self.quit = 1
		else:
			LOGGER.debug("Received:", dwID)
		return

	def __init__(self, auto_connect=True, library_path="./SimConnect.dll"):

		self.EventID = SIMCONNECT_CLIENT_EVENT_ID
		self.DATA_DEFINITION_ID = SIMCONNECT_DATA_DEFINITION_ID
		self.DATA_REQUEST_ID = SIMCONNECT_DATA_REQUEST_ID
		self.GROUP_ID = SIMCONNECT_NOTIFICATION_GROUP_ID
		self.INPUT_GROUP_ID = SIMCONNECT_INPUT_GROUP_ID
		self.CLIENT_DATA_ID = SIMCONNECT_CLIENT_DATA_ID
		self.CLIENT_DATA_DEFINITION_ID = SIMCONNECT_CLIENT_DATA_DEFINITION_ID

		self.Requests = []
		self.out_data = {}

		self.SimConnect = cdll.LoadLibrary(library_path)
		self.set_attributes()

		if auto_connect:
			self.connect()

	def set_attributes(self):
		# SIMCONNECTAPI SimConnect_Open(
		# 	HANDLE * phSimConnect,
		# 	LPCSTR szName,
		# 	HWND hWnd,
		# 	DWORD UserEventWin32,
		# 	HANDLE hEventHandle,
		# 	DWORD ConfigIndex)

		self.__Open = self.SimConnect.SimConnect_Open
		self.__Open.restype = HRESULT
		self.__Open.argtypes = [POINTER(HANDLE), LPCSTR, HWND, DWORD, HANDLE, DWORD]

		# SIMCONNECTAPI SimConnect_Close(
		# 	HANDLE hSimConnect);

		self.__Close = self.SimConnect.SimConnect_Close
		self.__Close.restype = HRESULT
		self.__Close.argtypes = [HANDLE]

		# SIMCONNECTAPI SimConnect_AddToDataDefinition(
		# 	HANDLE hSimConnect,
		# 	SIMCONNECT_DATA_DEFINITION_ID DefineID,
		# 	const char * DatumName,
		# 	const char * UnitsName,
		# 	SIMCONNECT_DATATYPE DatumType = SIMCONNECT_DATATYPE_FLOAT64,
		# 	float fEpsilon = 0,
		# 	DWORD DatumID = SIMCONNECT_UNUSED);

		self.AddToDataDefinition = self.SimConnect.SimConnect_AddToDataDefinition
		self.AddToDataDefinition.restype = HRESULT
		self.AddToDataDefinition.argtypes = [
			HANDLE,
			self.DATA_DEFINITION_ID,
			c_char_p,
			c_char_p,
			SIMCONNECT_DATATYPE,
			c_float,
			DWORD,
		]

		# SIMCONNECTAPI SimConnect_SubscribeToSystemEvent(
		# 	HANDLE hSimConnect,
		# 	SIMCONNECT_CLIENT_EVENT_ID EventID,
		# 	const char * SystemEventName);

		self.__SubscribeToSystemEvent = (
			self.SimConnect.SimConnect_SubscribeToSystemEvent
		)
		self.__SubscribeToSystemEvent.restype = HRESULT
		self.__SubscribeToSystemEvent.argtypes = [HANDLE, self.EventID, c_char_p]

		# SIMCONNECTAPI SimConnect_CallDispatch(
		# 	HANDLE hSimConnect,
		# 	DispatchProc pfcnDispatch,
		# 	void * pContext);

		DispatchProc = CFUNCTYPE(c_void_p, POINTER(SIMCONNECT_RECV), DWORD, c_void_p)

		self.__CallDispatch = self.SimConnect.SimConnect_CallDispatch
		self.__CallDispatch.restype = HRESULT
		self.__CallDispatch.argtypes = [HANDLE, DispatchProc, c_void_p]

		# SIMCONNECTAPI SimConnect_RequestDataOnSimObjectType(
		# 	HANDLE hSimConnect,
		# 	SIMCONNECT_DATA_REQUEST_ID RequestID,
		# 	SIMCONNECT_DATA_DEFINITION_ID DefineID,
		# 	DWORD dwRadiusMeters,
		# 	SIMCONNECT_SIMOBJECT_TYPE type);

		self.__RequestDataOnSimObjectType = (
			self.SimConnect.SimConnect_RequestDataOnSimObjectType
		)
		self.__RequestDataOnSimObjectType.restype = HRESULT
		self.__RequestDataOnSimObjectType.argtypes = [
			HANDLE,
			self.DATA_REQUEST_ID,
			self.DATA_DEFINITION_ID,
			DWORD,
			SIMCONNECT_SIMOBJECT_TYPE,
		]

		# SIMCONNECTAPI SimConnect_SetDataOnSimObject(
		# 	HANDLE hSimConnect,
		# 	SIMCONNECT_DATA_DEFINITION_ID DefineID,
		# 	SIMCONNECT_OBJECT_ID ObjectID,
		# 	SIMCONNECT_DATA_SET_FLAG Flags,
		# 	DWORD ArrayCount,
		# 	DWORD cbUnitSize,
		# 	void * pDataSet);

		# self.SetDataOnSimObject = self.SimConnect.SimConnect_SetDataOnSimObject
		# self.SetDataOnSimObject.restype = HRESULT
		# self.SetDataOnSimObject.argtypes = [HANDLE, DATA_DEFINE_ID, SIMCONNECT_OBJECT_ID, SIMCONNECT_DATA_SET_FLAG, DWORD, DWORD, ibbuf]

		# SIMCONNECTAPI SimConnect_TransmitClientEvent(
		# 	HANDLE hSimConnect,
		# 	SIMCONNECT_OBJECT_ID ObjectID,
		# 	SIMCONNECT_CLIENT_EVENT_ID EventID,
		# 	DWORD dwData,
		# 	SIMCONNECT_NOTIFICATION_GROUP_ID GroupID,
		# 	SIMCONNECT_EVENT_FLAG Flags);

		self.__TransmitClientEvent = self.SimConnect.SimConnect_TransmitClientEvent
		self.__TransmitClientEvent.restype = HRESULT
		self.__TransmitClientEvent.argtypes = [
			HANDLE,
			SIMCONNECT_OBJECT_ID,
			self.EventID,
			DWORD,
			DWORD,
			DWORD,
		]

		# SIMCONNECTAPI SimConnect_MapClientEventToSimEvent(
		# 	HANDLE hSimConnect,
		# 	SIMCONNECT_CLIENT_EVENT_ID EventID,
		# 	const char * EventName = "");

		self.__MapClientEventToSimEvent = (
			self.SimConnect.SimConnect_MapClientEventToSimEvent
		)
		self.__MapClientEventToSimEvent.restype = HRESULT
		self.__MapClientEventToSimEvent.argtypes = [HANDLE, self.EventID, c_char_p]

		# SIMCONNECTAPI SimConnect_AddClientEventToNotificationGroup(
		# 	HANDLE hSimConnect,
		# 	SIMCONNECT_NOTIFICATION_GROUP_ID GroupID,
		# 	SIMCONNECT_CLIENT_EVENT_ID EventID,
		# 	BOOL bMaskable = FALSE);

		self.__AddClientEventToNotificationGroup = (
			self.SimConnect.SimConnect_AddClientEventToNotificationGroup
		)
		self.__AddClientEventToNotificationGroup.restype = HRESULT
		self.__AddClientEventToNotificationGroup.argtypes = [
			HANDLE,
			self.GROUP_ID,
			self.EventID,
			c_bool,
		]

		# SIMCONNECTAPI SimConnect_SetSystemEventState(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   SIMCONNECT_STATE dwState);
		self.__SetSystemEventState = self.SimConnect.SimConnect_SetSystemEventState
		self.__SetSystemEventState.restype = HRESULT
		self.__SetSystemEventState.argtypes = [HANDLE, self.EventID, SIMCONNECT_STATE]

		# SIMCONNECTAPI SimConnect_AddClientEventToNotificationGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   BOOL bMaskable = FALSE);
		self.__AddClientEventToNotificationGroup = (
			self.SimConnect.SimConnect_AddClientEventToNotificationGroup
		)
		self.__AddClientEventToNotificationGroup.restype = HRESULT
		self.__AddClientEventToNotificationGroup.argtypes = [
			HANDLE,
			self.GROUP_ID,
			self.EventID,
			c_bool,
		]

		# SIMCONNECTAPI SimConnect_RemoveClientEvent(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   SIMCONNECT_CLIENT_EVENT_ID EventID);
		self.__RemoveClientEvent = self.SimConnect.SimConnect_RemoveClientEvent
		self.__RemoveClientEvent.restype = HRESULT
		self.__RemoveClientEvent.argtypes = [HANDLE, self.GROUP_ID, self.EventID]

		# SIMCONNECTAPI SimConnect_SetNotificationGroupPriority(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   DWORD uPriority);
		self.__SetNotificationGroupPriority = (
			self.SimConnect.SimConnect_SetNotificationGroupPriority
		)
		self.__SetNotificationGroupPriority.restype = HRESULT
		self.__SetNotificationGroupPriority.argtypes = [HANDLE, self.GROUP_ID, DWORD]

		# SIMCONNECTAPI SimConnect_ClearNotificationGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID);
		self.__ClearNotificationGroup = (
			self.SimConnect.SimConnect_ClearNotificationGroup
		)
		self.__ClearNotificationGroup.restype = HRESULT
		self.__ClearNotificationGroup.argtypes = [HANDLE, self.GROUP_ID]

		# SIMCONNECTAPI SimConnect_RequestNotificationGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   DWORD dwReserved = 0
		#   DWORD Flags = 0);
		self.__RequestNotificationGroup = (
			self.SimConnect.SimConnect_RequestNotificationGroup
		)
		self.__RequestNotificationGroup.restype = HRESULT
		self.__RequestNotificationGroup.argtypes = [HANDLE, self.GROUP_ID, DWORD, DWORD]

		# SIMCONNECTAPI SimConnect_ClearDataDefinition(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_DEFINITION_ID DefineID);
		self.__ClearDataDefinition = self.SimConnect.SimConnect_ClearDataDefinition
		self.__ClearDataDefinition.restype = HRESULT
		self.__ClearDataDefinition.argtypes = [HANDLE, self.DATA_DEFINITION_ID]

		# SIMCONNECTAPI SimConnect_RequestDataOnSimObject(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   SIMCONNECT_DATA_DEFINITION_ID DefineID
		#   SIMCONNECT_OBJECT_ID ObjectID
		#   SIMCONNECT_PERIOD Period
		#   SIMCONNECT_DATA_REQUEST_FLAG Flags = 0
		#   DWORD origin = 0
		#   DWORD interval = 0
		#   DWORD limit = 0);
		self.__RequestDataOnSimObject = (
			self.SimConnect.SimConnect_RequestDataOnSimObject
		)
		self.__RequestDataOnSimObject.restype = HRESULT
		self.__RequestDataOnSimObject.argtypes = [
			HANDLE,
			self.DATA_REQUEST_ID,
			self.DATA_DEFINITION_ID,
			SIMCONNECT_OBJECT_ID,
			SIMCONNECT_PERIOD,
			SIMCONNECT_DATA_REQUEST_FLAG,
			DWORD,
			DWORD,
			DWORD,
		]

		# SIMCONNECTAPI SimConnect_SetDataOnSimObject(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_DEFINITION_ID DefineID
		#   SIMCONNECT_OBJECT_ID ObjectID
		#   SIMCONNECT_DATA_SET_FLAG Flags
		#   DWORD ArrayCount
		#   DWORD cbUnitSize
		#   void * pDataSet);
		self.__SetDataOnSimObject = self.SimConnect.SimConnect_SetDataOnSimObject
		self.__SetDataOnSimObject.restype = HRESULT
		self.__SetDataOnSimObject.argtypes = [
			HANDLE,
			self.DATA_DEFINITION_ID,
			SIMCONNECT_OBJECT_ID,
			SIMCONNECT_DATA_SET_FLAG,
			DWORD,
			DWORD,
			c_void_p,
		]

		# SIMCONNECTAPI SimConnect_MapInputEventToClientEvent(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID
		#   const char * szInputDefinition
		#   SIMCONNECT_CLIENT_EVENT_ID DownEventID
		#   DWORD DownValue = 0
		#   SIMCONNECT_CLIENT_EVENT_ID UpEventID = (SIMCONNECT_CLIENT_EVENT_ID)SIMCONNECT_UNUSED
		#   DWORD UpValue = 0
		#   BOOL bMaskable = FALSE);
		self.__MapInputEventToClientEvent = (
			self.SimConnect.SimConnect_MapInputEventToClientEvent
		)
		self.__MapInputEventToClientEvent.restype = HRESULT
		self.__MapInputEventToClientEvent.argtypes = [
			HANDLE,
			self.INPUT_GROUP_ID,
			c_char_p,
			self.EventID,
			DWORD,
			self.EventID,
			DWORD,
			c_bool,
		]

		# SIMCONNECTAPI SimConnect_SetInputGroupPriority(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID
		#   DWORD uPriority);
		self.__SetInputGroupPriority = self.SimConnect.SimConnect_SetInputGroupPriority
		self.__SetInputGroupPriority.restype = HRESULT
		self.__SetInputGroupPriority.argtypes = [HANDLE, self.INPUT_GROUP_ID, DWORD]

		# SIMCONNECTAPI SimConnect_RemoveInputEvent(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID
		#   const char * szInputDefinition);
		self.__RemoveInputEvent = self.SimConnect.SimConnect_RemoveInputEvent
		self.__RemoveInputEvent.restype = HRESULT
		self.__RemoveInputEvent.argtypes = [HANDLE, self.INPUT_GROUP_ID, c_char_p]

		# SIMCONNECTAPI SimConnect_ClearInputGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID);
		self.__ClearInputGroup = self.SimConnect.SimConnect_ClearInputGroup
		self.__ClearInputGroup.restype = HRESULT
		self.__ClearInputGroup.argtypes = [HANDLE, self.INPUT_GROUP_ID]

		# SIMCONNECTAPI SimConnect_SetInputGroupState(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID
		#   DWORD dwState);
		self.__SetInputGroupState = self.SimConnect.SimConnect_SetInputGroupState
		self.__SetInputGroupState.restype = HRESULT
		self.__SetInputGroupState.argtypes = [HANDLE, self.INPUT_GROUP_ID, DWORD]

		# SIMCONNECTAPI SimConnect_RequestReservedKey(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   const char * szKeyChoice1 = ""
		#   const char * szKeyChoice2 = ""
		#   const char * szKeyChoice3 = "");
		self.__RequestReservedKey = self.SimConnect.SimConnect_RequestReservedKey
		self.__RequestReservedKey.restype = HRESULT
		self.__RequestReservedKey.argtypes = [
			HANDLE,
			self.EventID,
			c_char_p,
			c_char_p,
			c_char_p,
		]

		# SIMCONNECTAPI SimConnect_UnsubscribeFromSystemEvent(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID EventID);
		self.__UnsubscribeFromSystemEvent = (
			self.SimConnect.SimConnect_UnsubscribeFromSystemEvent
		)
		self.__UnsubscribeFromSystemEvent.restype = HRESULT
		self.__UnsubscribeFromSystemEvent.argtypes = [HANDLE, self.EventID]

		# SIMCONNECTAPI SimConnect_WeatherRequestInterpolatedObservation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   float lat
		#   float lon
		#   float alt);
		self.__WeatherRequestInterpolatedObservation = (
			self.SimConnect.SimConnect_WeatherRequestInterpolatedObservation
		)
		self.__WeatherRequestInterpolatedObservation.restype = HRESULT
		self.__WeatherRequestInterpolatedObservation.argtypes = [
			HANDLE,
			self.DATA_REQUEST_ID,
			c_float,
			c_float,
			c_float,
		]

		# SIMCONNECTAPI SimConnect_WeatherRequestObservationAtStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szICAO);
		self.__WeatherRequestObservationAtStation = (
			self.SimConnect.SimConnect_WeatherRequestObservationAtStation
		)
		self.__WeatherRequestObservationAtStation.restype = HRESULT
		self.__WeatherRequestObservationAtStation.argtypes = [
			HANDLE,
			self.DATA_REQUEST_ID,
			c_char_p,
		]

		# SIMCONNECTAPI SimConnect_WeatherRequestObservationAtNearestStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   float lat
		#   float lon);
		self.__WeatherRequestObservationAtNearestStation = (
			self.SimConnect.SimConnect_WeatherRequestObservationAtNearestStation
		)
		self.__WeatherRequestObservationAtNearestStation.restype = HRESULT
		self.__WeatherRequestObservationAtNearestStation.argtypes = [
			HANDLE,
			self.DATA_REQUEST_ID,
			c_float,
			c_float,
		]

		# SIMCONNECTAPI SimConnect_WeatherCreateStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szICAO
		#   const char * szName
		#   float lat
		#   float lon
		#   float alt);
		self.__WeatherCreateStation = self.SimConnect.SimConnect_WeatherCreateStation
		self.__WeatherCreateStation.restype = HRESULT
		self.__WeatherCreateStation.argtypes = [
			HANDLE,
			self.DATA_REQUEST_ID,
			c_char_p,
			c_char_p,
			c_float,
			c_float,
			c_float,
		]

		# SIMCONNECTAPI SimConnect_WeatherRemoveStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szICAO);
		self.__WeatherRemoveStation = self.SimConnect.SimConnect_WeatherRemoveStation
		self.__WeatherRemoveStation.restype = HRESULT
		self.__WeatherRemoveStation.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_char_p]

		# SIMCONNECTAPI SimConnect_WeatherSetObservation(
		#   HANDLE hSimConnect,
		#   DWORD Seconds
		#   const char * szMETAR);
		self.__WeatherSetObservation = self.SimConnect.SimConnect_WeatherSetObservation
		self.__WeatherSetObservation.restype = HRESULT
		self.__WeatherSetObservation.argtypes = [HANDLE, DWORD, c_char_p]

		# SIMCONNECTAPI SimConnect_WeatherSetModeServer(
		#   HANDLE hSimConnect,
		#   DWORD dwPort
		#   DWORD dwSeconds);
		self.__WeatherSetModeServer = self.SimConnect.SimConnect_WeatherSetModeServer
		self.__WeatherSetModeServer.restype = HRESULT
		self.__WeatherSetModeServer.argtypes = [HANDLE, DWORD, DWORD]

		# SIMCONNECTAPI SimConnect_WeatherSetModeTheme(
		#   HANDLE hSimConnect,
		#   const char * szThemeName);
		self.__WeatherSetModeTheme = self.SimConnect.SimConnect_WeatherSetModeTheme
		self.__WeatherSetModeTheme.restype = HRESULT
		self.__WeatherSetModeTheme.argtypes = [HANDLE, c_char_p]

		# SIMCONNECTAPI SimConnect_WeatherSetModeGlobal(
		#   HANDLE hSimConnect);
		self.__WeatherSetModeGlobal = self.SimConnect.SimConnect_WeatherSetModeGlobal
		self.__WeatherSetModeGlobal.restype = HRESULT
		self.__WeatherSetModeGlobal.argtypes = [HANDLE]

		# SIMCONNECTAPI SimConnect_WeatherSetModeCustom(
		#   HANDLE hSimConnect);
		self.__WeatherSetModeCustom = self.SimConnect.SimConnect_WeatherSetModeCustom
		self.__WeatherSetModeCustom.restype = HRESULT
		self.__WeatherSetModeCustom.argtypes = [HANDLE]

		# SIMCONNECTAPI SimConnect_WeatherSetDynamicUpdateRate(
		#   HANDLE hSimConnect,
		#   DWORD dwRate);
		self.__WeatherSetDynamicUpdateRate = (
			self.SimConnect.SimConnect_WeatherSetDynamicUpdateRate
		)
		self.__WeatherSetDynamicUpdateRate.restype = HRESULT
		self.__WeatherSetDynamicUpdateRate.argtypes = [HANDLE, DWORD]

		# SIMCONNECTAPI SimConnect_WeatherRequestCloudState(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   float minLat
		#   float minLon
		#   float minAlt
		#   float maxLat
		#   float maxLon
		#   float maxAlt
		#   DWORD dwFlags = 0);
		self.__WeatherRequestCloudState = (
			self.SimConnect.SimConnect_WeatherRequestCloudState
		)
		self.__WeatherRequestCloudState.restype = HRESULT
		self.__WeatherRequestCloudState.argtypes = [
			HANDLE,
			self.DATA_REQUEST_ID,
			c_float,
			c_float,
			c_float,
			c_float,
			c_float,
			c_float,
			DWORD,
		]

		# SIMCONNECTAPI SimConnect_WeatherCreateThermal(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   float lat
		#   float lon
		#   float alt
		#   float radius
		#   float height
		#   float coreRate = 3.0f
		#   float coreTurbulence = 0.05f
		#   float sinkRate = 3.0f
		#   float sinkTurbulence = 0.2f
		#   float coreSize = 0.4f
		#   float coreTransitionSize = 0.1f
		#   float sinkLayerSize = 0.4f
		#   float sinkTransitionSize = 0.1f);
		self.__WeatherCreateThermal = self.SimConnect.SimConnect_WeatherCreateThermal
		self.__WeatherCreateThermal.restype = HRESULT
		self.__WeatherCreateThermal.argtypes = [
			HANDLE,
			self.DATA_REQUEST_ID,
			c_float,
			c_float,
			c_float,
			c_float,
			c_float,
			c_float,
			c_float,
			c_float,
			c_float,
			c_float,
			c_float,
			c_float,
			c_float,
		]

		# SIMCONNECTAPI SimConnect_WeatherRemoveThermal(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID);
		self.__WeatherRemoveThermal = self.SimConnect.SimConnect_WeatherRemoveThermal
		self.__WeatherRemoveThermal.restype = HRESULT
		self.__WeatherRemoveThermal.argtypes = [HANDLE, SIMCONNECT_OBJECT_ID]

		# SIMCONNECTAPI SimConnect_AICreateParkedATCAircraft(
		#   HANDLE hSimConnect,
		#   const char * szContainerTitle
		#   const char * szTailNumber
		#   const char * szAirportID
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__AICreateParkedATCAircraft = (
			self.SimConnect.SimConnect_AICreateParkedATCAircraft
		)
		self.__AICreateParkedATCAircraft.restype = HRESULT
		self.__AICreateParkedATCAircraft.argtypes = [
			HANDLE,
			c_char_p,
			c_char_p,
			c_char_p,
			self.DATA_REQUEST_ID,
		]

		# SIMCONNECTAPI SimConnect_AICreateEnrouteATCAircraft(
		#   HANDLE hSimConnect,
		#   const char * szContainerTitle
		#   const char * szTailNumber
		#   int iFlightNumber
		#   const char * szFlightPlanPath
		#   double dFlightPlanPosition
		#   BOOL bTouchAndGo
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__AICreateEnrouteATCAircraft = (
			self.SimConnect.SimConnect_AICreateEnrouteATCAircraft
		)
		self.__AICreateEnrouteATCAircraft.restype = HRESULT
		self.__AICreateEnrouteATCAircraft.argtypes = [
			HANDLE,
			c_char_p,
			c_char_p,
			c_int,
			c_char_p,
			c_double,
			c_bool,
			self.DATA_REQUEST_ID,
		]

		# SIMCONNECTAPI SimConnect_AICreateNonATCAircraft(
		#   HANDLE hSimConnect,
		#   const char * szContainerTitle
		#   const char * szTailNumber
		#   SIMCONNECT_DATA_INITPOSITION InitPos
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__AICreateNonATCAircraft = (
			self.SimConnect.SimConnect_AICreateNonATCAircraft
		)
		self.__AICreateNonATCAircraft.restype = HRESULT
		self.__AICreateNonATCAircraft.argtypes = [
			HANDLE,
			c_double,
			c_double,
			SIMCONNECT_DATA_INITPOSITION,
			self.DATA_REQUEST_ID,
		]

		# SIMCONNECTAPI SimConnect_AICreateSimulatedObject(
		#   HANDLE hSimConnect,
		#   const char * szContainerTitle
		#   SIMCONNECT_DATA_INITPOSITION InitPos
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__AICreateSimulatedObject = (
			self.SimConnect.SimConnect_AICreateSimulatedObject
		)
		self.__AICreateSimulatedObject.restype = HRESULT
		self.__AICreateSimulatedObject.argtypes = [
			HANDLE,
			c_char_p,
			SIMCONNECT_DATA_INITPOSITION,
			self.DATA_REQUEST_ID,
		]

		# SIMCONNECTAPI SimConnect_AIReleaseControl(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__AIReleaseControl = self.SimConnect.SimConnect_AIReleaseControl
		self.__AIReleaseControl.restype = HRESULT
		self.__AIReleaseControl.argtypes = [
			HANDLE,
			SIMCONNECT_OBJECT_ID,
			self.DATA_REQUEST_ID,
		]

		# SIMCONNECTAPI SimConnect_AIRemoveObject(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__AIRemoveObject = self.SimConnect.SimConnect_AIRemoveObject
		self.__AIRemoveObject.restype = HRESULT
		self.__AIRemoveObject.argtypes = [
			HANDLE,
			SIMCONNECT_OBJECT_ID,
			self.DATA_REQUEST_ID,
		]

		# SIMCONNECTAPI SimConnect_AISetAircraftFlightPlan(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID
		#   const char * szFlightPlanPath
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__AISetAircraftFlightPlan = (
			self.SimConnect.SimConnect_AISetAircraftFlightPlan
		)
		self.__AISetAircraftFlightPlan.restype = HRESULT
		self.__AISetAircraftFlightPlan.argtypes = [
			HANDLE,
			SIMCONNECT_OBJECT_ID,
			c_char_p,
			self.DATA_REQUEST_ID,
		]

		# SIMCONNECTAPI SimConnect_ExecuteMissionAction(
		#   HANDLE hSimConnect,
		#   const GUID guidInstanceId);
		self.__ExecuteMissionAction = self.SimConnect.SimConnect_ExecuteMissionAction
		self.__ExecuteMissionAction.restype = HRESULT
		self.__ExecuteMissionAction.argtypes = []

		# SIMCONNECTAPI SimConnect_CompleteCustomMissionAction(
		#   HANDLE hSimConnect,
		#   const GUID guidInstanceId);
		self.__CompleteCustomMissionAction = (
			self.SimConnect.SimConnect_CompleteCustomMissionAction
		)
		self.__CompleteCustomMissionAction.restype = HRESULT
		self.__CompleteCustomMissionAction.argtypes = []

		# SIMCONNECTAPI SimConnect_RetrieveString(
		#   SIMCONNECT_RECV * pData,
		#   DWORD cbData
		#   void * pStringV
		#   char ** pszString
		#   DWORD * pcbString);
		self.__RetrieveString = self.SimConnect.SimConnect_RetrieveString
		self.__RetrieveString.restype = HRESULT
		self.__RetrieveString.argtypes = []

		# SIMCONNECTAPI SimConnect_GetLastSentPacketID(
		#   HANDLE hSimConnect,
		#   DWORD * pdwError);
		self.__GetLastSentPacketID = self.SimConnect.SimConnect_GetLastSentPacketID
		self.__GetLastSentPacketID.restype = HRESULT
		self.__GetLastSentPacketID.argtypes = [HANDLE, DWORD]

		# SIMCONNECTAPI SimConnect_GetNextDispatch(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_RECV ** ppData
		#   DWORD * pcbData);
		self.__GetNextDispatch = self.SimConnect.SimConnect_GetNextDispatch
		self.__GetNextDispatch.restype = HRESULT
		self.__GetNextDispatch.argtypes = []

		# SIMCONNECTAPI SimConnect_RequestResponseTimes(
		#   HANDLE hSimConnect,
		#   DWORD nCount
		#   float * fElapsedSeconds);
		self.__RequestResponseTimes = self.SimConnect.SimConnect_RequestResponseTimes
		self.__RequestResponseTimes.restype = HRESULT
		self.__RequestResponseTimes.argtypes = [HANDLE, DWORD, c_float]

		# SIMCONNECTAPI SimConnect_InsertString(
		#   char * pDest,
		#   DWORD cbDest
		#   void ** ppEnd
		#   DWORD * pcbStringV
		#   const char * pSource);
		self.__InsertString = self.SimConnect.SimConnect_InsertString
		self.__InsertString.restype = HRESULT
		self.__InsertString.argtypes = []

		# SIMCONNECTAPI SimConnect_CameraSetRelative6DOF(
		#   HANDLE hSimConnect,
		#   float fDeltaX
		#   float fDeltaY
		#   float fDeltaZ
		#   float fPitchDeg
		#   float fBankDeg
		#   float fHeadingDeg);
		self.__CameraSetRelative6DOF = self.SimConnect.SimConnect_CameraSetRelative6DOF
		self.__CameraSetRelative6DOF.restype = HRESULT
		self.__CameraSetRelative6DOF.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuAddItem(
		#   HANDLE hSimConnect,
		#   const char * szMenuItem
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID
		#   DWORD dwData);
		self.__MenuAddItem = self.SimConnect.SimConnect_MenuAddItem
		self.__MenuAddItem.restype = HRESULT
		self.__MenuAddItem.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuDeleteItem(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID);
		self.__MenuDeleteItem = self.SimConnect.SimConnect_MenuDeleteItem
		self.__MenuDeleteItem.restype = HRESULT
		self.__MenuDeleteItem.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuAddSubItem(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID
		#   const char * szMenuItem
		#   SIMCONNECT_CLIENT_EVENT_ID SubMenuEventID
		#   DWORD dwData);
		self.__MenuAddSubItem = self.SimConnect.SimConnect_MenuAddSubItem
		self.__MenuAddSubItem.restype = HRESULT
		self.__MenuAddSubItem.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuDeleteSubItem(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID
		#   const SIMCONNECT_CLIENT_EVENT_ID SubMenuEventID);
		self.__MenuDeleteSubItem = self.SimConnect.SimConnect_MenuDeleteSubItem
		self.__MenuDeleteSubItem.restype = HRESULT
		self.__MenuDeleteSubItem.argtypes = []

		# SIMCONNECTAPI SimConnect_RequestSystemState(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szState);
		self.__RequestSystemState = self.SimConnect.SimConnect_RequestSystemState
		self.__RequestSystemState.restype = HRESULT
		self.__RequestSystemState.argtypes = []

		# SIMCONNECTAPI SimConnect_SetSystemState(
		#   HANDLE hSimConnect,
		#   const char * szState
		#   DWORD dwInteger
		#   float fFloat
		#   const char * szString);
		self.__SetSystemState = self.SimConnect.SimConnect_SetSystemState
		self.__SetSystemState.restype = HRESULT
		self.__SetSystemState.argtypes = []

		# SIMCONNECTAPI SimConnect_MapClientDataNameToID(
		#   HANDLE hSimConnect,
		#   const char * szClientDataName
		#   SIMCONNECT_CLIENT_DATA_ID ClientDataID);
		self.__MapClientDataNameToID = self.SimConnect.SimConnect_MapClientDataNameToID
		self.__MapClientDataNameToID.restype = HRESULT
		self.__MapClientDataNameToID.argtypes = []

		# SIMCONNECTAPI SimConnect_CreateClientData(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_ID ClientDataID
		#   DWORD dwSize
		#   SIMCONNECT_CREATE_CLIENT_DATA_FLAG Flags);
		self.__CreateClientData = self.SimConnect.SimConnect_CreateClientData
		self.__CreateClientData.restype = HRESULT
		self.__CreateClientData.argtypes = [
			HANDLE,
			self.CLIENT_DATA_ID,
			DWORD,
			SIMCONNECT_CREATE_CLIENT_DATA_FLAG,
		]

		# SIMCONNECTAPI SimConnect_AddToClientDataDefinition(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_DEFINITION_ID DefineID
		#   DWORD dwOffset
		#   DWORD dwSizeOrType
		#   float fEpsilon = 0
		#   DWORD DatumID = SIMCONNECT_UNUSED);
		self.__AddToClientDataDefinition = (
			self.SimConnect.SimConnect_AddToClientDataDefinition
		)
		self.__AddToClientDataDefinition.restype = HRESULT
		self.__AddToClientDataDefinition.argtypes = [
			HANDLE,
			self.CLIENT_DATA_DEFINITION_ID,
			DWORD,
			DWORD,
			c_float,
			DWORD,
		]

		# SIMCONNECTAPI SimConnect_ClearClientDataDefinition(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_DEFINITION_ID DefineID);
		self.__ClearClientDataDefinition = (
			self.SimConnect.SimConnect_ClearClientDataDefinition
		)
		self.__ClearClientDataDefinition.restype = HRESULT
		self.__ClearClientDataDefinition.argtypes = [
			HANDLE,
			self.CLIENT_DATA_DEFINITION_ID,
		]

		# SIMCONNECTAPI SimConnect_RequestClientData(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_ID ClientDataID
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   SIMCONNECT_CLIENT_DATA_DEFINITION_ID DefineID
		#   SIMCONNECT_CLIENT_DATA_PERIOD Period = SIMCONNECT_CLIENT_DATA_PERIOD_ONCE
		#   SIMCONNECT_CLIENT_DATA_REQUEST_FLAG Flags = 0
		#   DWORD origin = 0
		#   DWORD interval = 0
		#   DWORD limit = 0);
		self.__RequestClientData = self.SimConnect.SimConnect_RequestClientData
		self.__RequestClientData.restype = HRESULT
		self.__RequestClientData.argtypes = [
			HANDLE,
			self.CLIENT_DATA_ID,
			self.DATA_REQUEST_ID,
			self.CLIENT_DATA_DEFINITION_ID,
			SIMCONNECT_CLIENT_DATA_PERIOD,
			SIMCONNECT_CLIENT_DATA_REQUEST_FLAG,
			DWORD,
			DWORD,
			DWORD,
		]

		# SIMCONNECTAPI SimConnect_SetClientData(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_ID ClientDataID
		#   SIMCONNECT_CLIENT_DATA_DEFINITION_ID DefineID
		#   SIMCONNECT_CLIENT_DATA_SET_FLAG Flags
		#   DWORD dwReserved
		#   DWORD cbUnitSize
		#   void * pDataSet);
		self.__SetClientData = self.SimConnect.SimConnect_SetClientData
		self.__SetClientData.restype = HRESULT
		self.__SetClientData.argtypes = [
			HANDLE,
			self.CLIENT_DATA_ID,
			self.CLIENT_DATA_DEFINITION_ID,
			SIMCONNECT_CLIENT_DATA_SET_FLAG,
			DWORD,
			DWORD,
			c_void_p,
		]

		# SIMCONNECTAPI SimConnect_FlightLoad(
		#   HANDLE hSimConnect,
		#   const char * szFileName);
		self.__FlightLoad = self.SimConnect.SimConnect_FlightLoad
		self.__FlightLoad.restype = HRESULT
		self.__FlightLoad.argtypes = [HANDLE, c_char_p]

		# SIMCONNECTAPI SimConnect_FlightSave(
		#   HANDLE hSimConnect,
		#   const char * szFileName
		#   const char * szTitle
		#   const char * szDescription
		#   DWORD Flags);
		self.__FlightSave = self.SimConnect.SimConnect_FlightSave
		self.__FlightSave.restype = HRESULT
		self.__FlightSave.argtypes = [HANDLE, c_char_p, c_char_p, c_char_p, DWORD]

		# SIMCONNECTAPI SimConnect_FlightPlanLoad(
		#   HANDLE hSimConnect,
		#   const char * szFileName);
		self.__FlightPlanLoad = self.SimConnect.SimConnect_FlightPlanLoad
		self.__FlightPlanLoad.restype = HRESULT
		self.__FlightPlanLoad.argtypes = [HANDLE, c_char_p]

		# SIMCONNECTAPI SimConnect_Text(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_TEXT_TYPE type
		#   float fTimeSeconds
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   DWORD cbUnitSize
		#   void * pDataSet);
		self.__Text = self.SimConnect.SimConnect_Text
		self.__Text.restype = HRESULT
		self.__Text.argtypes = [
			HANDLE,
			SIMCONNECT_TEXT_TYPE,
			c_float,
			self.EventID,
			DWORD,
			c_void_p,
		]

		# SIMCONNECTAPI SimConnect_SubscribeToFacilities(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_FACILITY_LIST_TYPE type
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__SubscribeToFacilities = self.SimConnect.SimConnect_SubscribeToFacilities
		self.__SubscribeToFacilities.restype = HRESULT
		self.__SubscribeToFacilities.argtypes = [
			HANDLE,
			SIMCONNECT_FACILITY_LIST_TYPE,
			self.DATA_REQUEST_ID,
		]

		# SIMCONNECTAPI SimConnect_UnsubscribeToFacilities(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_FACILITY_LIST_TYPE type);
		self.__UnsubscribeToFacilities = (
			self.SimConnect.SimConnect_UnsubscribeToFacilities
		)
		self.__UnsubscribeToFacilities.restype = HRESULT
		self.__UnsubscribeToFacilities.argtypes = [
			HANDLE,
			SIMCONNECT_FACILITY_LIST_TYPE,
		]

		# SIMCONNECTAPI SimConnect_RequestFacilitiesList(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_FACILITY_LIST_TYPE type
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.____RequestFacilitiesList = (
			self.SimConnect.SimConnect_RequestFacilitiesList
		)
		self.____RequestFacilitiesList.restype = HRESULT
		self.____RequestFacilitiesList.argtypes = [
			HANDLE,
			SIMCONNECT_FACILITY_LIST_TYPE,
			self.DATA_REQUEST_ID,
		]

		self.hSimConnect = HANDLE()
		self.quit = 0
		self.my_dispatch_proc_rd = DispatchProc(self.my_dispatch_proc)
		# self.haveData = False

	def connect(self):
		try:
			err = self.__Open(
				byref(self.hSimConnect), LPCSTR(b"Request Data"), None, 0, 0, 0
			)
			if IsHR(err, 0):
				LOGGER.debug("Connected to Flight Simulator!")
				# Set up the data definition, but do not yet do anything with itd
				# Request an event when the simulation starts
				self.__SubscribeToSystemEvent(
					self.hSimConnect, self.EventID.EVENT_SIM_START, b"SimStart"
				)
		except OSError:
			LOGGER.debug("Did not find Flight Simulator running.")
			exit(0)

	def run(self):
		for _request in self.Requests:
			self.out_data[_request.DATA_REQUEST_ID] = None
			if _request.time is not None:
				if (_request.timeout + _request.time) < millis():
					self.request_data(_request)
					_request.timeout = millis()

		self.__CallDispatch(self.hSimConnect, self.my_dispatch_proc_rd, None)

	def exit(self):
		self.__Close(self.hSimConnect)

	def map_to_sim_event(self, name):
		for m in self.EventID:
			if name.decode() == m.name:
				LOGGER.debug("Already have event: ", m)
				return m

		names = [m.name for m in self.EventID] + [name.decode()]
		self.EventID = Enum(self.EventID.__name__, names)
		evnt = list(self.EventID)[-1]
		err = self.__MapClientEventToSimEvent(self.hSimConnect, evnt.value, name)
		if IsHR(err, 0):
			return evnt
		else:
			LOGGER.error("Error: MapToSimEvent")
			return None

	def add_to_notification_group(self, group, evnt, bMaskable=False):
		self.__AddClientEventToNotificationGroup(
			self.hSimConnect, group, evnt, bMaskable
		)

	def request_data(self, _Request):
		self.out_data[_Request.DATA_REQUEST_ID] = None
		self.__RequestDataOnSimObjectType(
			self.hSimConnect,
			_Request.DATA_REQUEST_ID.value,
			_Request.DATA_DEFINITION_ID.value,
			0,
			SIMCONNECT_SIMOBJECT_TYPE.SIMCONNECT_SIMOBJECT_TYPE_USER,
		)

	def get_data(self, _Request, _format=False):
		if self.out_data[_Request.DATA_REQUEST_ID] is None:
			return None
		if _format:
			map = {}
		else:
			map = sData
		for od in _Request.outData:
			if _format:
				map[od] = self.out_data[_Request.DATA_REQUEST_ID][_Request.outData[od]]
			else:
				setattr(
					sData,
					od,
					self.out_data[_Request.DATA_REQUEST_ID][_Request.outData[od]],
				)
		return map

	def send_data(self, evnt, data=DWORD(0)):
		err = self.__TransmitClientEvent(
			self.hSimConnect,
			SIMCONNECT_OBJECT_ID_USER,
			evnt.value,
			data,
			SIMCONNECT_GROUP_PRIORITY_HIGHEST,
			DWORD(16),
		)
		if IsHR(err, 0):
			LOGGER.debug("Event Sent")
			return True
		else:
			return False

	def new_request(self, time=None):
		name = "Request" + str(len(self.Requests))
		names = [m.name for m in self.DATA_DEFINITION_ID] + [name]
		self.DATA_DEFINITION_ID = Enum(self.DATA_DEFINITION_ID.__name__, names)
		DEFINITION_ID = list(self.DATA_DEFINITION_ID)[-1]

		names = [m.name for m in self.DATA_REQUEST_ID] + [name]
		self.DATA_REQUEST_ID = Enum(self.DATA_REQUEST_ID.__name__, names)
		REQUEST_ID = list(self.DATA_REQUEST_ID)[-1]

		_Request = Request(
			_DATA_DEFINITION_ID=DEFINITION_ID,
			_DATA_REQUEST_ID=REQUEST_ID,
			_time=time,
			_name=name,
			_psc=self,
		)
		self.Requests.append(_Request)
		return _Request
