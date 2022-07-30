## System Imports

## Embedder Imports
from junctions import network
from junctions import application

## Application imports
from FSM.enums import PhaseState
from game_system import Metin2GameSystem
from FSM.decorators import register_state
from System.Manager.base import BaseManager

## Library Imports
from Core.Manager.decorators import register_manager
from Core.Interface.Presenter.interfaces import PresenterInterface


@register_state(PhaseState.Login)
@register_manager(Metin2GameSystem)
class LoginManager(BaseManager):
	
	Presenters: list[PresenterInterface] = []
	
	@classmethod
	def Ready(cls):
		pass
	
	## State Machine Calls
	@classmethod
	def OnEnterLoginPhase(cls):
		network.SetPhaseWindow(network.PHASE_WINDOW_GAME, cls)
		application.ShowCursor()
	
	@classmethod
	def OnExitLoginPhase(cls):
		network.SetPhaseWindow(network.PHASE_WINDOW_GAME, None)
		application.HideCursor()
	
	## Dispatcher Calls
	@classmethod
	def OnUpdate(cls):
		# TODO: Protocols should be called here, and there is no need to check if the attribute exists
		for presenter in cls.Presenters:
			if hasattr(presenter, 'OnUpdate'):
				presenter.OnUpdate()
	
	@classmethod
	def OnRender(cls):
		# TODO: Same as above
		for presenter in cls.Presenters:
			if hasattr(presenter, 'OnRender'):
				presenter.OnRender()

