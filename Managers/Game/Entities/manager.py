# Standard Imports

# Embedder Imports
from junctions import character_manager

# Library Imports
from System.Manager.base import BaseManager
from System.Parsers.RaceData import RaceData

# External Imports


class EntityManager(BaseManager):
	
	__registered: bool = False
	
	@classmethod
	def Ready(cls):
		if cls.__registered:
			raise AttributeError('Cannot register entities more than once')
		
		cls.__registered = True
		
		# cls.__RegisterRaceData(None)
	
	@classmethod
	def __RegisterRaceData(cls, race_data: RaceData | None):
		for race in race_data.races:
			character_manager.RegisterRaceName(race.vnum, race.model)
	

