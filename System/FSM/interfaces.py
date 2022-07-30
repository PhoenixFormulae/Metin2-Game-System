## System Imports
from abc import ABC, abstractmethod


## Application Imports
from FSM.enums import PhaseState


## Library Imports
from Core.dispatcher import CallDispatcher


class PhaseInterface(ABC):
	
	@property
	@abstractmethod
	def Dispatcher(self) -> CallDispatcher:
		pass
	
	@abstractmethod
	def Enter(self, state: PhaseState):
		pass
	
	@abstractmethod
	def Exit(self, state: PhaseState):
		pass
	
