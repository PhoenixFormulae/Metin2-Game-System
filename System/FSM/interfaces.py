# Standard Imports
from abc import ABC, abstractmethod


# Library Imports
from FSM.enums import PhaseState


# External Imports
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
	
