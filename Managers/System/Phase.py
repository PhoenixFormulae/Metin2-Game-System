# Standard Imports

# Library Imports
from FSM import model
from FSM.enums import PhaseState
from game_system import Metin2GameSystem
from FSM.decorators import register_state
from System.Manager.base import BaseManager

# External Imports
from Core import CoreSystem
from Core.Manager.decorators import register_manager


@register_state()
@register_manager(Metin2GameSystem)
class PhaseManager(BaseManager):
	
	# FiniteStateMachine = GameFiniteStateMachine()
	
	@classmethod
	def Ready(cls):
		model.FiniteStateMachine.to_logo()
	
	@classmethod
	def PostReady(cls):
		model.FiniteStateMachine.to_logo()
	
	@classmethod
	def OnPhaseChange(cls, old: PhaseState, new: PhaseState):
		for presenter in CoreSystem.GameSystem.PresenterTypes:
			cls.NotifyPresenter(presenter, old, new)
	
	@classmethod
	def NotifyPresenter(cls, presenter, old: PhaseState, new: PhaseState):
		enter_phase_change_call = f'OnEnter{new.name}Phase'
		
		exit_phase_change_call = None
		if old:
			exit_phase_change_call = f'OnExit{old.name}Phase'
		
		if hasattr(presenter, enter_phase_change_call):
			getattr(presenter, enter_phase_change_call)()
		
		if old != new:
			if hasattr(presenter, exit_phase_change_call):
				getattr(presenter, exit_phase_change_call)()

