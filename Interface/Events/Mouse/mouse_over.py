# Standard Imports
from typing import Callable, Optional


# Embedder Imports


# Library Imports


# External Imports
from Core.Plugins import factory
from Core.Interface.View.Event.base import BaseEvent
from Core.Interface.View.Event.interfaces import EventArgumentsInterface


class MouseOverEventArguments(EventArgumentsInterface):
	
	def __init__(self, out: bool):
		self.__out: bool = out
	
	def __del__(self):
		pass


@factory.register
class MouseOverEvent(BaseEvent):
	
	Type = 'mouse'
	
	def __init__(self, args: MouseOverEventArguments = None):
		super().__init__()
		
		self.__arguments: Optional[MouseOverEventArguments] = args
	
	def Bind(self, method: Callable):
		pass
	
	def Trigger(self, args: MouseOverEventArguments = None):
		pass

