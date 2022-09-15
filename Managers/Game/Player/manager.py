# Standard Imports

# Embedder Imports
from junctions import skill, character_manager

# Library Imports
from System.Manager.base import BaseManager
from Settings.Game.Player.enums import Race

# External Imports


class PlayerManager(BaseManager):
	
	__registered: bool = False
	
	@classmethod
	def Ready(cls):
		if cls.__registered:
			raise AttributeError('Cannot register player races more than once')
		
		cls.__RegisterRaces()
		cls.__registered = True

	
	@classmethod
	def __RegisterRaces(cls):
		for race in Race:
			character_manager.CreateRace(race.value)
	
	@classmethod
	def __RegisterSkillData(cls):
		skill.LoadSkillData()
	
