# Standard Imports

# Embedder Imports
from junctions import sound

# Library Imports
from FSM.decorators import register_state
from System.Manager.base import BaseManager

# External Imports


@register_state()
class SoundManager(BaseManager):
	
	## State Machine Calls
	def OnEnterGamePhase(self):
		pass
	
	@classmethod
	def OnExitGamePhase(cls):
		sound.StopAllSound()
	
