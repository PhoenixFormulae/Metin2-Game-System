## System Imports
from enum import Enum


## Application Imports


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.Event.base import BaseEvent
from Core.Interface.View.decorators import generic_property
from Core.Interface.View.Event.interfaces import EventArgumentsInterface


class ImageAnimationEventArguments(EventArgumentsInterface):
	
	@property
	def time(self):
		return self.__time
	
	def __init__(self, time: float):
		self.__time: float = time
	
	def __del__(self):
		pass


class AnimationType(Enum):
	SemiLap = 0
	Lap = 1
	NonStop = 2


class AnimationState(Enum):
	FadingIn = 0
	Waiting = 1
	FadingOut = 2


@factory.register
class ImageFadingEvent(BaseEvent):
	
	type: str = 'image_fading'
	
	@generic_property('animation_type')
	def animation_type(self, value: AnimationType):
		self.SetProperty("animation_type", value)
	
	@generic_property('amount')
	def amount(self, value: float):
		self.SetProperty("amount", value)
	
	@generic_property('maximum')
	def maximum(self, value: float):
		self.SetProperty("maximum", value)
	
	def __init__(self):
		super().__init__()
		
		self.__animating: bool = True
		
		self.__current_fade: float = 0.0
		self.__fade_state: AnimationState.Waiting
	
	def __CallSubscribers(self, transparency: float):
		for subscriber in self.subscribers:
			subscriber.SetTransparency(transparency)
	
	def Trigger(self, args: ImageAnimationEventArguments | None = None):
		self.__ProcessAnimation()
	
	def __ProcessAnimation(self):
		if not self.__animating:
			return
		
		if self.properties["animation_type"] == "fadein":
			self.__ProcessFadeIn()
		elif self.properties["animation_type"] == "fadeout":
			self.__ProcessFadeOut()
	
	def __ProcessFadeIn(self):
		if self.__current_fade >= self.properties["maximum"]:
			self.__animating = False
			return
		
		self.__current_fade += self.properties["amount"]
		
		transparency = self.__current_fade / 100
		print(f"transparency: {transparency}")
		
		self.__CallSubscribers(transparency)
	
	def __ProcessFadeOut(self):
		pass
	