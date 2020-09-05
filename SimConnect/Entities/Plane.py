from .Entity import Entity

import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


class Plane(Entity):
	request_attr_altitude = ("Altitude", (b"Plane Altitude", b"feet"))
	request_attr_latitude = ("Latitude", (b"Plane Latitude", b"degrees"))
	request_attr_longitude = ("Longitude", (b"Plane Longitude", b"degrees"))
	request_attr_kohlsman = ("Kohlsman", (b"Kohlsman setting hg", b"inHg"))

	def __init__(self, *args, **kwargs):
		super(Plane, self).__init__(*args, **kwargs)

		attributes = [
			self.request_attr_altitude,
			self.request_attr_latitude,
			self.request_attr_longitude,
			self.request_attr_kohlsman,
		]

		for attr in attributes:
			setattr(
				self,
				attr[0].lower(),
				property(self._get_attr_request(attr)).fget(),
			)
