## System Imports


## Embedder Imports


## Application Imports


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.Event.base import BaseEvent
from Core.Interface.View.decorators import generic_property
from Core.Interface.View.Event.interfaces import EventArgumentsInterface


class ControlMovementEventArguments(EventArgumentsInterface):
	
	def __init__(self):
		pass
	
	def __del__(self):
		pass


@factory.register
class ControlMovementEvent(BaseEvent):
	
	Type = 'control_movement'
	
	@generic_property('x')
	def x(self, x: int):
		self.SetProperty('x', x)
	
	@generic_property('y')
	def y(self, value: int):
		self.SetProperty("y", value)
	
	def __init__(self):
		super().__init__()
	
	def Trigger(self, args: EventArgumentsInterface = None):
		pass
