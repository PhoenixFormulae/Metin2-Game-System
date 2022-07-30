## System Imports

## Embedder Imports
from junctions import quest
from junctions import network

## Application Imports
from FSM.enums import PhaseState
from game_system import Metin2GameSystem
from FSM.decorators import register_state
from System.Manager.base import BaseManager

## Library Imports
from Core.Manager.decorators import register_manager


@register_state(PhaseState.Game)
@register_manager(Metin2GameSystem)
class QuestManager(BaseManager):
	
	__ignore_input: bool = False
	
	@classmethod
	def Ready(cls):
		...
	
	## State Machine Calls
	def OnEnterGamePhase(self):
		...
	
	@classmethod
	def OnExitGamePhase(cls):
		quest.Clear()
	
	## Embedder Calls
	def BINARY_OnQuestConfirm(self, message: str, timeout: int, pid: int):
		self.__presenter.OnConfirm(message, timeout, pid)
	
	## Command Calls
	def COMMAND_inputblock(self):
		self.__ignore_input = True
	
	def COMMAND_inputblockend(self):
		self.__ignore_input = False
	
	## Manager Methods
	def OpenQuestWindow(self, skin: int, index: int):
		if self.__ignore_input:
			return
		
		self.__presenter.Open(skin, index)
	
	def HideAllQuestWindow(self):
		self.__presenter.HideAll()
	
	@staticmethod
	def AcceptQuest(pid: int):
		network.SendQuestConfirmPacket(True, pid)
	
	@staticmethod
	def DenyQuest(pid: int):
		network.SendQuestConfirmPacket(False, pid)
	
