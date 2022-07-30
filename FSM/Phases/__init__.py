## System Imports

## Application Imports
from FSM.enums import PhaseState
from System.FSM.interfaces import PhaseInterface

## Library Imports
from Core.dispatcher import CallDispatcher
from Core.Manager.interfaces import ManagerInterface

from statemachine import State


class BasePhase(State, PhaseInterface):
	
	@property
	def Managers(self):
		return self.__managers
	
	@property
	def Dispatcher(self):
		return self.__dispatcher
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.__dispatcher = CallDispatcher()
		self.__managers: list[ManagerInterface] = []
	
	def Enter(self, state: PhaseState):
		self.Dispatcher.dispatch('OnPhaseChange', state, self)
	
	def Exit(self, state: PhaseState):
		self.Dispatcher.dispatch('OnPhaseChange', self, state)
	
