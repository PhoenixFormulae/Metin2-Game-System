## System Imports


## Embedder Imports
from junctions import chat


## Application Imports
from FSM.enums import PhaseState
from FSM.decorators import register_state
from System.Manager.base import BaseManager


## Library Imports


@register_state(PhaseState.Game)
class ChatManager(BaseManager):
	
	## Embedder Calls
	def OnEnterGamePhase(self):
		pass
	
	@classmethod
	def OnExitGamePhase(cls):
		chat.Close()
	
