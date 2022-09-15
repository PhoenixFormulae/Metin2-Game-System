# Standard Imports

# Embedder Imports

# Library Imports
from FSM.enums import PhaseState
from FSM.decorators import register_state
from System.Manager.base import BaseManager

# External Imports


@register_state(PhaseState.Game)
class FishingManager(BaseManager):
	
	__alerts: dict[str, bool] = {}
	__catches: dict[str, bool] = {}
	
	_protocol = None
	
	@classmethod
	def Ready(cls):
		pass
	
	## Embedder Calls
	@classmethod
	def OnFishingSuccess(cls, is_fish: bool, name: str):
		cls.__catches[name] = is_fish
		cls._protocol.OnSuccess(is_fish, name)

	@classmethod
	def OnFishingNotifyUnknown(cls):
		cls._protocol.OnUnknown()

	@classmethod
	def OnFishingWrongPlace(cls):
		cls._protocol.OnDisplaced()
	
	@classmethod
	def OnFishingNotify(cls, is_fish: bool, fish_name: str):
		cls.__alerts[fish_name] = is_fish
		cls._protocol.OnMotion(is_fish, fish_name)
	
	@classmethod
	def OnFishingFailure(cls):
		cls._protocol.OnFailure()

