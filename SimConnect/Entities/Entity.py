from SimConnect import SimConnect


class Entity:
    def __init__(self, sm=None):
        self.sm = sm or SimConnect()

    def __get_attr_request(self, attribute, time=2000, request=None, default=None):
        def inner_func():
            if request is None:
                request = self.sm.new_request(time=time)
            request.add(attribute)

            data = self.sm.get_data(request)
            return getattr(data, attribute[0], default=default)

        return inner_func