## System Imports

## Embedder Imports
from junctions import item, effect, background, character_manager


## Application Imports
from FSM.enums import PhaseState
from FSM.decorators import register_state
from Settings.Game.Environment import data

## Library Imports
from System.Manager.base import BaseManager


@register_state(PhaseState.Game)
class EnvironmentManager(BaseManager):
	
	def __init__(self):
		super().__init__()
		
		self.__RegisterEnvironment()
	
	def Ready(self):
		background.RegisterEnvironmentData(1, data.NightEnvironmentPath)
	
	def __RegisterEnvironment(self):
		self.__RegisterGameEffects()
		self.__RegisterInterfaceSounds()
		self.__RegisterSounds()
		self.__RegisterDungeonMapNames()
	
	@staticmethod
	def __RegisterGameEffects():
		character_manager.SetDustGap(data.DustGaps['dust'])
		character_manager.SetHorseDustGap(data.DustGaps['horse'])
		
		for index, effect_data in data.FlyEffects.keys():
			effect.RegisterIndexedFlyData(index, effect_data[0], effect_data[1])
	
	@staticmethod
	def __RegisterFlyEffects():
		pass
	
	@staticmethod
	def __RegisterInterfaceSounds():
		for index, path in data.InterfaceSounds.keys():
			item.SetUseSoundFileName(index, path)
	
	@staticmethod
	def __RegisterSounds():
		pass
	
	@staticmethod
	def __RegisterDungeonMapNames():
		for dungeon_name in data.DungeonMapName:
			background.RegisterDungeonMapName(dungeon_name)

