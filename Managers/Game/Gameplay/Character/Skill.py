# Standard Imports


# Embedder Imports
from junctions import skill


# Library Imports


# External Imports
from System.Manager.base import BaseManager


class SkillManager(BaseManager):
	
	## State Machine Calls
	def OnEnterGamePhase(self):
		pass
	
	@classmethod
	def OnExitGamePhase(cls):
		skill.ClearSkillData()
	
