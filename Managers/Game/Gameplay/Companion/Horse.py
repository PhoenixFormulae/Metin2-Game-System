# Standard Imports

# Embedder Imports
from junctions import player
from junctions import network
from junctions import application

# Library Imports
from FSM.enums import PhaseState
from FSM.decorators import register_state
from Managers.Input.Keyboard.data import KeyState
from Managers.Input.Keyboard.decorators import Key

# External Imports
from System.Manager.base import BaseManager


@register_state(PhaseState.Game)
class HorseManager(BaseManager):
	
	__level: int = 0
	__health: int = 0
	__energy: int = 0
	
	_protocol = None
	
	@classmethod
	def Ready(cls):
		pass
	
	## State Machine Calls
	def OnEnterGamePhase(self):
		pass
	
	def OnExitGamePhase(self):
		pass
	
	## Keyboard Calls
	@Key(KeyState.Both, ((application.DIK_LCONTROL, application.DIK_RCONTROL), application.DIK_J))
	def MountHorse(self):
		if player.IsMountingHorse():
			network.SendChatPacket('/unmount')
		else:
			network.SendChatPacket('/user_horse_ride')
	
	@Key(KeyState.Press, ((application.DIK_LCONTROL, application.DIK_RCONTROL), application.DIK_G))
	def RideMount(self):
		network.SendChatPacket('/ride')
	
	@Key(KeyState.Both, ((application.DIK_LCONTROL, application.DIK_RCONTROL), application.DIK_B))
	def RecallMount(self):
		network.SendChatPacket('/user_horse_back')
	
	## Command Calls
	@classmethod
	def COMMAND_horse_state(cls, level: int, health: int, energy: int):
		cls.__level = level
		cls.__health = health
		cls.__energy = energy
		
		cls._protocol.UpdateHorseState()
	
	@classmethod
	def COMMAND_hide_horse_state(cls):
		cls._protocol.HideHorseState()
		
	
