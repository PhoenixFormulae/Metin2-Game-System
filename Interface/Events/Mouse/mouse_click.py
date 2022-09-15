# Standard Imports
from enum import Enum


# Embedder Imports
from junctions import player


# Library Imports


# External Imports
from Core.Plugins import factory
from Core.Interface.View.Event.base import BaseEvent
from Core.Interface.View.Event.interfaces import EventArgumentsInterface


class MouseButton(Enum):
	Left = player.MBT_LEFT
	Right = player.MBT_RIGHT
	Wheel = 2


class MouseClickEventArguments(EventArgumentsInterface):
	
	def __init__(self, button: MouseButton, value: int):
		self.__button: MouseButton = button
		self.__value: int = value
	
	def __del__(self):
		pass


@factory.register
class MouseClickEvent(BaseEvent):
	
	Type = 'mouse_click'
	
	def Trigger(self, args: EventArgumentsInterface = None):
		self.subscribers[0](args)
