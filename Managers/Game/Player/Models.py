## System Imports

## Embedder Imports
from junctions import character_manager

## Application Imports
from System.Manager.base import BaseManager
from Settings.Game.Player.Motions.data import PlayerRaces

## Library Imports


class PlayerModelsManager(BaseManager):
	
	__registered: bool = False
	
	@classmethod
	def Ready(cls):
		if cls.__registered:
			raise AttributeError('Cannot register player models mora than once')
		
		cls.RegisterModelsData()
		cls.__registered = True

	@classmethod
	def RegisterModelsData(cls):
		for index, race in PlayerRaces['Races'].items():
			character_manager.SelectRace(index.value)
			
			for data in tuple_up(race['RaceData']):
				character_manager.LoadLocalRaceData(data)


def tuple_up(value):
	values = ()
	
	if not isinstance(value, tuple):
		values = (value, )
	else:
		values = value
	
	return values
