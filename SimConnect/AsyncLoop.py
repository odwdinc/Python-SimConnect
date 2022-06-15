import asyncio
from threading import Thread, Condition
import logging

logger = logging.getLogger(__name__)

class AsyncLoop(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.async_loop = None
        self._condition_var = Condition()

    def start(self):
        with self._condition_var:
            Thread.start(self)
            self._condition_var.wait()

    def run(self):
        self.async_loop = asyncio.new_event_loop()
        logger.debug("AsyncLoop: %s", self.async_loop)
        self.async_loop.call_soon_threadsafe(self._notify_start)
        self.async_loop.run_forever()

    def _notify_start(self):
        with self._condition_var:
            self._condition_var.notify_all()

    def stop(self):
        self.async_loop.call_soon_threadsafe(self.async_loop.stop)
        self.join()
        self.async_loop.close()

    def execute(self, routine):
        future_runner = asyncio.run_coroutine_threadsafe(routine, loop=self.async_loop)
        return future_runner.result()