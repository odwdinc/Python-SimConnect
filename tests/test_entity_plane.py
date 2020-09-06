import SimConnect
from unittest import TestCase
from unittest.mock import Mock, patch, create_autospec

import logging

LOGGER = logging.getLogger(__name__)


class sData(dict):
    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

    def __setattr__(self, key, value):
        super(sData, self).__setitem__(key, value)
        setattr(
            self,
            key,
            value,
        )

    def __init__(self, data=None):
        if data is not None:
            try:
                for key, value in data.items():
                    self[key] = value
            except:
                pass


class TestPlane(TestCase):
    def test_init(self):
        # SimConnect.Plane()
        self.assertTrue(True)

    def test_values(self):

        sm = create_autospec(SimConnect.SimConnect)

        def side_effect(*args, **kwargs):
            def val():
                v = 100
                x = 100
                while True:
                    yield x
                    x += v

            data = sData()
            val = val()
            data["Altitude"] = next(val)
            data["Latitude"] = next(val)
            data["Longitude"] = next(val)
            data["Kohlsman"] = next(val)
            return data

        sm.get_data.side_effect = side_effect

        pl = SimConnect.Plane(sm=sm)
        self.assertEqual(100, pl.altitude)
        self.assertEqual(200, pl.latitude)
        self.assertEqual(300, pl.longitude)
        self.assertEqual(400, pl.kohlsman)
