from SimConnect import Plane, Measurement

from unittest import TestCase

import logging

LOGGER = logging.getLogger(__name__)
loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
for logger in loggers:
    logger.setLevel(logging.INFO)


LOGGER.info("START")

pl = Plane()

LOGGER.debug("kawomm")

tasks = [Measurement.altitude, Measurement.longitude]
while not pl.sm.quit:
    for t in tasks:
        data = pl.get(t)
        LOGGER.info("{}: {}".format(t.value[0], data))

pl.sm.exit()