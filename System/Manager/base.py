# Standard Imports
from abc import ABC

# Embedder Imports

# Library Imports
from FSM.enums import PhaseState

# External Imports
from Core.Manager.interfaces import ManagerInterface


class BaseManager(ManagerInterface, ABC):
	
	@classmethod
	def Ready(cls):
		# GameFiniteStateMachine.Game.Dispatcher += self
		pass
	
	@classmethod
	def PostReady(cls):
		pass
	
	# TODO: Bind phase state changes from the StateMachine to this method
	@classmethod
	def OnPhaseChange(cls, old: PhaseState, new: PhaseState):
		enter_phase_change_call = f'OnEnter{new.name}Phase'
		
		exit_phase_change_call = None
		if old:
			exit_phase_change_call = f'OnExit{old.name}Phase'
		
		if hasattr(cls, enter_phase_change_call):
			getattr(cls, enter_phase_change_call)()
		
		if old:
			if hasattr(cls, exit_phase_change_call):
				getattr(cls, exit_phase_change_call)()
