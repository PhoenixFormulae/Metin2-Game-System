# Standard Imports
from typing import Callable
from enum import IntEnum, unique


# Library Imports


# External Imports
from Core.Plugins import factory
from Core.Interface.View.Event.base import BaseEvent
from Core.Interface.View.Event.interfaces import EventArgumentsInterface


@unique
class FadeState(IntEnum):
	Waiting = 1
	FadeIn = 2
	FadeOut = 3


class ImageFadingEventArguments(EventArgumentsInterface):
	
	def __init__(self):
		pass
	
	def __del__(self):
		pass


@factory.register
class ImageFadingEvent(BaseEvent):
	
	type: str = "image_fading_ex"
	
	def __init__(self):
		super().__init__()
		
		self.__current_alpha: float = 0.0
		self.__fade_state: FadeState = FadeState.Waiting
		self.__fade_speed: float = 0.5
	
	def Trigger(self, arguments: ImageFadingEventArguments = None):
		"""
		Triggers this event to process the fading cycle.
		This should only be called by one OnUpdate method,
		otherwise the processing speed will different from
		expected
		
		:param arguments:
		:return:
		"""
		
		self.__ProcessFading()
	
	def Bind(self, method: Callable):
		pass
	
	def __FadeOut(self, speed: float):
		"""
		Starts to fade the image from completely visible
		gradually along the specified speed until its
		completely invisible
		
		:param speed: Amount to add when update cycle occurs
		"""
		
		self.__current_alpha = 1.0
		self.__Fade(FadeState.FadingOut, speed)
	
	def __FadeIn(self, speed: float):
		"""
		Starts to fade the image from completely invisible
		gradually along the specified speed until its
		completely visible
		
		:param speed: Amount to add when update cycle occurs
		"""
		
		self.__current_alpha = 0.0
		self.__Fade(FadeState.FadingIn, speed)
	
	def __Fade(self, fade_state: FadeState, speed: float):
		self.__fade_speed = self.__fade_speed if speed != 0 else speed
		
		self.__fade_state = fade_state
	
	def __ProcessFading(self):
		"""
		Processes the fading animation state cycles
		"""
		
		if self.__fade_state == FadeState.Waiting:
			return
		
		elif self.__fade_state == FadeState.In:
			self.__current_alpha += self.__fade_speed
			
			if self.__current_alpha >= 1.0:
				self.__fade_state = FadeState.Wait
				self.current_alpha = 1.0
		
		elif self.__fade_state == FadeState.FadeOut:
			self.__current_alpha -= self.__fade_speed
			
			if self.__current_alpha <= 0.0:
				self.__fade_state = FadeState.Wait
				self.__current_alpha = 0.0
		
		for subscriber in self.subscribers:
			subscriber(self.current_alpha)

