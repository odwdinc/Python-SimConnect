from enum import Enum


class Measurement(Enum):
    altitude = ("Altitude", (b"Plane Altitude", b"feet"))
    latitude = ("Latitude", (b"Plane Latitude", b"degrees"))
    longitude = ("Longitude", (b"Plane Longitude", b"degrees"))
    kohlsman = ("Kohlsman", (b"Kohlsman setting hg", b"inHg"))
