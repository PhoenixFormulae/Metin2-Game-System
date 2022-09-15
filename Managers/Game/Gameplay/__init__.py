# Standard Imports


# Embedder Imports
from junctions import character


# Library Imports
from System.Manager.base import BaseManager


# External Imports


class GameplayManager(BaseManager):
	
	@classmethod
	def Ready(cls):
		...
	
	## State Machine Calls
	def OnEnterGamePhase(self):
		pass
	
	@classmethod
	def OnExitGamePhase(cls):
		character.Destroy()
	
	def StartGame(self):
		self.RefreshInventory()
		self.RefreshEquipment()
		self.RefreshCharacter()
		self.RefreshSkill()
	
	def OnGameOver(self):
		self.CloseTargetBoard()
		self.OpenRestartDialog()
	
	def OpenRestartDialog(self):
		self.interface.OpenRestartDialog()

