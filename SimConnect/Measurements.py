from enum import Enum


class Measurement(Enum):
    altitude = ("Altitude", (b"Plane Altitude", b"feet"))
    latitude = ("Latitude", (b"Plane Latitude", b"degrees"))
    longitude = ("Longitude", (b"Plane Longitude", b"degrees"))
    kohlsman = ("Kohlsman", (b"Kohlsman setting hg", b"inHg"))
    
    altitude_above_ground = ("Kohlsman", (b"PLANE ALT ABOVE GROUND", b"feet"))
    pitch = ("Kohlsman", (b"PLANE PITCH DEGREES", b"Radians"))
    bank = ("Kohlsman", (b"PLANE BANK DEGREES", b"Radians"))
    heading = ("Kohlsman", (b"PLANE HEADING DEGREES TRUE", b"Radians"))
    heading_magnetic = ("Kohlsman", (b"PLANE HEADING DEGREES MAGNETIC", b"Radians"))