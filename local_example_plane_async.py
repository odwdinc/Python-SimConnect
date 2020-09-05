from SimConnect import Plane, Measurement

from unittest import TestCase

import logging
import asyncio

LOGGER = logging.getLogger(__name__)
loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
for logger in loggers:
    logger.setLevel(logging.INFO)


LOGGER.info("START")

pl = Plane()

while not pl.sm.quit:
    loop = asyncio.get_event_loop()
    tasks = [pl.async_get(Measurement.altitude), pl.async_get(Measurement.longitude)]
    a, b = loop.run_until_complete(asyncio.gather(*tasks))
    LOGGER.info("alt={a}, long()={b}".format(**vars()))

pl.sm.exit()