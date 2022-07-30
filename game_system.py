## System Imports
import logging
from typing import Type


## Application Imports


## Library Imports
from Core.System import decorators
from Core.System.base import BaseGameSystem
from Core.System.data import GameSystemConfiguration
from Core.Manager.interfaces import ManagerInterface
from Core.Interface.Frame.interfaces import FrameInterface
from Core.Interface.Presenter.interfaces import PresenterInterface


@decorators.register_game_system()
class Metin2GameSystem(BaseGameSystem):
	
	ManagerTypes: list[Type[ManagerInterface]] = []
	PresenterTypes: list[Type[PresenterInterface]] = []
	
	@property
	def Configuration(self) -> GameSystemConfiguration:
		return self.__configuration
	
	@property
	def Frames(self) -> list[Type[FrameInterface]]:
		return self.__frames
	
	def __init__(self, configuration: GameSystemConfiguration):
		logging.debug('Initializing Metin2 system')
		
		self.__state_machine = None
		self.__configuration = configuration
		
		from Interface.Frames.Metin2.frame import Metin2InterfaceFrame
		self.__frames: list[Type[FrameInterface]] = [Metin2InterfaceFrame]
		
		self.Initialize()
	
	def __del__(self):
		logging.debug('Terminating Metin2 system')
	
	@classmethod
	def RegisterManager(cls, manager_type: Type[ManagerInterface]):
		if manager_type not in cls.ManagerTypes:
			cls.ManagerTypes.append(manager_type)
	
	@classmethod
	def RegisterPresenter(cls, presenter_type: Type[PresenterInterface]):
		if presenter_type not in cls.PresenterTypes:
			cls.PresenterTypes.append(presenter_type)
	
	def Initialize(self):
		for frame in self.__frames:
			frame.Initialize()
	
	def Ready(self):
		super().Ready()
		super().PostReady()
	
