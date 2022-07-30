## System Imports


## Embedder Imports


## Application Imports


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.Event.base import BaseEvent
from Core.Interface.View.Event.interfaces import EventArgumentsInterface


class ControlResizeEventArguments(EventArgumentsInterface):
	
	def __init__(self, width: int, height: int):
		self.width = width
		self.height = height
	
	def __del__(self):
		pass


@factory.register
class ControlResizeEvent(BaseEvent):
	
	Type = 'control_resize'
	
	def __init__(self):
		super().__init__()
	
	def Trigger(self, args: ControlResizeEventArguments = None):
		for subscriber in self.subscribers:
			for control in self.controls:
				subscriber(control, control.GetWidth() + args.width, control.GetHeight() + args.height)
				print(control.GetWidth(), control.GetHeight())
