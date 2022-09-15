# Standard Imports


# Embedder Imports
from junctions import application
from junctions import network


# Library Imports
from FSM import model
from FSM.enums import PhaseState
from game_system import Metin2GameSystem
from FSM.decorators import register_state
from System.Manager.base import BaseManager


# External Imports
from Core.Manager.decorators import register_manager
from Core.Interface.Presenter.interfaces import PresenterInterface


@register_state(PhaseState.Logo)
@register_manager(Metin2GameSystem)
class LogoManager(BaseManager):
	
	Presenters: list[PresenterInterface] = []
	
	@classmethod
	def Ready(cls):
		pass
	
	@classmethod
	def Finished(cls):
		from Managers.System.Phase import PhaseManager
		model.FiniteStateMachine.to_login()
	
	## State Machine Calls
	@classmethod
	def OnEnterLogoPhase(cls):
		network.SetPhaseWindow(network.PHASE_WINDOW_LOGO, cls)
		application.ShowCursor()
	
	@classmethod
	def OnExitLogoPhase(cls):
		network.SetPhaseWindow(network.PHASE_WINDOW_LOGO, None)
		application.HideCursor()
	
	## Dispatcher Calls
	@classmethod
	def OnUpdate(cls):
		# TODO: Protocols should be called here, and there is no need to check if the attribute exists
		for presenter in cls.Presenters:
			presenter.OnUpdate()
	
	@classmethod
	def OnRender(cls):
		# TODO: Same as above
		for presenter in cls.Presenters:
			presenter.OnRender()

