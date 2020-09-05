import SimConnect
from unittest import TestCase
from unittest.mock import Mock, patch

import logging

LOGGER = logging.getLogger(__name__)


class TestPlane(TestCase):
    def test_init(self):
        # SimConnect.Plane()
        self.assertTrue(True)

    @patch.object(SimConnect.Plane, "sm", side_effect="")
    def test_altitude(self, mock_simconnect):
        val = 500
        self.assertEqual(val, SimConnect.Plane().altitude)
