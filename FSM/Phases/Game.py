## System Imports

## Embedder Imports
from junctions import event
from junctions import group
from junctions import player
from junctions import network
from junctions import background
from junctions import application
from junctions import window_manager
from junctions import system_settings

## Application Imports
from FSM.enums import PhaseState
from FSM.Phases import BasePhase


## Library Imports


class PhaseGameState(BasePhase):

	@property
	def Handle(self) -> int:
		return self.__dispatcher

	def __init__(self):
		super().__init__(name=PhaseState.Game.name, value=PhaseState.Game)

	# State Machine Calls
	def OnEnterPhase(self):
		network.SetPhaseWindow(network.PHASE_WINDOW_GAME, self.__dispatcher)
		player.SetGameWindow(self.__dispatcher)
		system_settings.SetInterfaceHandler(self)
		event.SetInterfaceWindow(self)
		application.SetFrameSkip(1)

	@classmethod
	def OnPostEnterPhase(cls):
		application.ShowCursor()
		network.SendEnterGamePacket()

	def OnExitPhase(self):
		player.SetGameWindow(0)
		network.ClearPhaseWindow(network.PHASE_WINDOW_GAME, self)
		system_settings.DestroyInterfaceHandler()
		event.SetInterfaceWindow(None)

	def Exit(self, state: PhaseState):
		group.InitScreenEffect()

		background.Destroy()

		window_manager.Unlock()

	# Embedder Calls
	@classmethod
	def OnUpdate(cls):
		application.UpdateGame()

	def OnRender(self):
		pass

	# Command Calls
	@staticmethod
	def COMMAND_test_server():
		application.EnableTestServerFlag()

	def COMMAND_mall(self, url):
		print(f"Got mall command {url}")

	def COMMAND_CloseRestartWindo(self):
		self.interface.CloseRestartDialog()
