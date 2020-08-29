from ctypes import *
from ctypes.wintypes import *
from enum import IntEnum, Enum, auto
import time


SIMCONNECT_OBJECT_ID = DWORD

#//----------------------------------------------------------------------------
#//        Constants
#//----------------------------------------------------------------------------

DWORD_MAX = DWORD(0xFFFFFFFF)
SIMCONNECT_UNUSED = DWORD_MAX
SIMCONNECT_OBJECT_ID_USER = DWORD(0)  	# proxy value for User vehicle ObjectID
SIMCONNECT_UNUSED = DWORD_MAX			# special value to indicate unused event, ID
SIMCONNECT_OBJECT_ID_USER = DWORD(0)  	# proxy value for User vehicle ObjectID

SIMCONNECT_CAMERA_IGNORE_FIELD = c_float(-1)  # Used to tell the Camera API to NOT modify the value in this part of the argument.

SIMCONNECT_CLIENTDATA_MAX_SIZE = DWORD(8192)  # maximum value for SimConnect_CreateClientData dwSize parameter


# Notification Group priority values
SIMCONNECT_GROUP_PRIORITY_HIGHEST = DWORD(1)  					# highest priority
SIMCONNECT_GROUP_PRIORITY_HIGHEST_MASKABLE = DWORD(10000000)  	# highest priority that allows events to be masked
SIMCONNECT_GROUP_PRIORITY_STANDARD = DWORD(1900000000) 			# standard priority
SIMCONNECT_GROUP_PRIORITY_DEFAULT = DWORD(2000000000) 			# default priority
SIMCONNECT_GROUP_PRIORITY_LOWEST = DWORD(4000000000) 			# priorities lower than this will be ignored

#Weather observations Metar strings
MAX_METAR_LENGTH = DWORD(2000)

# Maximum thermal size is 100 km.
MAX_THERMAL_SIZE = c_float(100000)
MAX_THERMAL_RATE = c_float(1000)

# SIMCONNECT_DATA_INITPOSITION.Airspeed
INITPOSITION_AIRSPEED_CRUISE = DWORD(-1) 	# aircraft's cruise airspeed
INITPOSITION_AIRSPEED_KEEP = DWORD(-2)		# keep current airspeed

# AddToClientDataDefinition dwSizeOrType parameter type values
SIMCONNECT_CLIENTDATATYPE_INT8 = DWORD(-1)  		# 8-bit integer number
SIMCONNECT_CLIENTDATATYPE_INT16 = DWORD(-2) 		# 16-bit integer number
SIMCONNECT_CLIENTDATATYPE_INT32 = DWORD(-3) 		# 32-bit integer number
SIMCONNECT_CLIENTDATATYPE_INT64 = DWORD(-4) 		# 64-bit integer number
SIMCONNECT_CLIENTDATATYPE_FLOAT32 = DWORD(-5) 	# 32-bit floating-point number (float)
SIMCONNECT_CLIENTDATATYPE_FLOAT64 = DWORD(-6) 	# 64-bit floating-point number (double)

#AddToClientDataDefinition dwOffset parameter special values
SIMCONNECT_CLIENTDATAOFFSET_AUTO = DWORD(-1)   # automatically compute offset of the ClientData variable

#Open ConfigIndex parameter special value
SIMCONNECT_OPEN_CONFIGINDEX_LOCAL = DWORD(-1)  # ignore SimConnect.cfg settings, and force local connection


def IsHR(hr, value):
	_hr = ctypes.HRESULT(hr)
	return ctypes.c_ulong(_hr.value).value == value


def millis():
	return int(round(time.time() * 1000))


#----------------------------------------------------------------------------
#        Enum definitions
#----------------------------------------------------------------------------


# Define the types we need.
class CtypesEnum(IntEnum):
	"""A ctypes-compatible IntEnum superclass."""
	@classmethod
	def from_param(cls, obj):
		return int(obj)


# Define the types we need.
class CtypesEn(Enum):
	"""A ctypes-compatible Enum superclass."""
	@classmethod
	def from_param(cls, obj):
		return int(obj)


# Receive data types
class SIMCONNECT_RECV_ID(CtypesEnum):
	SIMCONNECT_RECV_ID_NULL = 0
	SIMCONNECT_RECV_ID_EXCEPTION = 1
	SIMCONNECT_RECV_ID_OPEN = 2
	SIMCONNECT_RECV_ID_QUIT = 3
	SIMCONNECT_RECV_ID_EVENT = 4
	SIMCONNECT_RECV_ID_EVENT_OBJECT_ADDREMOVE = 5
	SIMCONNECT_RECV_ID_EVENT_FILENAME = 6
	SIMCONNECT_RECV_ID_EVENT_FRAME = 7
	SIMCONNECT_RECV_ID_SIMOBJECT_DATA = 8
	SIMCONNECT_RECV_ID_SIMOBJECT_DATA_BYTYPE = 9
	SIMCONNECT_RECV_ID_WEATHER_OBSERVATION = 10
	SIMCONNECT_RECV_ID_CLOUD_STATE = 11
	SIMCONNECT_RECV_ID_ASSIGNED_OBJECT_ID = 12
	SIMCONNECT_RECV_ID_RESERVED_KEY = 13
	SIMCONNECT_RECV_ID_CUSTOM_ACTION = 14
	SIMCONNECT_RECV_ID_SYSTEM_STATE = 15
	SIMCONNECT_RECV_ID_CLIENT_DATA = 16
	SIMCONNECT_RECV_ID_EVENT_WEATHER_MODE = 17
	SIMCONNECT_RECV_ID_AIRPORT_LIST = 18
	SIMCONNECT_RECV_ID_VOR_LIST = 19
	SIMCONNECT_RECV_ID_NDB_LIST = 20
	SIMCONNECT_RECV_ID_WAYPOINT_LIST = 21
	SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_SERVER_STARTED = 22
	SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_CLIENT_STARTED = 23
	SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_SESSION_ENDED = 24
	SIMCONNECT_RECV_ID_EVENT_RACE_END = 25
	SIMCONNECT_RECV_ID_EVENT_RACE_LAP = 26

# Data data types
class SIMCONNECT_DATATYPE(CtypesEnum):
	SIMCONNECT_DATATYPE_INVALID = 0        # invalid data type
	SIMCONNECT_DATATYPE_INT32 = 1          # 32-bit integer number
	SIMCONNECT_DATATYPE_INT64 = 2          # 64-bit integer number
	SIMCONNECT_DATATYPE_FLOAT32 = 3        # 32-bit floating-point number (float)
	SIMCONNECT_DATATYPE_FLOAT64 = 4        # 64-bit floating-point number (double)
	SIMCONNECT_DATATYPE_STRING8 = 5        # 8-byte string
	SIMCONNECT_DATATYPE_STRING32 = 6       # 32-byte string
	SIMCONNECT_DATATYPE_STRING64 = 7       # 64-byte string
	SIMCONNECT_DATATYPE_STRING128 = 8      # 128-byte string
	SIMCONNECT_DATATYPE_STRING256 = 9      # 256-byte string
	SIMCONNECT_DATATYPE_STRING260 = 10      # 260-byte string
	SIMCONNECT_DATATYPE_STRINGV = 11        # variable-length string

	SIMCONNECT_DATATYPE_INITPOSITION = 12   # see SIMCONNECT_DATA_INITPOSITION
	SIMCONNECT_DATATYPE_MARKERSTATE = 13    # see SIMCONNECT_DATA_MARKERSTATE
	SIMCONNECT_DATATYPE_WAYPOINT = 14       # see SIMCONNECT_DATA_WAYPOINT
	SIMCONNECT_DATATYPE_LATLONALT = 15      # see SIMCONNECT_DATA_LATLONALT
	SIMCONNECT_DATATYPE_XYZ = 16            # see SIMCONNECT_DATA_XYZ

	SIMCONNECT_DATATYPE_MAX = 17            # enum limit


# Exception error types
class SIMCONNECT_EXCEPTION(CtypesEnum):
	SIMCONNECT_EXCEPTION_NONE = 0

	SIMCONNECT_EXCEPTION_ERROR = 1
	SIMCONNECT_EXCEPTION_SIZE_MISMATCH = 2
	SIMCONNECT_EXCEPTION_UNRECOGNIZED_ID = 3
	SIMCONNECT_EXCEPTION_UNOPENED = 4
	SIMCONNECT_EXCEPTION_VERSION_MISMATCH = 5
	SIMCONNECT_EXCEPTION_TOO_MANY_GROUPS = 6
	SIMCONNECT_EXCEPTION_NAME_UNRECOGNIZED = 7
	SIMCONNECT_EXCEPTION_TOO_MANY_EVENT_NAMES = 8
	SIMCONNECT_EXCEPTION_EVENT_ID_DUPLICATE = 9
	SIMCONNECT_EXCEPTION_TOO_MANY_MAPS = 10
	SIMCONNECT_EXCEPTION_TOO_MANY_OBJECTS = 11
	SIMCONNECT_EXCEPTION_TOO_MANY_REQUESTS = 12
	SIMCONNECT_EXCEPTION_WEATHER_INVALID_PORT = 13
	SIMCONNECT_EXCEPTION_WEATHER_INVALID_METAR = 14
	SIMCONNECT_EXCEPTION_WEATHER_UNABLE_TO_GET_OBSERVATION = 15
	SIMCONNECT_EXCEPTION_WEATHER_UNABLE_TO_CREATE_STATION = 16
	SIMCONNECT_EXCEPTION_WEATHER_UNABLE_TO_REMOVE_STATION = 17
	SIMCONNECT_EXCEPTION_INVALID_DATA_TYPE = 18
	SIMCONNECT_EXCEPTION_INVALID_DATA_SIZE = 19
	SIMCONNECT_EXCEPTION_DATA_ERROR = 20
	SIMCONNECT_EXCEPTION_INVALID_ARRAY = 21
	SIMCONNECT_EXCEPTION_CREATE_OBJECT_FAILED = 22
	SIMCONNECT_EXCEPTION_LOAD_FLIGHTPLAN_FAILED = 23
	SIMCONNECT_EXCEPTION_OPERATION_INVALID_FOR_OBJECT_TYPE = 24
	SIMCONNECT_EXCEPTION_ILLEGAL_OPERATION = 24
	SIMCONNECT_EXCEPTION_ALREADY_SUBSCRIBED = 26
	SIMCONNECT_EXCEPTION_INVALID_ENUM = 27
	SIMCONNECT_EXCEPTION_DEFINITION_ERROR = 28
	SIMCONNECT_EXCEPTION_DUPLICATE_ID = 29
	SIMCONNECT_EXCEPTION_DATUM_ID = 30
	SIMCONNECT_EXCEPTION_OUT_OF_BOUNDS = 31
	SIMCONNECT_EXCEPTION_ALREADY_CREATED = 32
	SIMCONNECT_EXCEPTION_OBJECT_OUTSIDE_REALITY_BUBBLE = 33
	SIMCONNECT_EXCEPTION_OBJECT_CONTAINER = 34
	SIMCONNECT_EXCEPTION_OBJECT_AI = 35
	SIMCONNECT_EXCEPTION_OBJECT_ATC = 36
	SIMCONNECT_EXCEPTION_OBJECT_SCHEDULE = 37


# Object types
class SIMCONNECT_SIMOBJECT_TYPE(CtypesEnum):
	SIMCONNECT_SIMOBJECT_TYPE_USER = 0
	SIMCONNECT_SIMOBJECT_TYPE_ALL = 1
	SIMCONNECT_SIMOBJECT_TYPE_AIRCRAFT = 2
	SIMCONNECT_SIMOBJECT_TYPE_HELICOPTER = 3
	SIMCONNECT_SIMOBJECT_TYPE_BOAT = 4
	SIMCONNECT_SIMOBJECT_TYPE_GROUND = 5


# EventState values
class SIMCONNECT_STATE(CtypesEnum):
	SIMCONNECT_STATE_OFF = 0
	SIMCONNECT_STATE_ON = 1


# Object Data Request Period values
class SIMCONNECT_PERIOD(CtypesEnum):  #
	SIMCONNECT_PERIOD_NEVER = 0
	SIMCONNECT_PERIOD_ONCE = 1
	SIMCONNECT_PERIOD_VISUAL_FRAME = 2
	SIMCONNECT_PERIOD_SIM_FRAME = 3
	SIMCONNECT_PERIOD_SECOND = 4


class SIMCONNECT_MISSION_END(CtypesEnum):  #
	SIMCONNECT_MISSION_FAILED = 0
	SIMCONNECT_MISSION_CRASHED = 1
	SIMCONNECT_MISSION_SUCCEEDED = 2


# ClientData Request Period values
class SIMCONNECT_CLIENT_DATA_PERIOD(CtypesEnum):  #
	SIMCONNECT_CLIENT_DATA_PERIOD_NEVER = 0
	SIMCONNECT_CLIENT_DATA_PERIOD_ONCE = 1
	SIMCONNECT_CLIENT_DATA_PERIOD_VISUAL_FRAME = 2
	SIMCONNECT_CLIENT_DATA_PERIOD_ON_SET = 3
	SIMCONNECT_CLIENT_DATA_PERIOD_SECOND = 4


class SIMCONNECT_TEXT_TYPE(CtypesEnum):  #
	SIMCONNECT_TEXT_TYPE_SCROLL_BLACK = 0
	SIMCONNECT_TEXT_TYPE_SCROLL_WHITE = 1
	SIMCONNECT_TEXT_TYPE_SCROLL_RED = 2
	SIMCONNECT_TEXT_TYPE_SCROLL_GREEN = 3
	SIMCONNECT_TEXT_TYPE_SCROLL_BLUE = 4
	SIMCONNECT_TEXT_TYPE_SCROLL_YELLOW = 5
	SIMCONNECT_TEXT_TYPE_SCROLL_MAGENTA = 6
	SIMCONNECT_TEXT_TYPE_SCROLL_CYAN = 7
	SIMCONNECT_TEXT_TYPE_PRINT_BLACK = 0x100
	SIMCONNECT_TEXT_TYPE_PRINT_WHITE = 0x101
	SIMCONNECT_TEXT_TYPE_PRINT_RED = 0x102
	SIMCONNECT_TEXT_TYPE_PRINT_GREEN = 0x103
	SIMCONNECT_TEXT_TYPE_PRINT_BLUE = 0x104
	SIMCONNECT_TEXT_TYPE_PRINT_YELLOW = 0x105
	SIMCONNECT_TEXT_TYPE_PRINT_MAGENTA = 0x106
	SIMCONNECT_TEXT_TYPE_PRINT_CYAN = 0x107
	SIMCONNECT_TEXT_TYPE_MENU = 0x0200


class SIMCONNECT_TEXT_RESULT(CtypesEnum):  #
	SIMCONNECT_TEXT_RESULT_MENU_SELECT_1 = 0
	SIMCONNECT_TEXT_RESULT_MENU_SELECT_2 = 1
	SIMCONNECT_TEXT_RESULT_MENU_SELECT_3 = 2
	SIMCONNECT_TEXT_RESULT_MENU_SELECT_4 = 3
	SIMCONNECT_TEXT_RESULT_MENU_SELECT_5 = 4
	SIMCONNECT_TEXT_RESULT_MENU_SELECT_6 = 5
	SIMCONNECT_TEXT_RESULT_MENU_SELECT_7 = 6
	SIMCONNECT_TEXT_RESULT_MENU_SELECT_8 = 7
	SIMCONNECT_TEXT_RESULT_MENU_SELECT_9 = 8
	SIMCONNECT_TEXT_RESULT_MENU_SELECT_10 = 9
	SIMCONNECT_TEXT_RESULT_DISPLAYED = 0x10000
	SIMCONNECT_TEXT_RESULT_QUEUED = 0x10001
	SIMCONNECT_TEXT_RESULT_REMOVED = 0x1002
	SIMCONNECT_TEXT_RESULT_REPLACED = 0x10003
	SIMCONNECT_TEXT_RESULT_TIMEOUT = 0x10004


class SIMCONNECT_WEATHER_MODE(CtypesEnum):  #
	SIMCONNECT_WEATHER_MODE_THEME = 0
	SIMCONNECT_WEATHER_MODE_RWW = 1
	SIMCONNECT_WEATHER_MODE_CUSTOM = 2
	SIMCONNECT_WEATHER_MODE_GLOBAL = 3


class SIMCONNECT_FACILITY_LIST_TYPE(CtypesEnum):  #
	SIMCONNECT_FACILITY_LIST_TYPE_AIRPORT = 0
	SIMCONNECT_FACILITY_LIST_TYPE_WAYPOINT = 1
	SIMCONNECT_FACILITY_LIST_TYPE_NDB = 2
	SIMCONNECT_FACILITY_LIST_TYPE_VOR = 3
	SIMCONNECT_FACILITY_LIST_TYPE_COUNT = 4  # invalid


class SIMCONNECT_VOR_FLAGS(CtypesEn):  # flags for SIMCONNECT_RECV_ID_VOR_LIST
	SIMCONNECT_RECV_ID_VOR_LIST_HAS_NAV_SIGNAL = DWORD(0x00000001)  # Has Nav signal
	SIMCONNECT_RECV_ID_VOR_LIST_HAS_LOCALIZER = DWORD(0x00000002)  # Has localizer
	SIMCONNECT_RECV_ID_VOR_LIST_HAS_GLIDE_SLOPE = DWORD(0x00000004)  # Has Nav signal
	SIMCONNECT_RECV_ID_VOR_LIST_HAS_DME = DWORD(0x00000008)  # Station has DME


# bits for the Waypoint Flags field: may be combined
class SIMCONNECT_WAYPOINT_FLAGS(CtypesEn):  #
	SIMCONNECT_WAYPOINT_NONE = DWORD(0x00)  #
	SIMCONNECT_WAYPOINT_SPEED_REQUESTED = DWORD(0x04)  # requested speed at waypoint is valid
	SIMCONNECT_WAYPOINT_THROTTLE_REQUESTED = DWORD(0x08)  # request a specific throttle percentage
	SIMCONNECT_WAYPOINT_COMPUTE_VERTICAL_SPEED = DWORD(0x10)  # compute vertical to speed to reach waypoint altitude when crossing the waypoint
	SIMCONNECT_WAYPOINT_ALTITUDE_IS_AGL = DWORD(0x20)  # AltitudeIsAGL
	SIMCONNECT_WAYPOINT_ON_GROUND = DWORD(0x00100000)  # place this waypoint on the ground
	SIMCONNECT_WAYPOINT_REVERSE = DWORD(0x00200000)  # Back up to this waypoint. Only valid on first waypoint
	SIMCONNECT_WAYPOINT_WRAP_TO_FIRST = DWORD(0x00400000)  # Wrap around back to first waypoint. Only valid on last waypoint.


class SIMCONNECT_EVENT_FLAG(CtypesEn):  #
	SIMCONNECT_EVENT_FLAG_DEFAULT = DWORD(0x00000000)  #
	SIMCONNECT_EVENT_FLAG_FAST_REPEAT_TIMER = DWORD(0x00000001)  # set event repeat timer to simulate fast repeat
	SIMCONNECT_EVENT_FLAG_SLOW_REPEAT_TIMER = DWORD(0x00000002)  # set event repeat timer to simulate slow repeat
	SIMCONNECT_EVENT_FLAG_GROUPID_IS_PRIORITY = DWORD(0x00000010)  # interpret GroupID parameter as priority value


class SIMCONNECT_DATA_REQUEST_FLAG(CtypesEn):  #
	SIMCONNECT_DATA_REQUEST_FLAG_DEFAULT = DWORD(0x00000000)
	SIMCONNECT_DATA_REQUEST_FLAG_CHANGED = DWORD(0x00000001)  # send requested data when value(s) change
	SIMCONNECT_DATA_REQUEST_FLAG_TAGGED = DWORD(0x00000002)  # send requested data in tagged format


class SIMCONNECT_DATA_SET_FLAG(CtypesEn):  #
	SIMCONNECT_DATA_SET_FLAG_DEFAULT = DWORD(0x00000000)
	SIMCONNECT_DATA_SET_FLAG_TAGGED = DWORD(0x00000001)  # data is in tagged format


class SIMCONNECT_CREATE_CLIENT_DATA_FLAG(CtypesEn):  #
	SIMCONNECT_CREATE_CLIENT_DATA_FLAG_DEFAULT = DWORD(0x00000000)  #
	SIMCONNECT_CREATE_CLIENT_DATA_FLAG_READ_ONLY = DWORD(0x00000001)  # permit only ClientData creator to write into ClientData


class SIMCONNECT_CLIENT_DATA_REQUEST_FLAG(CtypesEn):  #
	SIMCONNECT_CLIENT_DATA_REQUEST_FLAG_DEFAULT = DWORD(0x00000000)  #
	SIMCONNECT_CLIENT_DATA_REQUEST_FLAG_CHANGED = DWORD(0x00000001)  # send requested ClientData when value(s) change
	SIMCONNECT_CLIENT_DATA_REQUEST_FLAG_TAGGED = DWORD(0x00000002)  # send requested ClientData in tagged format


class SIMCONNECT_CLIENT_DATA_SET_FLAG(CtypesEn):  #
	SIMCONNECT_CLIENT_DATA_SET_FLAG_DEFAULT = DWORD(0x00000000)  #
	SIMCONNECT_CLIENT_DATA_SET_FLAG_TAGGED = DWORD(0x00000001)  # data is in tagged format


class SIMCONNECT_VIEW_SYSTEM_EVENT_DATA(CtypesEn):  # dwData contains these flags for the "View" System Event
	SIMCONNECT_VIEW_SYSTEM_EVENT_DATA_COCKPIT_2D = DWORD(0x00000001)  # 2D Panels in cockpit view
	SIMCONNECT_VIEW_SYSTEM_EVENT_DATA_COCKPIT_VIRTUAL = DWORD(0x00000002)  # Virtual (3D) panels in cockpit view
	SIMCONNECT_VIEW_SYSTEM_EVENT_DATA_ORTHOGONAL = DWORD(0x00000004)  # Orthogonal (Map) view


class SIMCONNECT_SOUND_SYSTEM_EVENT_DATA(CtypesEn):  # dwData contains these flags for the "Sound" System Event
	SIMCONNECT_SOUND_SYSTEM_EVENT_DATA_MASTER = DWORD(0x00000001)  # Sound Master


class SIMCONNECT_PICK_FLAGS(CtypesEn):
	SIMCONNECT_PICK_GROUND = DWORD(0x01)  # pick ground/ pick result item is ground location
	SIMCONNECT_PICK_AI = DWORD(0x02)  # pick AI    / pick result item is AI, (dwSimObjectID is valid)
	SIMCONNECT_PICK_SCENERY = DWORD(0x04)  # pick scenery/ pick result item is scenery object (hSceneryObject is valid)
	SIMCONNECT_PICK_ALL = DWORD(0x04 | 0x02 | 0x01)  # pick all / (not valid on pick result item)
	SIMCONNECT_PICK_COORDSASPIXELS = DWORD(0x08)  #


#----------------------------------------------------------------------------
#        User-defined enums
#----------------------------------------------------------------------------
class SIMCONNECT_NOTIFICATION_GROUP_ID(CtypesEnum):  # client-defined notification group ID
	pass


class SIMCONNECT_INPUT_GROUP_ID(CtypesEnum):  # client-defined input group ID
	pass


class SIMCONNECT_DATA_DEFINITION_ID(CtypesEnum):  # client-defined data definition ID
	pass


class SIMCONNECT_DATA_REQUEST_ID(CtypesEnum):  # client-defined request data ID
	pass


class SIMCONNECT_CLIENT_EVENT_ID(CtypesEnum):  # client-defined client event ID
	pass


class SIMCONNECT_CLIENT_DATA_ID(CtypesEnum):  # client-defined client data ID
	pass


class SIMCONNECT_CLIENT_DATA_DEFINITION_ID(CtypesEnum):  # client-defined client data definition ID
	pass


#----------------------------------------------------------------------------
#        Struct definitions
#----------------------------------------------------------------------------


class SIMCONNECT_RECV(Structure):
	_fields_ = [
		("dwSize", DWORD),
		("dwVersion", DWORD),
		("dwID", DWORD)
	]


class SIMCONNECT_RECV_EXCEPTION(SIMCONNECT_RECV):   # when dwID == SIMCONNECT_RECV_ID_EXCEPTION
	_fields_ = [
		("dwException", DWORD),  # see SIMCONNECT_EXCEPTION
		("UNKNOWN_SENDID", DWORD),  #
		("dwSendID", DWORD),  # see SimConnect_GetLastSentPacketID
		("UNKNOWN_INDEX", DWORD),  #
		("dwIndex", DWORD)  # index of parameter that was source of error
	]


class SIMCONNECT_RECV_OPEN(SIMCONNECT_RECV):   # when dwID == SIMCONNECT_RECV_ID_OPEN
	_fields_ = [
		("szApplicationName", c_char * 256),
		("dwApplicationVersionMajor", DWORD),
		("dwApplicationVersionMinor", DWORD),
		("dwApplicationBuildMajor", DWORD),
		("dwApplicationBuildMinor", DWORD),
		("dwSimConnectVersionMajor", DWORD),
		("dwSimConnectVersionMinor", DWORD),
		("dwSimConnectBuildMajor", DWORD),
		("dwSimConnectBuildMinor", DWORD),
		("dwReserved1", DWORD),
		("dwReserved2", DWORD)
	]


class SIMCONNECT_RECV_QUIT(SIMCONNECT_RECV):  # when dwID == SIMCONNECT_RECV_ID_QUIT
	pass


class SIMCONNECT_RECV_EVENT(SIMCONNECT_RECV):       # when dwID == SIMCONNECT_RECV_ID_EVENT
	UNKNOWN_GROUP = DWORD_MAX
	_fields_ = [
		("uGroupID", DWORD),
		("uEventID", DWORD),
		("dwData", DWORD)	 # uEventID-dependent context
	]


class SIMCONNECT_RECV_EVENT_FILENAME(SIMCONNECT_RECV_EVENT):       # when dwID == SIMCONNECT_RECV_ID_EVENT_FILENAME
	_fields_ = [
		("zFileName", c_char * MAX_PATH),   # uEventID-dependent context
		("dwFlags", DWORD)
	]


class SIMCONNECT_RECV_EVENT_OBJECT_ADDREMOVE(SIMCONNECT_RECV_EVENT):       # when dwID == SIMCONNECT_RECV_ID_EVENT_FILENAME
	eObjType = SIMCONNECT_SIMOBJECT_TYPE


class SIMCONNECT_RECV_EVENT_FRAME(SIMCONNECT_RECV_EVENT):       # when dwID == SIMCONNECT_RECV_ID_EVENT_FRAME
	_fields_ = [
		("fFrameRate", c_float),
		("fSimSpeed", c_float)
	]


class SIMCONNECT_RECV_EVENT_MULTIPLAYER_SERVER_STARTED(SIMCONNECT_RECV_EVENT):
	# when dwID == SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_SERVER_STARTED
	# No event specific data, for now
	pass


class SIMCONNECT_RECV_EVENT_MULTIPLAYER_CLIENT_STARTED(SIMCONNECT_RECV_EVENT):
	# when dwID == SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_CLIENT_STARTED
	# No event specific data, for now
	pass


class SIMCONNECT_RECV_EVENT_MULTIPLAYER_SESSION_ENDED(SIMCONNECT_RECV_EVENT):
	# when dwID == SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_SESSION_ENDED
	# No event specific data, for now
	pass


# SIMCONNECT_DATA_RACE_RESULT
class SIMCONNECT_DATA_RACE_RESULT(Structure):
	_fields_ = [
		("dwNumberOfRacers", DWORD),  # The total number of racers
		("szPlayerName", c_char * MAX_PATH),  # The name of the player
		("szSessionType", c_char * MAX_PATH),  # The type of the multiplayer session: "LAN", "GAMESPY")
		("szAircraft", c_char * MAX_PATH),  # The aircraft type
		("szPlayerRole", c_char * MAX_PATH),  # The player role in the mission
		("fTotalTime", c_double),  # Total time in seconds, 0 means DNF
		("fPenaltyTime", c_double),  # Total penalty time in seconds
		("MissionGUID", DWORD),    # The name of the mission to execute, NULL if no mission
		("dwIsDisqualified", c_double)  # non 0 - disqualified, 0 - not disqualified

	]


class SIMCONNECT_RECV_EVENT_RACE_END(SIMCONNECT_RECV_EVENT):       # when dwID == SIMCONNECT_RECV_ID_EVENT_RACE_END
	RacerData = SIMCONNECT_DATA_RACE_RESULT
	_fields_ = [
		("dwRacerNumber", DWORD)  # The index of the racer the results are for
	]


class SIMCONNECT_RECV_EVENT_RACE_LAP(SIMCONNECT_RECV_EVENT):       # when dwID == SIMCONNECT_RECV_ID_EVENT_RACE_LAP
	RacerData = SIMCONNECT_DATA_RACE_RESULT
	_fields_ = [
		("dwLapIndex", DWORD)  # The index of the lap the results are for
	]


class SIMCONNECT_RECV_SIMOBJECT_DATA(SIMCONNECT_RECV):
	_fields_ = [
		("dwRequestID", DWORD),
		("dwObjectID", DWORD),
		("dwDefineID", DWORD),
		("dwFlags", DWORD),
		("dwentrynumber", DWORD),
		("dwoutof", DWORD),
		("dwDefineCount", DWORD),
		("dwData", DWORD * 8192)]


class SIMCONNECT_RECV_SIMOBJECT_DATA_BYTYPE(SIMCONNECT_RECV_SIMOBJECT_DATA):
	_fields_ = []


class SIMCONNECT_RECV_CLIENT_DATA(SIMCONNECT_RECV_SIMOBJECT_DATA):    # when dwID == SIMCONNECT_RECV_ID_CLIENT_DATA
	_fields_ = []


class SIMCONNECT_RECV_WEATHER_OBSERVATION(SIMCONNECT_RECV):  # when dwID == SIMCONNECT_RECV_ID_WEATHER_OBSERVATION
	_fields_ = [
		("dwRequestID", DWORD),
		("szMetar", c_char * MAX_METAR_LENGTH.value) 	# Variable length string whose maximum size is MAX_METAR_LENGTH
	]


SIMCONNECT_CLOUD_STATE_ARRAY_WIDTH = 64
SIMCONNECT_CLOUD_STATE_ARRAY_SIZE = SIMCONNECT_CLOUD_STATE_ARRAY_WIDTH * SIMCONNECT_CLOUD_STATE_ARRAY_WIDTH


class SIMCONNECT_RECV_CLOUD_STATE(SIMCONNECT_RECV):
	# when dwID == SIMCONNECT_RECV_ID_CLOUD_STATE
	_fields_ = [
		("dwRequestID", DWORD),
		("dwArraySize", DWORD),
		# SIMCONNECT_FIXEDTYPE_DATAV(BYTE,    rgbData, dwArraySize, U1 /*member of UnmanagedType enum*/ , System::Byte /*cli type*/);
	]


class SIMCONNECT_RECV_ASSIGNED_OBJECT_ID(SIMCONNECT_RECV):  # when dwID == SIMCONNECT_RECV_ID_ASSIGNED_OBJECT_ID
	_fields_ = [
		("dwRequestID", DWORD),
		("dwObjectID", DWORD)
	]


class SIMCONNECT_RECV_RESERVED_KEY(SIMCONNECT_RECV):  # when dwID == SIMCONNECT_RECV_ID_RESERVED_KEY
	_fields_ = [
		("szChoiceReserved", c_char * 30),
		("szReservedKey", c_char * 30)
	]


class SIMCONNECT_RECV_SYSTEM_STATE(SIMCONNECT_RECV):  # when dwID == SIMCONNECT_RECV_ID_SYSTEM_STATE
	_fields_ = [
		("dwRequestID", DWORD),
		("dwInteger", DWORD),
		("fFloat", c_float),
		("szString", c_char * MAX_PATH)
	]


class SIMCONNECT_RECV_CUSTOM_ACTION(SIMCONNECT_RECV_EVENT):  #
	_fields_ = [
		("guidInstanceId", DWORD),  # Instance id of the action that executed
		("dwWaitForCompletion", DWORD),  # Wait for completion flag on the action
		("szPayLoad", c_char)  # Variable length string payload associated with the mission action.
	]


class SIMCONNECT_RECV_EVENT_WEATHER_MODE(SIMCONNECT_RECV_EVENT):  #
	_fields_ = []  # No event specific data - the new weather mode is in the base structure dwData member.


# SIMCONNECT_RECV_FACILITIES_LIST
class SIMCONNECT_RECV_FACILITIES_LIST(SIMCONNECT_RECV):  #
	_fields_ = [
		("dwRequestID", DWORD),
		("dwArraySize", DWORD),
		("dwEntryNumber", DWORD),  # when the array of items is too big for one send, which send this is (0..dwOutOf-1)
		("dwOutOf", DWORD)  # total number of transmissions the list is chopped into
	]


# SIMCONNECT_DATA_FACILITY_AIRPORT
class SIMCONNECT_DATA_FACILITY_AIRPORT(Structure):  #
	_fields_ = [
		("Icao", c_char * 9),  # ICAO of the object
		("Latitude", c_double),  # degrees
		("Longitude", c_double),  # degrees
		("Altitude", c_double)  # meters
	]


# SIMCONNECT_RECV_AIRPORT_LIST
#class SIMCONNECT_RECV_AIRPORT_LIST(SIMCONNECT_RECV_FACILITIES_LIST):  #
#	_fields_ = [
#		("SIMCONNECT_DATA_FACILITY_AIRPORT", rgData * dwArraySize)
#	]
#  SIMCONNECT_FIXEDTYPE_DATAV(SIMCONNECT_DATA_FACILITY_AIRPORT, rgData, dwArraySize,
#  U1 /*member of UnmanagedType enum*/, SIMCONNECT_DATA_FACILITY_AIRPORT /*cli type*/);


# SIMCONNECT_DATA_FACILITY_WAYPOINT
class SIMCONNECT_DATA_FACILITY_WAYPOINT(SIMCONNECT_DATA_FACILITY_AIRPORT):  #
	_fields_ = [
		("fMagVar", c_float)  # Magvar in degrees
	]


# SIMCONNECT_RECV_WAYPOINT_LIST
#class SIMCONNECT_RECV_WAYPOINT_LIST(SIMCONNECT_RECV_FACILITIES_LIST):  #
#	_fields_ = [
#		("", )
#	]
#    SIMCONNECT_FIXEDTYPE_DATAV(SIMCONNECT_DATA_FACILITY_WAYPOINT,
#   rgData
#   dwArraySize,
#    U1 /*member of UnmanagedType enum*/,
#   SIMCONNECT_DATA_FACILITY_WAYPOINT /*cli type*/);


# SIMCONNECT_DATA_FACILITY_NDB
class SIMCONNECT_DATA_FACILITY_NDB(SIMCONNECT_DATA_FACILITY_WAYPOINT):  #
	_fields_ = [
		("fFrequency", DWORD)  # frequency in Hz
	]


# SIMCONNECT_RECV_NDB_LIST
# class SIMCONNECT_RECV_NDB_LIST(SIMCONNECT_RECV_FACILITIES_LIST):  #
#	_fields_ = [
#		("", )
#	]
#    SIMCONNECT_FIXEDTYPE_DATAV(SIMCONNECT_DATA_FACILITY_NDB,
#   rgData
#   dwArraySize,
#    U1 /*member of UnmanagedType enum*/,
#   SIMCONNECT_DATA_FACILITY_NDB /*cli type*/);


# SIMCONNECT_DATA_FACILITY_VOR
class SIMCONNECT_DATA_FACILITY_VOR(SIMCONNECT_DATA_FACILITY_NDB):  #
	_fields_ = [
		("Flags", DWORD),  # SIMCONNECT_VOR_FLAGS
		("fLocalizer", c_float),  # Localizer in degrees
		("GlideLat", c_double),  # Glide Slope Location (deg, deg, meters)
		("GlideLon", c_double),  #
		("GlideAlt", c_double),  #
		("fGlideSlopeAngle", c_float)  # Glide Slope in degrees
	]


# SIMCONNECT_RECV_VOR_LIST
#class SIMCONNECT_RECV_VOR_LIST(SIMCONNECT_RECV_FACILITIES_LIST):  #
#	_fields_ = [
#		("", )
#	]
#    SIMCONNECT_FIXEDTYPE_DATAV(SIMCONNECT_DATA_FACILITY_VOR,
#   rgData
#   dwArraySize,
#		 U1 /*member of UnmanagedType enum*/, SIMCONNECT_DATA_FACILITY_VOR /*cli type*/);


class SIMCONNECT_RECV_PICK(SIMCONNECT_RECV):  # when dwID == SIMCONNECT_RECV_ID_RESERVED_KEY
	_fields_ = [
		("hContext", HANDLE),
		("dwFlags", DWORD),
		("Latitude", c_double),  # degrees
		("Longitude", c_double),  # degrees
		("Altitude", c_double),  # feet
		("xPos", c_int),  # reserved
		("yPos", c_int),  # reserved
		("dwSimObjectID", DWORD),
		("hSceneryObject", HANDLE),
		("dwentrynumber", DWORD),  # if multiple objects returned, this is number <entrynumber> out of <outof>.
		("dwoutof", DWORD)  # note:  starts with 1, not 0.
	]


# SIMCONNECT_DATATYPE_INITPOSITION
class SIMCONNECT_DATA_INITPOSITION(Structure):  #
	_fields_ = [
		("Latitude", c_double),  # degrees
		("Longitude", c_double),  # degrees
		("Altitude", c_double),  # feet
		("Pitch", c_double),  # degrees
		("Bank", c_double),  # degrees
		("Heading", c_double),  # degrees
		("OnGround", DWORD),  # 1=force to be on the ground
		("Airspeed", DWORD)  # knots
	]


# SIMCONNECT_DATATYPE_MARKERSTATE
class SIMCONNECT_DATA_MARKERSTATE(Structure):  #
	_fields_ = [
		("szMarkerName", c_char * 64),
		("dwMarkerState", DWORD)
	]


# SIMCONNECT_DATATYPE_WAYPOINT
class SIMCONNECT_DATA_WAYPOINT(Structure):  #
	_fields_ = [
		("Latitude", c_double),  # degrees
		("Longitude", c_double),  # degrees
		("Altitude", c_double),  # feet
		("Flags", c_ulong),
		("ktsSpeed", c_double),  # knots
		("percentThrottle", c_double)
	]


# SIMCONNECT_DATA_LATLONALT
class SIMCONNECT_DATA_LATLONALT(Structure):  #
	_fields_ = [
		("Latitude", c_double),
		("Longitude", c_double),
		("Altitude", c_double)
	]


# SIMCONNECT_DATA_XYZ
class SIMCONNECT_DATA_XYZ(Structure):  #
	_fields_ = [
		("x", c_double),
		("y", c_double),
		("z", c_double)
	]


class Request():
	def __init__(self, _DATA_DEFINITION_ID=SIMCONNECT_DATA_DEFINITION_ID, _DATA_REQUEST_ID=SIMCONNECT_DATA_REQUEST_ID, _outputData=None):
		self.DATA_DEFINITION_ID = _DATA_DEFINITION_ID
		self.DATA_REQUEST_ID = _DATA_REQUEST_ID
		self.definitions = []
		self.outputData = _outputData


class PythonSimConnect():

	# TODO: update callbackfunction to expand functions.
	def MyDispatchProc(self, pData, cbData, pContext):
		dwID = pData.contents.dwID
		self.pS = None
		if dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT:
			evt = cast(pData, POINTER(SIMCONNECT_RECV_EVENT))
			uEventID = evt.contents.uEventID
			if uEventID == self.EventID.EVENT_SIM_START:
				print("SIM START")

		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_SIMOBJECT_DATA_BYTYPE:
			pObjData = cast(pData, POINTER(SIMCONNECT_RECV_SIMOBJECT_DATA_BYTYPE)).contents
			dwRequestID = pObjData.dwRequestID
			for _request in self.Requests:
				if dwRequestID == _request.DATA_REQUEST_ID:
					self.out_data[_request.DATA_REQUEST_ID] = cast(pObjData.dwData, POINTER(_request.outputData)).contents

		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_OPEN:
			print("SIM OPEN")

		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_QUIT:
			self.quit = 1
		else:
			print("Received:", dwID)
		return

	def __init__(
		self,
		_CLIENT_EVENT_ID=SIMCONNECT_CLIENT_EVENT_ID,
		_NOTIFICATION_GROUP_ID=SIMCONNECT_NOTIFICATION_GROUP_ID,
		_DATA_DEFINITION_ID=SIMCONNECT_DATA_DEFINITION_ID,
		_DATA_REQUEST_ID=SIMCONNECT_DATA_REQUEST_ID,
		_INPUT_GROUP_ID=SIMCONNECT_INPUT_GROUP_ID,
		_CLIENT_DATA_ID=SIMCONNECT_CLIENT_DATA_ID,
		_CLIENT_DATA_DEFINITION_ID=SIMCONNECT_CLIENT_DATA_DEFINITION_ID
	):

		self.EventID = _CLIENT_EVENT_ID
		self.DATA_DEFINITION_ID = _DATA_DEFINITION_ID
		self.DATA_REQUEST_ID = _DATA_REQUEST_ID
		self.GROUP_ID = _NOTIFICATION_GROUP_ID
		self.INPUT_GROUP_ID = _INPUT_GROUP_ID
		self.CLIENT_DATA_ID = _CLIENT_DATA_ID
		self.CLIENT_DATA_DEFINITION_ID = _CLIENT_DATA_DEFINITION_ID
		self.Requests = []
		self.out_data = {}

		SimConnect = cdll.LoadLibrary("./SimConnect.dll")
		#SIMCONNECTAPI SimConnect_Open(
		#	HANDLE * phSimConnect,
		#	LPCSTR szName,
		#	HWND hWnd,
		#	DWORD UserEventWin32,
		#	HANDLE hEventHandle,
		#	DWORD ConfigIndex)

		self.Open = SimConnect.SimConnect_Open
		self.Open.restype = HRESULT
		self.Open.argtypes = [POINTER(HANDLE), LPCSTR, HWND, DWORD, HANDLE, DWORD]

		#SIMCONNECTAPI SimConnect_Close(
		#	HANDLE hSimConnect);

		self.Close = SimConnect.SimConnect_Close
		self.Close.restype = HRESULT
		self.Close.argtypes = [HANDLE]

		#SIMCONNECTAPI SimConnect_AddToDataDefinition(
		#	HANDLE hSimConnect,
		#	SIMCONNECT_DATA_DEFINITION_ID DefineID,
		#	const char * DatumName,
		#	const char * UnitsName,
		#	SIMCONNECT_DATATYPE DatumType = SIMCONNECT_DATATYPE_FLOAT64,
		#	float fEpsilon = 0,
		#	DWORD DatumID = SIMCONNECT_UNUSED);

		self.AddToDataDefinition = SimConnect.SimConnect_AddToDataDefinition
		self.AddToDataDefinition.restype = HRESULT
		self.AddToDataDefinition.argtypes = [HANDLE, self.DATA_DEFINITION_ID, c_char_p, c_char_p, SIMCONNECT_DATATYPE, c_float, DWORD]

		#SIMCONNECTAPI SimConnect_SubscribeToSystemEvent(
		#	HANDLE hSimConnect,
		#	SIMCONNECT_CLIENT_EVENT_ID EventID,
		#	const char * SystemEventName);

		self.SubscribeToSystemEvent = SimConnect.SimConnect_SubscribeToSystemEvent
		self.SubscribeToSystemEvent.restype = HRESULT
		self.SubscribeToSystemEvent.argtypes = [HANDLE, self.EventID, c_char_p]

		#SIMCONNECTAPI SimConnect_CallDispatch(
		#	HANDLE hSimConnect,
		#	DispatchProc pfcnDispatch,
		#	void * pContext);

		DispatchProc = CFUNCTYPE(c_void_p, POINTER(SIMCONNECT_RECV), DWORD, c_void_p)

		self.CallDispatch = SimConnect.SimConnect_CallDispatch
		self.CallDispatch.restype = HRESULT
		self.CallDispatch.argtypes = [HANDLE, DispatchProc, c_void_p]

		#SIMCONNECTAPI SimConnect_RequestDataOnSimObjectType(
		#	HANDLE hSimConnect,
		#	SIMCONNECT_DATA_REQUEST_ID RequestID,
		#	SIMCONNECT_DATA_DEFINITION_ID DefineID,
		#	DWORD dwRadiusMeters,
		#	SIMCONNECT_SIMOBJECT_TYPE type);

		self.RequestDataOnSimObjectType = SimConnect.SimConnect_RequestDataOnSimObjectType
		self.RequestDataOnSimObjectType.restype = HRESULT
		self.RequestDataOnSimObjectType.argtypes = [HANDLE, self.DATA_REQUEST_ID, self.DATA_DEFINITION_ID, DWORD, SIMCONNECT_SIMOBJECT_TYPE]

		#SIMCONNECTAPI SimConnect_SetDataOnSimObject(
		#	HANDLE hSimConnect,
		#	SIMCONNECT_DATA_DEFINITION_ID DefineID,
		#	SIMCONNECT_OBJECT_ID ObjectID,
		#	SIMCONNECT_DATA_SET_FLAG Flags,
		#	DWORD ArrayCount,
		#	DWORD cbUnitSize,
		#	void * pDataSet);

		#self.SetDataOnSimObject = SimConnect.SimConnect_SetDataOnSimObject
		#self.SetDataOnSimObject.restype = HRESULT
		#self.SetDataOnSimObject.argtypes = [HANDLE, DATA_DEFINE_ID, SIMCONNECT_OBJECT_ID, SIMCONNECT_DATA_SET_FLAG, DWORD, DWORD, ibbuf]

		#SIMCONNECTAPI SimConnect_TransmitClientEvent(
		#	HANDLE hSimConnect,
		#	SIMCONNECT_OBJECT_ID ObjectID,
		#	SIMCONNECT_CLIENT_EVENT_ID EventID,
		#	DWORD dwData,
		#	SIMCONNECT_NOTIFICATION_GROUP_ID GroupID,
		#	SIMCONNECT_EVENT_FLAG Flags);

		self.TransmitClientEvent = SimConnect.SimConnect_TransmitClientEvent
		self.TransmitClientEvent.restype = HRESULT
		self.TransmitClientEvent.argtypes = [HANDLE, SIMCONNECT_OBJECT_ID, self.EventID, DWORD, DWORD, DWORD]

		#SIMCONNECTAPI SimConnect_MapClientEventToSimEvent(
		#	HANDLE hSimConnect,
		#	SIMCONNECT_CLIENT_EVENT_ID EventID,
		#	const char * EventName = "");

		self.MapClientEventToSimEvent = SimConnect.SimConnect_MapClientEventToSimEvent
		self.MapClientEventToSimEvent.restype = HRESULT
		self.MapClientEventToSimEvent.argtypes = [HANDLE, self.EventID, c_char_p]

		#SIMCONNECTAPI SimConnect_AddClientEventToNotificationGroup(
		#	HANDLE hSimConnect,
		#	SIMCONNECT_NOTIFICATION_GROUP_ID GroupID,
		#	SIMCONNECT_CLIENT_EVENT_ID EventID,
		#	BOOL bMaskable = FALSE);

		self.AddClientEventToNotificationGroup = SimConnect.SimConnect_AddClientEventToNotificationGroup
		self.AddClientEventToNotificationGroup.restype = HRESULT
		self.AddClientEventToNotificationGroup.argtypes = [HANDLE, self.GROUP_ID, self.EventID, c_bool]

		# SIMCONNECTAPI SimConnect_SetSystemEventState(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   SIMCONNECT_STATE dwState);
		self.SetSystemEventState = SimConnect.SimConnect_SetSystemEventState
		self.SetSystemEventState.restype = HRESULT
		self.SetSystemEventState.argtypes = [HANDLE, self.EventID, SIMCONNECT_STATE]

		# SIMCONNECTAPI SimConnect_AddClientEventToNotificationGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   BOOL bMaskable = FALSE);
		self.AddClientEventToNotificationGroup = SimConnect.SimConnect_AddClientEventToNotificationGroup
		self.AddClientEventToNotificationGroup.restype = HRESULT
		self.AddClientEventToNotificationGroup.argtypes = [HANDLE, self.GROUP_ID, self.EventID, c_bool]

		# SIMCONNECTAPI SimConnect_RemoveClientEvent(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   SIMCONNECT_CLIENT_EVENT_ID EventID);
		self.RemoveClientEvent = SimConnect.SimConnect_RemoveClientEvent
		self.RemoveClientEvent.restype = HRESULT
		self.RemoveClientEvent.argtypes = [HANDLE, self.GROUP_ID, self.EventID]

		# SIMCONNECTAPI SimConnect_SetNotificationGroupPriority(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   DWORD uPriority);
		self.SetNotificationGroupPriority = SimConnect.SimConnect_SetNotificationGroupPriority
		self.SetNotificationGroupPriority.restype = HRESULT
		self.SetNotificationGroupPriority.argtypes = [HANDLE, self.GROUP_ID, DWORD]

		# SIMCONNECTAPI SimConnect_ClearNotificationGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID);
		self.ClearNotificationGroup = SimConnect.SimConnect_ClearNotificationGroup
		self.ClearNotificationGroup.restype = HRESULT
		self.ClearNotificationGroup.argtypes = [HANDLE, self.GROUP_ID]

		# SIMCONNECTAPI SimConnect_RequestNotificationGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   DWORD dwReserved = 0
		#   DWORD Flags = 0);
		self.RequestNotificationGroup = SimConnect.SimConnect_RequestNotificationGroup
		self.RequestNotificationGroup.restype = HRESULT
		self.RequestNotificationGroup.argtypes = [HANDLE, self.GROUP_ID, DWORD, DWORD]

		# SIMCONNECTAPI SimConnect_ClearDataDefinition(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_DEFINITION_ID DefineID);
		self.ClearDataDefinition = SimConnect.SimConnect_ClearDataDefinition
		self.ClearDataDefinition.restype = HRESULT
		self.ClearDataDefinition.argtypes = [HANDLE, self.DATA_DEFINITION_ID]

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
		self.RequestDataOnSimObject = SimConnect.SimConnect_RequestDataOnSimObject
		self.RequestDataOnSimObject.restype = HRESULT
		self.RequestDataOnSimObject.argtypes = [
			HANDLE,
			self.DATA_REQUEST_ID,
			self.DATA_DEFINITION_ID,
			SIMCONNECT_OBJECT_ID, SIMCONNECT_PERIOD,
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
		self.SetDataOnSimObject = SimConnect.SimConnect_SetDataOnSimObject
		self.SetDataOnSimObject.restype = HRESULT
		self.SetDataOnSimObject.argtypes = [
			HANDLE,
			self.DATA_DEFINITION_ID,
			SIMCONNECT_OBJECT_ID,
			SIMCONNECT_DATA_SET_FLAG,
			DWORD,
			DWORD,
			c_void_p
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
		self.MapInputEventToClientEvent = SimConnect.SimConnect_MapInputEventToClientEvent
		self.MapInputEventToClientEvent.restype = HRESULT
		self.MapInputEventToClientEvent.argtypes = [
			HANDLE,
			self.INPUT_GROUP_ID,
			c_char_p,
			self.EventID,
			DWORD,
			self.EventID,
			DWORD,
			c_bool
		]

		# SIMCONNECTAPI SimConnect_SetInputGroupPriority(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID
		#   DWORD uPriority);
		self.SetInputGroupPriority = SimConnect.SimConnect_SetInputGroupPriority
		self.SetInputGroupPriority.restype = HRESULT
		self.SetInputGroupPriority.argtypes = [HANDLE, self.INPUT_GROUP_ID, DWORD]

		# SIMCONNECTAPI SimConnect_RemoveInputEvent(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID
		#   const char * szInputDefinition);
		self.RemoveInputEvent = SimConnect.SimConnect_RemoveInputEvent
		self.RemoveInputEvent.restype = HRESULT
		self.RemoveInputEvent.argtypes = [HANDLE, self.INPUT_GROUP_ID, c_char_p]

		# SIMCONNECTAPI SimConnect_ClearInputGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID);
		self.ClearInputGroup = SimConnect.SimConnect_ClearInputGroup
		self.ClearInputGroup.restype = HRESULT
		self.ClearInputGroup.argtypes = [HANDLE, self.INPUT_GROUP_ID]

		# SIMCONNECTAPI SimConnect_SetInputGroupState(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID
		#   DWORD dwState);
		self.SetInputGroupState = SimConnect.SimConnect_SetInputGroupState
		self.SetInputGroupState.restype = HRESULT
		self.SetInputGroupState.argtypes = [HANDLE, self.INPUT_GROUP_ID, DWORD]

		# SIMCONNECTAPI SimConnect_RequestReservedKey(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   const char * szKeyChoice1 = ""
		#   const char * szKeyChoice2 = ""
		#   const char * szKeyChoice3 = "");
		self.RequestReservedKey = SimConnect.SimConnect_RequestReservedKey
		self.RequestReservedKey.restype = HRESULT
		self.RequestReservedKey.argtypes = [HANDLE, self.EventID, c_char_p, c_char_p, c_char_p]

		# SIMCONNECTAPI SimConnect_UnsubscribeFromSystemEvent(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID EventID);
		self.UnsubscribeFromSystemEvent = SimConnect.SimConnect_UnsubscribeFromSystemEvent
		self.UnsubscribeFromSystemEvent.restype = HRESULT
		self.UnsubscribeFromSystemEvent.argtypes = [HANDLE, self.EventID]

		# SIMCONNECTAPI SimConnect_WeatherRequestInterpolatedObservation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   float lat
		#   float lon
		#   float alt);
		self.WeatherRequestInterpolatedObservation = SimConnect.SimConnect_WeatherRequestInterpolatedObservation
		self.WeatherRequestInterpolatedObservation.restype = HRESULT
		self.WeatherRequestInterpolatedObservation.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_float, c_float, c_float]

		# SIMCONNECTAPI SimConnect_WeatherRequestObservationAtStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szICAO);
		self.WeatherRequestObservationAtStation = SimConnect.SimConnect_WeatherRequestObservationAtStation
		self.WeatherRequestObservationAtStation.restype = HRESULT
		self.WeatherRequestObservationAtStation.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_char_p]

		# SIMCONNECTAPI SimConnect_WeatherRequestObservationAtNearestStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   float lat
		#   float lon);
		self.WeatherRequestObservationAtNearestStation = SimConnect.SimConnect_WeatherRequestObservationAtNearestStation
		self.WeatherRequestObservationAtNearestStation.restype = HRESULT
		self.WeatherRequestObservationAtNearestStation.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_float, c_float]

		# SIMCONNECTAPI SimConnect_WeatherCreateStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szICAO
		#   const char * szName
		#   float lat
		#   float lon
		#   float alt);
		self.WeatherCreateStation = SimConnect.SimConnect_WeatherCreateStation
		self.WeatherCreateStation.restype = HRESULT
		self.WeatherCreateStation.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_char_p, c_char_p, c_float, c_float, c_float]

		# SIMCONNECTAPI SimConnect_WeatherRemoveStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szICAO);
		self.WeatherRemoveStation = SimConnect.SimConnect_WeatherRemoveStation
		self.WeatherRemoveStation.restype = HRESULT
		self.WeatherRemoveStation.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_char_p]

		# SIMCONNECTAPI SimConnect_WeatherSetObservation(
		#   HANDLE hSimConnect,
		#   DWORD Seconds
		#   const char * szMETAR);
		self.WeatherSetObservation = SimConnect.SimConnect_WeatherSetObservation
		self.WeatherSetObservation.restype = HRESULT
		self.WeatherSetObservation.argtypes = [HANDLE, DWORD, c_char_p]

		# SIMCONNECTAPI SimConnect_WeatherSetModeServer(
		#   HANDLE hSimConnect,
		#   DWORD dwPort
		#   DWORD dwSeconds);
		self.WeatherSetModeServer = SimConnect.SimConnect_WeatherSetModeServer
		self.WeatherSetModeServer.restype = HRESULT
		self.WeatherSetModeServer.argtypes = [HANDLE, DWORD, DWORD]

		# SIMCONNECTAPI SimConnect_WeatherSetModeTheme(
		#   HANDLE hSimConnect,
		#   const char * szThemeName);
		self.WeatherSetModeTheme = SimConnect.SimConnect_WeatherSetModeTheme
		self.WeatherSetModeTheme.restype = HRESULT
		self.WeatherSetModeTheme.argtypes = [HANDLE, c_char_p]

		# SIMCONNECTAPI SimConnect_WeatherSetModeGlobal(
		#   HANDLE hSimConnect);
		self.WeatherSetModeGlobal = SimConnect.SimConnect_WeatherSetModeGlobal
		self.WeatherSetModeGlobal.restype = HRESULT
		self.WeatherSetModeGlobal.argtypes = [HANDLE]

		# SIMCONNECTAPI SimConnect_WeatherSetModeCustom(
		#   HANDLE hSimConnect);
		self.WeatherSetModeCustom = SimConnect.SimConnect_WeatherSetModeCustom
		self.WeatherSetModeCustom.restype = HRESULT
		self.WeatherSetModeCustom.argtypes = [HANDLE]

		# SIMCONNECTAPI SimConnect_WeatherSetDynamicUpdateRate(
		#   HANDLE hSimConnect,
		#   DWORD dwRate);
		self.WeatherSetDynamicUpdateRate = SimConnect.SimConnect_WeatherSetDynamicUpdateRate
		self.WeatherSetDynamicUpdateRate.restype = HRESULT
		self.WeatherSetDynamicUpdateRate.argtypes = [HANDLE, DWORD]

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
		self.WeatherRequestCloudState = SimConnect.SimConnect_WeatherRequestCloudState
		self.WeatherRequestCloudState.restype = HRESULT
		self.WeatherRequestCloudState.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_float, c_float, c_float, c_float, c_float, c_float, DWORD]

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
		self.WeatherCreateThermal = SimConnect.SimConnect_WeatherCreateThermal
		self.WeatherCreateThermal.restype = HRESULT
		self.WeatherCreateThermal.argtypes = [
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
			c_float
		]

		# SIMCONNECTAPI SimConnect_WeatherRemoveThermal(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID);
		self.WeatherRemoveThermal = SimConnect.SimConnect_WeatherRemoveThermal
		self.WeatherRemoveThermal.restype = HRESULT
		self.WeatherRemoveThermal.argtypes = [HANDLE, SIMCONNECT_OBJECT_ID]

		# SIMCONNECTAPI SimConnect_AICreateParkedATCAircraft(
		#   HANDLE hSimConnect,
		#   const char * szContainerTitle
		#   const char * szTailNumber
		#   const char * szAirportID
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.AICreateParkedATCAircraft = SimConnect.SimConnect_AICreateParkedATCAircraft
		self.AICreateParkedATCAircraft.restype = HRESULT
		self.AICreateParkedATCAircraft.argtypes = [
			HANDLE,
			c_char_p,
			c_char_p,
			c_char_p,
			self.DATA_REQUEST_ID
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
		self.AICreateEnrouteATCAircraft = SimConnect.SimConnect_AICreateEnrouteATCAircraft
		self.AICreateEnrouteATCAircraft.restype = HRESULT
		self.AICreateEnrouteATCAircraft.argtypes = [
			HANDLE,
			c_char_p,
			c_char_p,
			c_int,
			c_char_p,
			c_double,
			c_bool,
			self.DATA_REQUEST_ID
		]

		# SIMCONNECTAPI SimConnect_AICreateNonATCAircraft(
		#   HANDLE hSimConnect,
		#   const char * szContainerTitle
		#   const char * szTailNumber
		#   SIMCONNECT_DATA_INITPOSITION InitPos
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.AICreateNonATCAircraft = SimConnect.SimConnect_AICreateNonATCAircraft
		self.AICreateNonATCAircraft.restype = HRESULT
		self.AICreateNonATCAircraft.argtypes = [
			HANDLE,
			c_double,
			c_double,
			SIMCONNECT_DATA_INITPOSITION,
			self.DATA_REQUEST_ID
		]

		# SIMCONNECTAPI SimConnect_AICreateSimulatedObject(
		#   HANDLE hSimConnect,
		#   const char * szContainerTitle
		#   SIMCONNECT_DATA_INITPOSITION InitPos
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.AICreateSimulatedObject = SimConnect.SimConnect_AICreateSimulatedObject
		self.AICreateSimulatedObject.restype = HRESULT
		self.AICreateSimulatedObject.argtypes = [
			HANDLE,
			c_char_p,
			SIMCONNECT_DATA_INITPOSITION,
			self.DATA_REQUEST_ID
		]

		# SIMCONNECTAPI SimConnect_AIReleaseControl(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.AIReleaseControl = SimConnect.SimConnect_AIReleaseControl
		self.AIReleaseControl.restype = HRESULT
		self.AIReleaseControl.argtypes = [
			HANDLE,
			SIMCONNECT_OBJECT_ID,
			self.DATA_REQUEST_ID
		]

		# SIMCONNECTAPI SimConnect_AIRemoveObject(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.AIRemoveObject = SimConnect.SimConnect_AIRemoveObject
		self.AIRemoveObject.restype = HRESULT
		self.AIRemoveObject.argtypes = [
			HANDLE,
			SIMCONNECT_OBJECT_ID,
			self.DATA_REQUEST_ID
		]

		# SIMCONNECTAPI SimConnect_AISetAircraftFlightPlan(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID
		#   const char * szFlightPlanPath
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.AISetAircraftFlightPlan = SimConnect.SimConnect_AISetAircraftFlightPlan
		self.AISetAircraftFlightPlan.restype = HRESULT
		self.AISetAircraftFlightPlan.argtypes = [
			HANDLE,
			SIMCONNECT_OBJECT_ID,
			c_char_p,
			self.DATA_REQUEST_ID
		]

		# SIMCONNECTAPI SimConnect_ExecuteMissionAction(
		#   HANDLE hSimConnect,
		#   const GUID guidInstanceId);
		self.ExecuteMissionAction = SimConnect.SimConnect_ExecuteMissionAction
		self.ExecuteMissionAction.restype = HRESULT
		self.ExecuteMissionAction.argtypes = []

		# SIMCONNECTAPI SimConnect_CompleteCustomMissionAction(
		#   HANDLE hSimConnect,
		#   const GUID guidInstanceId);
		self.CompleteCustomMissionAction = SimConnect.SimConnect_CompleteCustomMissionAction
		self.CompleteCustomMissionAction.restype = HRESULT
		self.CompleteCustomMissionAction.argtypes = []

		# SIMCONNECTAPI SimConnect_RetrieveString(
		#   SIMCONNECT_RECV * pData,
		#   DWORD cbData
		#   void * pStringV
		#   char ** pszString
		#   DWORD * pcbString);
		self.RetrieveString = SimConnect.SimConnect_RetrieveString
		self.RetrieveString.restype = HRESULT
		self.RetrieveString.argtypes = []

		# SIMCONNECTAPI SimConnect_GetLastSentPacketID(
		#   HANDLE hSimConnect,
		#   DWORD * pdwError);
		self.GetLastSentPacketID = SimConnect.SimConnect_GetLastSentPacketID
		self.GetLastSentPacketID.restype = HRESULT
		self.GetLastSentPacketID.argtypes = [HANDLE, DWORD]

		# SIMCONNECTAPI SimConnect_GetNextDispatch(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_RECV ** ppData
		#   DWORD * pcbData);
		self.GetNextDispatch = SimConnect.SimConnect_GetNextDispatch
		self.GetNextDispatch.restype = HRESULT
		self.GetNextDispatch.argtypes = []

		# SIMCONNECTAPI SimConnect_RequestResponseTimes(
		#   HANDLE hSimConnect,
		#   DWORD nCount
		#   float * fElapsedSeconds);
		self.RequestResponseTimes = SimConnect.SimConnect_RequestResponseTimes
		self.RequestResponseTimes.restype = HRESULT
		self.RequestResponseTimes.argtypes = [HANDLE, DWORD, c_float]

		# SIMCONNECTAPI SimConnect_InsertString(
		#   char * pDest,
		#   DWORD cbDest
		#   void ** ppEnd
		#   DWORD * pcbStringV
		#   const char * pSource);
		self.InsertString = SimConnect.SimConnect_InsertString
		self.InsertString.restype = HRESULT
		self.InsertString.argtypes = []

		# SIMCONNECTAPI SimConnect_CameraSetRelative6DOF(
		#   HANDLE hSimConnect,
		#   float fDeltaX
		#   float fDeltaY
		#   float fDeltaZ
		#   float fPitchDeg
		#   float fBankDeg
		#   float fHeadingDeg);
		self.CameraSetRelative6DOF = SimConnect.SimConnect_CameraSetRelative6DOF
		self.CameraSetRelative6DOF.restype = HRESULT
		self.CameraSetRelative6DOF.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuAddItem(
		#   HANDLE hSimConnect,
		#   const char * szMenuItem
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID
		#   DWORD dwData);
		self.MenuAddItem = SimConnect.SimConnect_MenuAddItem
		self.MenuAddItem.restype = HRESULT
		self.MenuAddItem.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuDeleteItem(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID);
		self.MenuDeleteItem = SimConnect.SimConnect_MenuDeleteItem
		self.MenuDeleteItem.restype = HRESULT
		self.MenuDeleteItem.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuAddSubItem(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID
		#   const char * szMenuItem
		#   SIMCONNECT_CLIENT_EVENT_ID SubMenuEventID
		#   DWORD dwData);
		self.MenuAddSubItem = SimConnect.SimConnect_MenuAddSubItem
		self.MenuAddSubItem.restype = HRESULT
		self.MenuAddSubItem.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuDeleteSubItem(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID
		#   const SIMCONNECT_CLIENT_EVENT_ID SubMenuEventID);
		self.MenuDeleteSubItem = SimConnect.SimConnect_MenuDeleteSubItem
		self.MenuDeleteSubItem.restype = HRESULT
		self.MenuDeleteSubItem.argtypes = []

		# SIMCONNECTAPI SimConnect_RequestSystemState(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szState);
		self.RequestSystemState = SimConnect.SimConnect_RequestSystemState
		self.RequestSystemState.restype = HRESULT
		self.RequestSystemState.argtypes = []

		# SIMCONNECTAPI SimConnect_SetSystemState(
		#   HANDLE hSimConnect,
		#   const char * szState
		#   DWORD dwInteger
		#   float fFloat
		#   const char * szString);
		self.SetSystemState = SimConnect.SimConnect_SetSystemState
		self.SetSystemState.restype = HRESULT
		self.SetSystemState.argtypes = []

		# SIMCONNECTAPI SimConnect_MapClientDataNameToID(
		#   HANDLE hSimConnect,
		#   const char * szClientDataName
		#   SIMCONNECT_CLIENT_DATA_ID ClientDataID);
		self.MapClientDataNameToID = SimConnect.SimConnect_MapClientDataNameToID
		self.MapClientDataNameToID.restype = HRESULT
		self.MapClientDataNameToID.argtypes = []

		# SIMCONNECTAPI SimConnect_CreateClientData(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_ID ClientDataID
		#   DWORD dwSize
		#   SIMCONNECT_CREATE_CLIENT_DATA_FLAG Flags);
		self.CreateClientData = SimConnect.SimConnect_CreateClientData
		self.CreateClientData.restype = HRESULT
		self.CreateClientData.argtypes = [HANDLE, self.CLIENT_DATA_ID, DWORD, SIMCONNECT_CREATE_CLIENT_DATA_FLAG]

		# SIMCONNECTAPI SimConnect_AddToClientDataDefinition(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_DEFINITION_ID DefineID
		#   DWORD dwOffset
		#   DWORD dwSizeOrType
		#   float fEpsilon = 0
		#   DWORD DatumID = SIMCONNECT_UNUSED);
		self.AddToClientDataDefinition = SimConnect.SimConnect_AddToClientDataDefinition
		self.AddToClientDataDefinition.restype = HRESULT
		self.AddToClientDataDefinition.argtypes = [HANDLE, self.CLIENT_DATA_DEFINITION_ID, DWORD, DWORD, c_float, DWORD]

		# SIMCONNECTAPI SimConnect_ClearClientDataDefinition(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_DEFINITION_ID DefineID);
		self.ClearClientDataDefinition = SimConnect.SimConnect_ClearClientDataDefinition
		self.ClearClientDataDefinition.restype = HRESULT
		self.ClearClientDataDefinition.argtypes = [HANDLE, self.CLIENT_DATA_DEFINITION_ID]

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
		self.RequestClientData = SimConnect.SimConnect_RequestClientData
		self.RequestClientData.restype = HRESULT
		self.RequestClientData.argtypes = [
			HANDLE,
			self.CLIENT_DATA_ID,
			self.DATA_REQUEST_ID,
			self.CLIENT_DATA_DEFINITION_ID,
			SIMCONNECT_CLIENT_DATA_PERIOD,
			SIMCONNECT_CLIENT_DATA_REQUEST_FLAG,
			DWORD,
			DWORD,
			DWORD
		]

		# SIMCONNECTAPI SimConnect_SetClientData(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_ID ClientDataID
		#   SIMCONNECT_CLIENT_DATA_DEFINITION_ID DefineID
		#   SIMCONNECT_CLIENT_DATA_SET_FLAG Flags
		#   DWORD dwReserved
		#   DWORD cbUnitSize
		#   void * pDataSet);
		self.SetClientData = SimConnect.SimConnect_SetClientData
		self.SetClientData.restype = HRESULT
		self.SetClientData.argtypes = [
			HANDLE,
			self.CLIENT_DATA_ID,
			self.CLIENT_DATA_DEFINITION_ID,
			SIMCONNECT_CLIENT_DATA_SET_FLAG,
			DWORD,
			DWORD,
			c_void_p
		]

		# SIMCONNECTAPI SimConnect_FlightLoad(
		#   HANDLE hSimConnect,
		#   const char * szFileName);
		self.FlightLoad = SimConnect.SimConnect_FlightLoad
		self.FlightLoad.restype = HRESULT
		self.FlightLoad.argtypes = [HANDLE, c_char_p]

		# SIMCONNECTAPI SimConnect_FlightSave(
		#   HANDLE hSimConnect,
		#   const char * szFileName
		#   const char * szTitle
		#   const char * szDescription
		#   DWORD Flags);
		self.FlightSave = SimConnect.SimConnect_FlightSave
		self.FlightSave.restype = HRESULT
		self.FlightSave.argtypes = [HANDLE, c_char_p, c_char_p, c_char_p, DWORD]

		# SIMCONNECTAPI SimConnect_FlightPlanLoad(
		#   HANDLE hSimConnect,
		#   const char * szFileName);
		self.FlightPlanLoad = SimConnect.SimConnect_FlightPlanLoad
		self.FlightPlanLoad.restype = HRESULT
		self.FlightPlanLoad.argtypes = [HANDLE, c_char_p]

		# SIMCONNECTAPI SimConnect_Text(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_TEXT_TYPE type
		#   float fTimeSeconds
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   DWORD cbUnitSize
		#   void * pDataSet);
		self.Text = SimConnect.SimConnect_Text
		self.Text.restype = HRESULT
		self.Text.argtypes = [HANDLE, SIMCONNECT_TEXT_TYPE, c_float, self.EventID, DWORD, c_void_p]

		# SIMCONNECTAPI SimConnect_SubscribeToFacilities(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_FACILITY_LIST_TYPE type
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.SubscribeToFacilities = SimConnect.SimConnect_SubscribeToFacilities
		self.SubscribeToFacilities.restype = HRESULT
		self.SubscribeToFacilities.argtypes = [HANDLE, SIMCONNECT_FACILITY_LIST_TYPE, self.DATA_REQUEST_ID]

		# SIMCONNECTAPI SimConnect_UnsubscribeToFacilities(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_FACILITY_LIST_TYPE type);
		self.UnsubscribeToFacilities = SimConnect.SimConnect_UnsubscribeToFacilities
		self.UnsubscribeToFacilities.restype = HRESULT
		self.UnsubscribeToFacilities.argtypes = [HANDLE, SIMCONNECT_FACILITY_LIST_TYPE]

		# SIMCONNECTAPI SimConnect_RequestFacilitiesList(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_FACILITY_LIST_TYPE type
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.RequestFacilitiesList = SimConnect.SimConnect_RequestFacilitiesList
		self.RequestFacilitiesList.restype = HRESULT
		self.RequestFacilitiesList.argtypes = [HANDLE, SIMCONNECT_FACILITY_LIST_TYPE, self.DATA_REQUEST_ID]

		self.hSimConnect = HANDLE()
		self.quit = 0
		self.MyDispatchProcRD = DispatchProc(self.MyDispatchProc)
		#self.haveData = False

	def setup(self):
		try:
			err = self.Open(byref(self.hSimConnect), LPCSTR(b"Request Data"), None, 0, 0, 0)
			if IsHR(err, 0):
				print("Connected to Flight Simulator!")
				# Set up the data definition, but do not yet do anything with itd
				# Request an event when the simulation starts
				self.SubscribeToSystemEvent(self.hSimConnect, self.EventID.EVENT_SIM_START, b'SimStart')
		except OSError:
			print("Did not find Flight Simulator running.")
			exit(0)

	def run(self):
		for deff in self.out_data:
			self.out_data[deff] = None
		self.CallDispatch(self.hSimConnect, self.MyDispatchProcRD, None)

	def exit(self):
		self.Close(self.hSimConnect)

	def Add_Definition(self, _Request):
		self.Requests.append(_Request)
		self.out_data[_Request.DATA_REQUEST_ID] = None
		for deff in _Request.definitions:
			self.AddToDataDefinition(
				self.hSimConnect,
				_Request.DATA_DEFINITION_ID,
				deff[0], deff[1],
				SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_FLOAT64,
				0,
				SIMCONNECT_UNUSED
			)

	def MapToSimEvent(self, name, evnt):
		err = self.MapClientEventToSimEvent(self.hSimConnect, evnt, name)
		if IsHR(err, 0):
			pass
		else:
			print("Error: MapToSimEvent")

	def AddToNotificationGroup(self, group, evnt, bMaskable=False):
		self.AddClientEventToNotificationGroup(self.hSimConnect, group, evnt, bMaskable)

	def RequestData(self, _Request):
		self.out_data[_Request.DATA_REQUEST_ID] = None
		self.RequestDataOnSimObjectType(
			self.hSimConnect, _Request.DATA_REQUEST_ID,
			_Request.DATA_DEFINITION_ID,
			0,
			SIMCONNECT_SIMOBJECT_TYPE.SIMCONNECT_SIMOBJECT_TYPE_USER
		)

	def SendData(self, evnt, data=DWORD(0)):
		err = self.TransmitClientEvent(
			self.hSimConnect,
			SIMCONNECT_OBJECT_ID_USER,
			evnt,
			data,
			SIMCONNECT_GROUP_PRIORITY_HIGHEST,
			DWORD(16)
		)
		if IsHR(err, 0):
			print("Sent Event")
