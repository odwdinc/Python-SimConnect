# coming soon
from .SimConnect import SimConnect, Request

class AsyncSimConnect(SimConnect):
    async def GetData(self, _Request):
        pass

    # TODO: add all other functions as async