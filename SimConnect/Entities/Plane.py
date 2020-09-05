from .Entity import Entity
from ..Measurements import Measurement
from ..Events import Event

import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


class Plane(Entity):
    def __init__(self, *args, **kwargs):
        """
        Initialie a plane entity.

        Parameters: (inherit from Entity)
            default (bool): If False, then no standard attributes will be loaded. Default True.
        """
        add_default = kwargs.get("default", True)
        if "default" in kwargs:
            del kwargs["default"]

        super(Plane, self).__init__(*args, **kwargs)

        if add_default:
            self.standard_attributes()
            self.add_events()

    def add_events(self):
        for ev in Event:
            setattr(
                self,
                ev.name.lower(),
                property(lambda: ev.value).fget(),
            )

    def standard_attributes(self):
        attributes = [
            Measurement.altitude,
            Measurement.latitude,
            Measurement.longitude,
            Measurement.kohlsman,
        ]

        for attr in attributes:
            self.add_attribute(attr)

    def add_attribute(self, attr):
        def func(fn):
            def inner_func():
                return fn(attr)

            return inner_func

        attr = attr.value
        setattr(
            self,
            attr[0].lower(),
            property(func(self.get)).fget(),
        )
