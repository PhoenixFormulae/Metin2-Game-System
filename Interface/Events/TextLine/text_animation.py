## System Imports
from typing import List
from enum import Enum, unique


## Application Imports


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.Event.base import BaseEvent
from Core.Interface.View.decorators import generic_property
from Core.Interface.View.Event.interfaces import EventArgumentsInterface


class TextAnimationEventArguments(EventArgumentsInterface):
	
	@property
	def time(self):
		return self.__time
	
	def __init__(self, time: float):
		self.__time: float = time
	
	def __del__(self):
		pass


@unique
class AnimationType(Enum):
	Forward = 0
	Backward = 1
	ForwardReverse = 2
	BackwardReverse = 3
	
	Gradient = 4
	GradientReverse = 5


@factory.register
class TextAnimationEvent(BaseEvent):
	
	Type: str = 'text_gradient'
	
	@generic_property('texts')
	def texts(self, value: List):
		self.SetProperty("texts", value)
	
	@generic_property('animation_type', required=False)
	def animation_type(self, value: AnimationType):
		self.SetProperty("animation_type", value)
	
	def __init__(self):
		super().__init__()
		
		self.__text: int = 0
		self.__index: int = 0
	
	def __CallSubscribers(self, text: str):
		for subscriber in self.subscribers:
			subscriber.SetText(text)
	
	def Trigger(self, args: TextAnimationEventArguments = None):
		self.__ProcessTextAnimation()
	
	def __ProcessTextAnimation(self):
		animation_type = self.properties["animation_type"]
		
		if animation_type == "forward":
			self.__ProcessForwardAnimation()
		elif animation_type == "gradient_reverse":
			# TODO: Create __ProcessGradientReverse function
			self.__ProcessForwardAnimation()
	
	def __ProcessForwardAnimation(self):
		self.__index += 1
		
		text = self.properties["texts"][self.__text]
		
		new_text = text[0:self.__index]
		
		if self.__index + 1 > len(text):
			self.__text += 1
			self.__index = 0
		
		if self.__text + 1 > len(self.properties["texts"]):
			self.__text = 0
		
		self.__CallSubscribers(new_text)

