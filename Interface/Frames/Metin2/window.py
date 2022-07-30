## System Imports
import logging
from typing import Type
from enum import Enum, unique


## Embedder imports
from junctions import application
from junctions import window_manager


## Application Imports


## Library Imports
from Core.Interface.data import BaseWindowConfiguration
from Core.Interface.Frame.interfaces import FrameWindowInterface, FrameInterface

from Interface.Frames.Metin2.frame import Metin2InterfaceFrame



@unique
class CreationError(Enum):
	CREATE_DEVICE = 0


class Metin2InterfaceFrameWindow(FrameWindowInterface):
	
	FrameType: Type[FrameInterface] = Metin2InterfaceFrame
	
	def __init__(self, configuration: BaseWindowConfiguration):
		self.__configuration = configuration
		
		self.Create()
	
	def __del__(self):
		pass
	
	def Create(self):
		try:
			window_manager.SetScreenSize(self.__configuration.width, self.__configuration.height)
			
			application.Create(self.__configuration.title, self.__configuration.width, self.__configuration.height,
							   self.__configuration.windowed)
		
		except RuntimeError as creation_error:
			if creation_error == CreationError.CREATE_DEVICE:
				logging.error("Could not create device")
			else:
				logging.error(f"Could not create window: {creation_error}")
				return
	
	def Loop(self):
		application.Loop()
