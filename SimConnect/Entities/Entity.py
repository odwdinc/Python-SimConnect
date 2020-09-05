from SimConnect import SimConnect
import logging

LOGGER = logging.getLogger(__name__)


class Entity:
	def __init__(self, sm=None):
		self.sm = sm or SimConnect()

	def _get_attr_request(self, attribute, time=2000, request=None, default=None):
		def inner_func():
			nonlocal request, time, default

			LOGGER.debug(f"get attribute: {attribute}")

			if request is None:
				LOGGER.debug("create new request")
				request = self.sm.new_request(time=time)
			request.add(attribute)

			LOGGER.debug(f"get request: {request}")
			data = self.sm.get_data(request)
			LOGGER.debug(f"got data: {data}")
			return getattr(data, attribute[0], default)

		return inner_func
