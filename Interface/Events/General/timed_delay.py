## System Imports
from typing import List
from enum import Enum, unique


## Embedder Imports


## Application Imports


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.Event.base import BaseEvent
from Core.Interface.View.decorators import generic_property
from Core.Interface.View.Event.interfaces import EventArgumentsInterface


class TimedEventArguments(EventArgumentsInterface):
	
	@property
	def time(self):
		return self.__time
	
	def __init__(self, time: float):
		self.__time: float = time
	
	def __del__(self):
		pass


@unique
class StopAt(Enum):
	NoStop = 0
	SemiLap = 1
	Lap = 2
	FullLap = 3
	
	@classmethod
	def _missing_(cls, value):
		return StopAt.NoStop


@factory.register
class TimedEvent(BaseEvent):
	
	type: str = 'timed_delay'
	
	@generic_property('minimum')
	def minimum(self, value: float):
		self.SetProperty('minimum', value)
	
	@generic_property('maximum')
	def maximum(self, value: float):
		self.SetProperty('maximum', value)
	
	@generic_property('reverse_count')
	def reverse_count(self, value: bool):
		self.SetProperty('reverse_count', value)
	
	@generic_property('stop_at')
	def stop_at(self, value: bool):
		self.SetProperty("stop_at", value)
	
	@generic_property('trigger_delay')
	def trigger_delay(self, value: float):
		self.SetProperty("trigger_delay", value)
	
	@generic_property('trigger')
	def trigger(self, value: List[str]):
		self.SetProperty("trigger", value)
	
	def __init__(self):
		super().__init__()
		
		self.__local_delay_time: float = 0
		self.__last_time: float = 0
		
		self.__counting: bool = True
		self.__counting_clockwise: bool = True
		
		self.__cur_delay: float = 0
		
		self.__last_trigger: float = 0
	
	def Trigger(self, args: TimedEventArguments = None):
		self.__ProcessTime(args)
	
	def __ProcessTime(self, args: TimedEventArguments):
		time_difference = args.time - self.__last_time
		
		self.__last_time = args.time
		
		self.__ProcessDelay(time_difference)
	
	def __ProcessDelay(self, time_difference: float):
		if not self.__counting:
			return
		
		if self.__counting_clockwise:
			time_delay = self.__cur_delay + time_difference
		else:
			time_delay = self.__cur_delay - time_difference
		
		self.__cur_delay = time_delay
		
		if self.properties["reverse_count"]:
			if self.properties["maximum"] <= time_delay:
				self.__counting_clockwise = False
				self.__cur_delay = self.properties["maximum"]
				
				if self.properties["stop_at"]:
					if self.properties["stop_at"] == StopAt.SemiLap:
						self.__counting = False
			
			elif self.properties["minimum"] >= time_delay:
				self.__counting_clockwise = True
				self.__cur_delay = self.properties["minimum"]
				
				if self.properties["stop_at"]:
					if self.properties["stop_at"] == StopAt.SemiLap:
						self.__counting = False
		
		trigger_delay: float = self.properties["trigger_delay"]
		
		delay_difference = abs(self.__cur_delay - self.__last_trigger)
		
		if delay_difference >= trigger_delay:
			self.__last_trigger = self.__cur_delay - (delay_difference - trigger_delay)
			self.__TriggerChildren()
			
	def __TriggerChildren(self):
		for event in self.children:
			event.Trigger()
