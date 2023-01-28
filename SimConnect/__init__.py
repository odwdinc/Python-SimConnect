from .SimConnect import SimConnect, millis, DWORD
from .SimConnection import SimConnection
from .RequestList import AircraftRequests, Request
from .EventList import AircraftEvents, Event
from .FacilitiesList import FacilitiesRequests, Facility


def int_or_str(value):
    try:
        return int(value)
    except TypeError:
        return value


__version__ = "0.5"
VERSION = tuple(map(int_or_str, __version__.split(".")))

__all__ = [
	"SimConnect",
	"SimConnection",
	"millis",
	"DWORD",
	"AircraftRequests",
	"Request",
	"AircraftEvents",
	"Event",
	"FacilitiesRequests",
	"Facility",
]
