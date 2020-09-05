from SimConnect import SimConnect, DWORD
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

    def _send_data(self, event, value):
        self.sm.send_data(self.sm.map_to_sim_event(event.value.encode("utf-8")), value)

    def get(self, attribute, request=None, default=None):
        return self._get_attr_request(attribute, request=request, default=default)()

    def send(self, event, value=DWORD(0)):
        self._send_data(event, value)