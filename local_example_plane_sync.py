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
    alt1 = pl.get(tasks[0])
    long = pl.get(tasks[1])
    alt2 = pl.altitude

    LOGGER.info("alt1={alt1}, alt2={alt2}, long()={long}".format(**vars()))

pl.sm.exit()