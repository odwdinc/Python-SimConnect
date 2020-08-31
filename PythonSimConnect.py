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


class AutoName(CtypesEnum):
	def _generate_next_value_(name, start, count, last_values):
		return count


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
class SIMCONNECT_NOTIFICATION_GROUP_ID(AutoName):  # client-defined notification group ID
	pass


class SIMCONNECT_INPUT_GROUP_ID(AutoName):  # client-defined input group ID
	pass


class SIMCONNECT_DATA_DEFINITION_ID(AutoName):  # client-defined data definition ID
	pass


class SIMCONNECT_DATA_REQUEST_ID(AutoName):  # client-defined request data ID
	pass


class SIMCONNECT_CLIENT_EVENT_ID(AutoName):  # client-defined client event ID
	EVENT_SIM_START = auto()
	pass


class SIMCONNECT_CLIENT_DATA_ID(AutoName):  # client-defined client data ID
	pass


class SIMCONNECT_CLIENT_DATA_DEFINITION_ID(AutoName):  # client-defined client data definition ID
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


class sData(dict):
	__getattr__ = dict.__getitem__
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__


class Request():
	def __init__(self, _name, _time=None, _DATA_DEFINITION_ID=SIMCONNECT_DATA_DEFINITION_ID, _DATA_REQUEST_ID=SIMCONNECT_DATA_REQUEST_ID, _psc=None):
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
			deff[0], deff[1],
			SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_FLOAT64,
			0,
			SIMCONNECT_UNUSED
		)


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
				if dwRequestID == _request.DATA_REQUEST_ID.value:
					self.out_data[_request.DATA_REQUEST_ID] = cast(pObjData.dwData, POINTER(c_double * 200)).contents
		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_OPEN:
			print("SIM OPEN")

		elif dwID == SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_QUIT:
			self.quit = 1
		else:
			print("Received:", dwID)
		return

	def __init__(self):

		self.EventID = SIMCONNECT_CLIENT_EVENT_ID
		self.DATA_DEFINITION_ID = SIMCONNECT_DATA_DEFINITION_ID
		self.DATA_REQUEST_ID = SIMCONNECT_DATA_REQUEST_ID
		self.GROUP_ID = SIMCONNECT_NOTIFICATION_GROUP_ID
		self.INPUT_GROUP_ID = SIMCONNECT_INPUT_GROUP_ID
		self.CLIENT_DATA_ID = SIMCONNECT_CLIENT_DATA_ID
		self.CLIENT_DATA_DEFINITION_ID = SIMCONNECT_CLIENT_DATA_DEFINITION_ID

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

		self.__Open = SimConnect.SimConnect_Open
		self.__Open.restype = HRESULT
		self.__Open.argtypes = [POINTER(HANDLE), LPCSTR, HWND, DWORD, HANDLE, DWORD]

		#SIMCONNECTAPI SimConnect_Close(
		#	HANDLE hSimConnect);

		self.__Close = SimConnect.SimConnect_Close
		self.__Close.restype = HRESULT
		self.__Close.argtypes = [HANDLE]

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

		self.__SubscribeToSystemEvent = SimConnect.SimConnect_SubscribeToSystemEvent
		self.__SubscribeToSystemEvent.restype = HRESULT
		self.__SubscribeToSystemEvent.argtypes = [HANDLE, self.EventID, c_char_p]

		#SIMCONNECTAPI SimConnect_CallDispatch(
		#	HANDLE hSimConnect,
		#	DispatchProc pfcnDispatch,
		#	void * pContext);

		DispatchProc = CFUNCTYPE(c_void_p, POINTER(SIMCONNECT_RECV), DWORD, c_void_p)

		self.__CallDispatch = SimConnect.SimConnect_CallDispatch
		self.__CallDispatch.restype = HRESULT
		self.__CallDispatch.argtypes = [HANDLE, DispatchProc, c_void_p]

		#SIMCONNECTAPI SimConnect_RequestDataOnSimObjectType(
		#	HANDLE hSimConnect,
		#	SIMCONNECT_DATA_REQUEST_ID RequestID,
		#	SIMCONNECT_DATA_DEFINITION_ID DefineID,
		#	DWORD dwRadiusMeters,
		#	SIMCONNECT_SIMOBJECT_TYPE type);

		self.__RequestDataOnSimObjectType = SimConnect.SimConnect_RequestDataOnSimObjectType
		self.__RequestDataOnSimObjectType.restype = HRESULT
		self.__RequestDataOnSimObjectType.argtypes = [HANDLE, self.DATA_REQUEST_ID, self.DATA_DEFINITION_ID, DWORD, SIMCONNECT_SIMOBJECT_TYPE]

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

		self.__TransmitClientEvent = SimConnect.SimConnect_TransmitClientEvent
		self.__TransmitClientEvent.restype = HRESULT
		self.__TransmitClientEvent.argtypes = [HANDLE, SIMCONNECT_OBJECT_ID, self.EventID, DWORD, DWORD, DWORD]

		#SIMCONNECTAPI SimConnect_MapClientEventToSimEvent(
		#	HANDLE hSimConnect,
		#	SIMCONNECT_CLIENT_EVENT_ID EventID,
		#	const char * EventName = "");

		self.__MapClientEventToSimEvent = SimConnect.SimConnect_MapClientEventToSimEvent
		self.__MapClientEventToSimEvent.restype = HRESULT
		self.__MapClientEventToSimEvent.argtypes = [HANDLE, self.EventID, c_char_p]

		#SIMCONNECTAPI SimConnect_AddClientEventToNotificationGroup(
		#	HANDLE hSimConnect,
		#	SIMCONNECT_NOTIFICATION_GROUP_ID GroupID,
		#	SIMCONNECT_CLIENT_EVENT_ID EventID,
		#	BOOL bMaskable = FALSE);

		self.__AddClientEventToNotificationGroup = SimConnect.SimConnect_AddClientEventToNotificationGroup
		self.__AddClientEventToNotificationGroup.restype = HRESULT
		self.__AddClientEventToNotificationGroup.argtypes = [HANDLE, self.GROUP_ID, self.EventID, c_bool]

		# SIMCONNECTAPI SimConnect_SetSystemEventState(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   SIMCONNECT_STATE dwState);
		self.__SetSystemEventState = SimConnect.SimConnect_SetSystemEventState
		self.__SetSystemEventState.restype = HRESULT
		self.__SetSystemEventState.argtypes = [HANDLE, self.EventID, SIMCONNECT_STATE]

		# SIMCONNECTAPI SimConnect_AddClientEventToNotificationGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   BOOL bMaskable = FALSE);
		self.__AddClientEventToNotificationGroup = SimConnect.SimConnect_AddClientEventToNotificationGroup
		self.__AddClientEventToNotificationGroup.restype = HRESULT
		self.__AddClientEventToNotificationGroup.argtypes = [HANDLE, self.GROUP_ID, self.EventID, c_bool]

		# SIMCONNECTAPI SimConnect_RemoveClientEvent(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   SIMCONNECT_CLIENT_EVENT_ID EventID);
		self.__RemoveClientEvent = SimConnect.SimConnect_RemoveClientEvent
		self.__RemoveClientEvent.restype = HRESULT
		self.__RemoveClientEvent.argtypes = [HANDLE, self.GROUP_ID, self.EventID]

		# SIMCONNECTAPI SimConnect_SetNotificationGroupPriority(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   DWORD uPriority);
		self.__SetNotificationGroupPriority = SimConnect.SimConnect_SetNotificationGroupPriority
		self.__SetNotificationGroupPriority.restype = HRESULT
		self.__SetNotificationGroupPriority.argtypes = [HANDLE, self.GROUP_ID, DWORD]

		# SIMCONNECTAPI SimConnect_ClearNotificationGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID);
		self.__ClearNotificationGroup = SimConnect.SimConnect_ClearNotificationGroup
		self.__ClearNotificationGroup.restype = HRESULT
		self.__ClearNotificationGroup.argtypes = [HANDLE, self.GROUP_ID]

		# SIMCONNECTAPI SimConnect_RequestNotificationGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_NOTIFICATION_GROUP_ID GroupID
		#   DWORD dwReserved = 0
		#   DWORD Flags = 0);
		self.__RequestNotificationGroup = SimConnect.SimConnect_RequestNotificationGroup
		self.__RequestNotificationGroup.restype = HRESULT
		self.__RequestNotificationGroup.argtypes = [HANDLE, self.GROUP_ID, DWORD, DWORD]

		# SIMCONNECTAPI SimConnect_ClearDataDefinition(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_DEFINITION_ID DefineID);
		self.__ClearDataDefinition = SimConnect.SimConnect_ClearDataDefinition
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
		self.__RequestDataOnSimObject = SimConnect.SimConnect_RequestDataOnSimObject
		self.__RequestDataOnSimObject.restype = HRESULT
		self.__RequestDataOnSimObject.argtypes = [
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
		self.__SetDataOnSimObject = SimConnect.SimConnect_SetDataOnSimObject
		self.__SetDataOnSimObject.restype = HRESULT
		self.__SetDataOnSimObject.argtypes = [
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
		self.__MapInputEventToClientEvent = SimConnect.SimConnect_MapInputEventToClientEvent
		self.__MapInputEventToClientEvent.restype = HRESULT
		self.__MapInputEventToClientEvent.argtypes = [
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
		self.__SetInputGroupPriority = SimConnect.SimConnect_SetInputGroupPriority
		self.__SetInputGroupPriority.restype = HRESULT
		self.__SetInputGroupPriority.argtypes = [HANDLE, self.INPUT_GROUP_ID, DWORD]

		# SIMCONNECTAPI SimConnect_RemoveInputEvent(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID
		#   const char * szInputDefinition);
		self.__RemoveInputEvent = SimConnect.SimConnect_RemoveInputEvent
		self.__RemoveInputEvent.restype = HRESULT
		self.__RemoveInputEvent.argtypes = [HANDLE, self.INPUT_GROUP_ID, c_char_p]

		# SIMCONNECTAPI SimConnect_ClearInputGroup(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID);
		self.__ClearInputGroup = SimConnect.SimConnect_ClearInputGroup
		self.__ClearInputGroup.restype = HRESULT
		self.__ClearInputGroup.argtypes = [HANDLE, self.INPUT_GROUP_ID]

		# SIMCONNECTAPI SimConnect_SetInputGroupState(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_INPUT_GROUP_ID GroupID
		#   DWORD dwState);
		self.__SetInputGroupState = SimConnect.SimConnect_SetInputGroupState
		self.__SetInputGroupState.restype = HRESULT
		self.__SetInputGroupState.argtypes = [HANDLE, self.INPUT_GROUP_ID, DWORD]

		# SIMCONNECTAPI SimConnect_RequestReservedKey(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   const char * szKeyChoice1 = ""
		#   const char * szKeyChoice2 = ""
		#   const char * szKeyChoice3 = "");
		self.__RequestReservedKey = SimConnect.SimConnect_RequestReservedKey
		self.__RequestReservedKey.restype = HRESULT
		self.__RequestReservedKey.argtypes = [HANDLE, self.EventID, c_char_p, c_char_p, c_char_p]

		# SIMCONNECTAPI SimConnect_UnsubscribeFromSystemEvent(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID EventID);
		self.__UnsubscribeFromSystemEvent = SimConnect.SimConnect_UnsubscribeFromSystemEvent
		self.__UnsubscribeFromSystemEvent.restype = HRESULT
		self.__UnsubscribeFromSystemEvent.argtypes = [HANDLE, self.EventID]

		# SIMCONNECTAPI SimConnect_WeatherRequestInterpolatedObservation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   float lat
		#   float lon
		#   float alt);
		self.__WeatherRequestInterpolatedObservation = SimConnect.SimConnect_WeatherRequestInterpolatedObservation
		self.__WeatherRequestInterpolatedObservation.restype = HRESULT
		self.__WeatherRequestInterpolatedObservation.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_float, c_float, c_float]

		# SIMCONNECTAPI SimConnect_WeatherRequestObservationAtStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szICAO);
		self.__WeatherRequestObservationAtStation = SimConnect.SimConnect_WeatherRequestObservationAtStation
		self.__WeatherRequestObservationAtStation.restype = HRESULT
		self.__WeatherRequestObservationAtStation.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_char_p]

		# SIMCONNECTAPI SimConnect_WeatherRequestObservationAtNearestStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   float lat
		#   float lon);
		self.__WeatherRequestObservationAtNearestStation = SimConnect.SimConnect_WeatherRequestObservationAtNearestStation
		self.__WeatherRequestObservationAtNearestStation.restype = HRESULT
		self.__WeatherRequestObservationAtNearestStation.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_float, c_float]

		# SIMCONNECTAPI SimConnect_WeatherCreateStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szICAO
		#   const char * szName
		#   float lat
		#   float lon
		#   float alt);
		self.__WeatherCreateStation = SimConnect.SimConnect_WeatherCreateStation
		self.__WeatherCreateStation.restype = HRESULT
		self.__WeatherCreateStation.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_char_p, c_char_p, c_float, c_float, c_float]

		# SIMCONNECTAPI SimConnect_WeatherRemoveStation(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szICAO);
		self.__WeatherRemoveStation = SimConnect.SimConnect_WeatherRemoveStation
		self.__WeatherRemoveStation.restype = HRESULT
		self.__WeatherRemoveStation.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_char_p]

		# SIMCONNECTAPI SimConnect_WeatherSetObservation(
		#   HANDLE hSimConnect,
		#   DWORD Seconds
		#   const char * szMETAR);
		self.__WeatherSetObservation = SimConnect.SimConnect_WeatherSetObservation
		self.__WeatherSetObservation.restype = HRESULT
		self.__WeatherSetObservation.argtypes = [HANDLE, DWORD, c_char_p]

		# SIMCONNECTAPI SimConnect_WeatherSetModeServer(
		#   HANDLE hSimConnect,
		#   DWORD dwPort
		#   DWORD dwSeconds);
		self.__WeatherSetModeServer = SimConnect.SimConnect_WeatherSetModeServer
		self.__WeatherSetModeServer.restype = HRESULT
		self.__WeatherSetModeServer.argtypes = [HANDLE, DWORD, DWORD]

		# SIMCONNECTAPI SimConnect_WeatherSetModeTheme(
		#   HANDLE hSimConnect,
		#   const char * szThemeName);
		self.__WeatherSetModeTheme = SimConnect.SimConnect_WeatherSetModeTheme
		self.__WeatherSetModeTheme.restype = HRESULT
		self.__WeatherSetModeTheme.argtypes = [HANDLE, c_char_p]

		# SIMCONNECTAPI SimConnect_WeatherSetModeGlobal(
		#   HANDLE hSimConnect);
		self.__WeatherSetModeGlobal = SimConnect.SimConnect_WeatherSetModeGlobal
		self.__WeatherSetModeGlobal.restype = HRESULT
		self.__WeatherSetModeGlobal.argtypes = [HANDLE]

		# SIMCONNECTAPI SimConnect_WeatherSetModeCustom(
		#   HANDLE hSimConnect);
		self.__WeatherSetModeCustom = SimConnect.SimConnect_WeatherSetModeCustom
		self.__WeatherSetModeCustom.restype = HRESULT
		self.__WeatherSetModeCustom.argtypes = [HANDLE]

		# SIMCONNECTAPI SimConnect_WeatherSetDynamicUpdateRate(
		#   HANDLE hSimConnect,
		#   DWORD dwRate);
		self.__WeatherSetDynamicUpdateRate = SimConnect.SimConnect_WeatherSetDynamicUpdateRate
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
		self.__WeatherRequestCloudState = SimConnect.SimConnect_WeatherRequestCloudState
		self.__WeatherRequestCloudState.restype = HRESULT
		self.__WeatherRequestCloudState.argtypes = [HANDLE, self.DATA_REQUEST_ID, c_float, c_float, c_float, c_float, c_float, c_float, DWORD]

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
		self.__WeatherCreateThermal = SimConnect.SimConnect_WeatherCreateThermal
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
			c_float
		]

		# SIMCONNECTAPI SimConnect_WeatherRemoveThermal(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID);
		self.__WeatherRemoveThermal = SimConnect.SimConnect_WeatherRemoveThermal
		self.__WeatherRemoveThermal.restype = HRESULT
		self.__WeatherRemoveThermal.argtypes = [HANDLE, SIMCONNECT_OBJECT_ID]

		# SIMCONNECTAPI SimConnect_AICreateParkedATCAircraft(
		#   HANDLE hSimConnect,
		#   const char * szContainerTitle
		#   const char * szTailNumber
		#   const char * szAirportID
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__AICreateParkedATCAircraft = SimConnect.SimConnect_AICreateParkedATCAircraft
		self.__AICreateParkedATCAircraft.restype = HRESULT
		self.__AICreateParkedATCAircraft.argtypes = [
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
		self.__AICreateEnrouteATCAircraft = SimConnect.SimConnect_AICreateEnrouteATCAircraft
		self.__AICreateEnrouteATCAircraft.restype = HRESULT
		self.__AICreateEnrouteATCAircraft.argtypes = [
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
		self.__AICreateNonATCAircraft = SimConnect.SimConnect_AICreateNonATCAircraft
		self.__AICreateNonATCAircraft.restype = HRESULT
		self.__AICreateNonATCAircraft.argtypes = [
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
		self.__AICreateSimulatedObject = SimConnect.SimConnect_AICreateSimulatedObject
		self.__AICreateSimulatedObject.restype = HRESULT
		self.__AICreateSimulatedObject.argtypes = [
			HANDLE,
			c_char_p,
			SIMCONNECT_DATA_INITPOSITION,
			self.DATA_REQUEST_ID
		]

		# SIMCONNECTAPI SimConnect_AIReleaseControl(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__AIReleaseControl = SimConnect.SimConnect_AIReleaseControl
		self.__AIReleaseControl.restype = HRESULT
		self.__AIReleaseControl.argtypes = [
			HANDLE,
			SIMCONNECT_OBJECT_ID,
			self.DATA_REQUEST_ID
		]

		# SIMCONNECTAPI SimConnect_AIRemoveObject(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__AIRemoveObject = SimConnect.SimConnect_AIRemoveObject
		self.__AIRemoveObject.restype = HRESULT
		self.__AIRemoveObject.argtypes = [
			HANDLE,
			SIMCONNECT_OBJECT_ID,
			self.DATA_REQUEST_ID
		]

		# SIMCONNECTAPI SimConnect_AISetAircraftFlightPlan(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_OBJECT_ID ObjectID
		#   const char * szFlightPlanPath
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__AISetAircraftFlightPlan = SimConnect.SimConnect_AISetAircraftFlightPlan
		self.__AISetAircraftFlightPlan.restype = HRESULT
		self.__AISetAircraftFlightPlan.argtypes = [
			HANDLE,
			SIMCONNECT_OBJECT_ID,
			c_char_p,
			self.DATA_REQUEST_ID
		]

		# SIMCONNECTAPI SimConnect_ExecuteMissionAction(
		#   HANDLE hSimConnect,
		#   const GUID guidInstanceId);
		self.__ExecuteMissionAction = SimConnect.SimConnect_ExecuteMissionAction
		self.__ExecuteMissionAction.restype = HRESULT
		self.__ExecuteMissionAction.argtypes = []

		# SIMCONNECTAPI SimConnect_CompleteCustomMissionAction(
		#   HANDLE hSimConnect,
		#   const GUID guidInstanceId);
		self.__CompleteCustomMissionAction = SimConnect.SimConnect_CompleteCustomMissionAction
		self.__CompleteCustomMissionAction.restype = HRESULT
		self.__CompleteCustomMissionAction.argtypes = []

		# SIMCONNECTAPI SimConnect_RetrieveString(
		#   SIMCONNECT_RECV * pData,
		#   DWORD cbData
		#   void * pStringV
		#   char ** pszString
		#   DWORD * pcbString);
		self.__RetrieveString = SimConnect.SimConnect_RetrieveString
		self.__RetrieveString.restype = HRESULT
		self.__RetrieveString.argtypes = []

		# SIMCONNECTAPI SimConnect_GetLastSentPacketID(
		#   HANDLE hSimConnect,
		#   DWORD * pdwError);
		self.__GetLastSentPacketID = SimConnect.SimConnect_GetLastSentPacketID
		self.__GetLastSentPacketID.restype = HRESULT
		self.__GetLastSentPacketID.argtypes = [HANDLE, DWORD]

		# SIMCONNECTAPI SimConnect_GetNextDispatch(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_RECV ** ppData
		#   DWORD * pcbData);
		self.__GetNextDispatch = SimConnect.SimConnect_GetNextDispatch
		self.__GetNextDispatch.restype = HRESULT
		self.__GetNextDispatch.argtypes = []

		# SIMCONNECTAPI SimConnect_RequestResponseTimes(
		#   HANDLE hSimConnect,
		#   DWORD nCount
		#   float * fElapsedSeconds);
		self.__RequestResponseTimes = SimConnect.SimConnect_RequestResponseTimes
		self.__RequestResponseTimes.restype = HRESULT
		self.__RequestResponseTimes.argtypes = [HANDLE, DWORD, c_float]

		# SIMCONNECTAPI SimConnect_InsertString(
		#   char * pDest,
		#   DWORD cbDest
		#   void ** ppEnd
		#   DWORD * pcbStringV
		#   const char * pSource);
		self.__InsertString = SimConnect.SimConnect_InsertString
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
		self.__CameraSetRelative6DOF = SimConnect.SimConnect_CameraSetRelative6DOF
		self.__CameraSetRelative6DOF.restype = HRESULT
		self.__CameraSetRelative6DOF.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuAddItem(
		#   HANDLE hSimConnect,
		#   const char * szMenuItem
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID
		#   DWORD dwData);
		self.__MenuAddItem = SimConnect.SimConnect_MenuAddItem
		self.__MenuAddItem.restype = HRESULT
		self.__MenuAddItem.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuDeleteItem(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID);
		self.__MenuDeleteItem = SimConnect.SimConnect_MenuDeleteItem
		self.__MenuDeleteItem.restype = HRESULT
		self.__MenuDeleteItem.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuAddSubItem(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID
		#   const char * szMenuItem
		#   SIMCONNECT_CLIENT_EVENT_ID SubMenuEventID
		#   DWORD dwData);
		self.__MenuAddSubItem = SimConnect.SimConnect_MenuAddSubItem
		self.__MenuAddSubItem.restype = HRESULT
		self.__MenuAddSubItem.argtypes = []

		# SIMCONNECTAPI SimConnect_MenuDeleteSubItem(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_EVENT_ID MenuEventID
		#   const SIMCONNECT_CLIENT_EVENT_ID SubMenuEventID);
		self.__MenuDeleteSubItem = SimConnect.SimConnect_MenuDeleteSubItem
		self.__MenuDeleteSubItem.restype = HRESULT
		self.__MenuDeleteSubItem.argtypes = []

		# SIMCONNECTAPI SimConnect_RequestSystemState(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_DATA_REQUEST_ID RequestID
		#   const char * szState);
		self.__RequestSystemState = SimConnect.SimConnect_RequestSystemState
		self.__RequestSystemState.restype = HRESULT
		self.__RequestSystemState.argtypes = []

		# SIMCONNECTAPI SimConnect_SetSystemState(
		#   HANDLE hSimConnect,
		#   const char * szState
		#   DWORD dwInteger
		#   float fFloat
		#   const char * szString);
		self.__SetSystemState = SimConnect.SimConnect_SetSystemState
		self.__SetSystemState.restype = HRESULT
		self.__SetSystemState.argtypes = []

		# SIMCONNECTAPI SimConnect_MapClientDataNameToID(
		#   HANDLE hSimConnect,
		#   const char * szClientDataName
		#   SIMCONNECT_CLIENT_DATA_ID ClientDataID);
		self.__MapClientDataNameToID = SimConnect.SimConnect_MapClientDataNameToID
		self.__MapClientDataNameToID.restype = HRESULT
		self.__MapClientDataNameToID.argtypes = []

		# SIMCONNECTAPI SimConnect_CreateClientData(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_ID ClientDataID
		#   DWORD dwSize
		#   SIMCONNECT_CREATE_CLIENT_DATA_FLAG Flags);
		self.__CreateClientData = SimConnect.SimConnect_CreateClientData
		self.__CreateClientData.restype = HRESULT
		self.__CreateClientData.argtypes = [HANDLE, self.CLIENT_DATA_ID, DWORD, SIMCONNECT_CREATE_CLIENT_DATA_FLAG]

		# SIMCONNECTAPI SimConnect_AddToClientDataDefinition(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_DEFINITION_ID DefineID
		#   DWORD dwOffset
		#   DWORD dwSizeOrType
		#   float fEpsilon = 0
		#   DWORD DatumID = SIMCONNECT_UNUSED);
		self.__AddToClientDataDefinition = SimConnect.SimConnect_AddToClientDataDefinition
		self.__AddToClientDataDefinition.restype = HRESULT
		self.__AddToClientDataDefinition.argtypes = [HANDLE, self.CLIENT_DATA_DEFINITION_ID, DWORD, DWORD, c_float, DWORD]

		# SIMCONNECTAPI SimConnect_ClearClientDataDefinition(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_CLIENT_DATA_DEFINITION_ID DefineID);
		self.__ClearClientDataDefinition = SimConnect.SimConnect_ClearClientDataDefinition
		self.__ClearClientDataDefinition.restype = HRESULT
		self.__ClearClientDataDefinition.argtypes = [HANDLE, self.CLIENT_DATA_DEFINITION_ID]

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
		self.__RequestClientData = SimConnect.SimConnect_RequestClientData
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
		self.__SetClientData = SimConnect.SimConnect_SetClientData
		self.__SetClientData.restype = HRESULT
		self.__SetClientData.argtypes = [
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
		self.__FlightLoad = SimConnect.SimConnect_FlightLoad
		self.__FlightLoad.restype = HRESULT
		self.__FlightLoad.argtypes = [HANDLE, c_char_p]

		# SIMCONNECTAPI SimConnect_FlightSave(
		#   HANDLE hSimConnect,
		#   const char * szFileName
		#   const char * szTitle
		#   const char * szDescription
		#   DWORD Flags);
		self.__FlightSave = SimConnect.SimConnect_FlightSave
		self.__FlightSave.restype = HRESULT
		self.__FlightSave.argtypes = [HANDLE, c_char_p, c_char_p, c_char_p, DWORD]

		# SIMCONNECTAPI SimConnect_FlightPlanLoad(
		#   HANDLE hSimConnect,
		#   const char * szFileName);
		self.__FlightPlanLoad = SimConnect.SimConnect_FlightPlanLoad
		self.__FlightPlanLoad.restype = HRESULT
		self.__FlightPlanLoad.argtypes = [HANDLE, c_char_p]

		# SIMCONNECTAPI SimConnect_Text(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_TEXT_TYPE type
		#   float fTimeSeconds
		#   SIMCONNECT_CLIENT_EVENT_ID EventID
		#   DWORD cbUnitSize
		#   void * pDataSet);
		self.__Text = SimConnect.SimConnect_Text
		self.__Text.restype = HRESULT
		self.__Text.argtypes = [HANDLE, SIMCONNECT_TEXT_TYPE, c_float, self.EventID, DWORD, c_void_p]

		# SIMCONNECTAPI SimConnect_SubscribeToFacilities(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_FACILITY_LIST_TYPE type
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.__SubscribeToFacilities = SimConnect.SimConnect_SubscribeToFacilities
		self.__SubscribeToFacilities.restype = HRESULT
		self.__SubscribeToFacilities.argtypes = [HANDLE, SIMCONNECT_FACILITY_LIST_TYPE, self.DATA_REQUEST_ID]

		# SIMCONNECTAPI SimConnect_UnsubscribeToFacilities(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_FACILITY_LIST_TYPE type);
		self.__UnsubscribeToFacilities = SimConnect.SimConnect_UnsubscribeToFacilities
		self.__UnsubscribeToFacilities.restype = HRESULT
		self.__UnsubscribeToFacilities.argtypes = [HANDLE, SIMCONNECT_FACILITY_LIST_TYPE]

		# SIMCONNECTAPI SimConnect_RequestFacilitiesList(
		#   HANDLE hSimConnect,
		#   SIMCONNECT_FACILITY_LIST_TYPE type
		#   SIMCONNECT_DATA_REQUEST_ID RequestID);
		self.____RequestFacilitiesList = SimConnect.SimConnect_RequestFacilitiesList
		self.____RequestFacilitiesList.restype = HRESULT
		self.____RequestFacilitiesList.argtypes = [HANDLE, SIMCONNECT_FACILITY_LIST_TYPE, self.DATA_REQUEST_ID]

		self.hSimConnect = HANDLE()
		self.quit = 0
		self.MyDispatchProcRD = DispatchProc(self.MyDispatchProc)
		#self.haveData = False

		try:
			err = self.__Open(byref(self.hSimConnect), LPCSTR(b"Request Data"), None, 0, 0, 0)
			if IsHR(err, 0):
				print("Connected to Flight Simulator!")
				# Set up the data definition, but do not yet do anything with itd
				# Request an event when the simulation starts
				self.__SubscribeToSystemEvent(self.hSimConnect, self.EventID.EVENT_SIM_START, b'SimStart')
		except OSError:
			print("Did not find Flight Simulator running.")
			exit(0)

	def Run(self):
		for _request in self.Requests:
			self.out_data[_request.DATA_REQUEST_ID] = None
			if _request.time is not None:
				if (_request.timeout + _request.time) < millis():
					self.RequestData(_request)
					_request.timeout = millis()

		self.__CallDispatch(self.hSimConnect, self.MyDispatchProcRD, None)

	def Exit(self):
		self.__Close(self.hSimConnect)

	def MapToSimEvent(self, name):
		for m in self.EventID:
			if name.decode() == m.name:
				print("Allrady have event: ", m)
				return m

		names = [m.name for m in self.EventID] + [name.decode()]
		self.EventID = Enum(self.EventID.__name__, names)
		evnt = list(self.EventID)[-1]
		err = self.__MapClientEventToSimEvent(self.hSimConnect, evnt.value, name)
		if IsHR(err, 0):
			return evnt
		else:
			print("Error: MapToSimEvent")
			return None

	def AddToNotificationGroup(self, group, evnt, bMaskable=False):
		self.__AddClientEventToNotificationGroup(self.hSimConnect, group, evnt, bMaskable)

	def RequestData(self, _Request):
		self.out_data[_Request.DATA_REQUEST_ID] = None
		self.__RequestDataOnSimObjectType(
			self.hSimConnect, _Request.DATA_REQUEST_ID.value,
			_Request.DATA_DEFINITION_ID.value,
			0,
			SIMCONNECT_SIMOBJECT_TYPE.SIMCONNECT_SIMOBJECT_TYPE_USER
		)

	def GetData(self, _Request):
		if self.out_data[_Request.DATA_REQUEST_ID] is None:
			return None
		map = sData
		for od in _Request.outData:
			setattr(sData, od, self.out_data[_Request.DATA_REQUEST_ID][_Request.outData[od]])
		return map

	def SendData(self, evnt, data=DWORD(0)):
		err = self.__TransmitClientEvent(
			self.hSimConnect,
			SIMCONNECT_OBJECT_ID_USER,
			evnt.value,
			data,
			SIMCONNECT_GROUP_PRIORITY_HIGHEST,
			DWORD(16)
		)
		if IsHR(err, 0):
			print("Event Sent")

	def newRequest(self, time=None):
		name = "Request" + str(len(self.Requests))
		names = [m.name for m in self.DATA_DEFINITION_ID] + [name]
		self.DATA_DEFINITION_ID = Enum(self.DATA_DEFINITION_ID.__name__, names)
		DEFINITION_ID = list(self.DATA_DEFINITION_ID)[-1]

		names = [m.name for m in self.DATA_REQUEST_ID] + [name]
		self.DATA_REQUEST_ID = Enum(self.DATA_REQUEST_ID.__name__, names)
		REQUEST_ID = list(self.DATA_REQUEST_ID)[-1]

		_Request = Request(_DATA_DEFINITION_ID=DEFINITION_ID, _DATA_REQUEST_ID=REQUEST_ID, _time=time, _name=name, _psc=self)
		self.Requests.append(_Request)
		return _Request
