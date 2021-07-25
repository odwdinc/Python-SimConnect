from SimConnect import *
from .Enum import *
from .Constants import *


class ScenarioRequest(object):
	def get(self):
		return self.value

	def get_data(self, *args):
		"""updates output data"""
		return self.sm.get_simple_data(self, *args)

	def setup_request(self):
		self.DATA_REQUEST_ID = self.sm.new_request_id()
		self.outData = None
		self.sm.Requests[self.DATA_REQUEST_ID.value] = self

	@property
	def value(self):
		if (self.LastData + self.time) < millis():
			self.setup_request()
			if self.fetch_data(self):
				self.LastData = millis()
			else:
				return None
		return self.outData

	def __init__(self, _sm, _requestName, _time=10, _dec=None, _settable=False, _attemps=10):
		self.DATA_REQUEST_ID = None
		self.description = _dec
		self.requestName = _requestName
		self.outData = None
		self.attemps = _attemps
		self.sm = _sm
		self.time = _time
		self.settable = _settable
		self.LastData = 0
		self.LastID = 0


class GoalRequests(object):
	def getGoalCount(self):
		return ScenarioRequest(self.sm, 'RequestGoalCount').value

	def getGoalByIndex(self, index):
		return ScenarioRequest(self.sm, 'RequestGoalDataByIndex').value

	def get_goals(self):
		count = self.getGoalCount()
		return [self.getGoalByIndex(index) for index in range(0, count)]

	def __init__(self, _sm, _time=10, _attemps=10):
		self.sm = _sm
		self.list = []
