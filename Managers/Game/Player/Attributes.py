## System Imports

## Embedder Imports
from junctions import player
from junctions import network
from junctions import character

## Application Imports
from FSM.decorators import register_state
from System.Manager.base import BaseManager
from Settings.Game.Player.Attributes.data import JobsSkills, JobsPassiveSkills,\
	GuildActiveSkills, GuildPassiveSkills

## Library Imports
from game_system import Metin2GameSystem
from Core.Manager.decorators import register_manager


@register_state()
@register_manager(Metin2GameSystem)
class PlayerAttributesManager(BaseManager):
	
	__registered: bool = False
	
	@classmethod
	def Ready(cls):
		if cls.__registered:
			raise AttributeError('Cannot register player attributes more than once')
		
		cls.__registered = True
		
		# cls.__Register()
	
	@classmethod
	def __Register(cls):
		race = network.GetMainActorRace()
		group = network.GetMainActorSkillGroup()
		job = character.RaceToJob(race)
		empire = network.GetMainActorEmpire()
	
		# cls.__RegisterSkills(job, group)
		# cls.__RegisterLanguageSkills(empire)
		# cls.__RegisterGuildSkills()
	
	@classmethod
	def __RegisterSkills(cls, job: int, group: int):
		
		if job not in JobsSkills:
			raise AttributeError(f'Cannot register skills for job index {job}, no index found in job skills')
		
		if group not in JobsSkills[job]:
			raise AttributeError(f'Cannot register skills for job index {job} and group index {group}, '
								 f'no index found in group skills')
		
		active_skills = JobsSkills[job][group]
		
		# TODO: Perhaps for some reason its not intended to set still for index 6 to 8
		#       But some skills are also 0 so maybe it doesn't matter, investigate this case
		for index in JobsSkills[job][group]:
			player.SetSkill(index + 1, active_skills[index])
		
		for index in JobsPassiveSkills:
			player.SetSkill(index + 1, JobsPassiveSkills[index])
	
	@classmethod
	def __RegisterLanguageSkills(cls, empire: int):
		
		if empire is 0:
			return
		
		for index in range(1, 3):
			if empire != index + 1:
				player.SetSkill(107, player.SKILL_INDEX_LANGUAGE1 + index)
	
	@classmethod
	def __RegisterGuildSkills(cls):
		
		for index in GuildActiveSkills:
			player.SetSkill(200 + index, GuildActiveSkills[index])
		
		for index in GuildPassiveSkills:
			player.SetSkill(210 + index, GuildPassiveSkills[index])
	
	@classmethod
	def __RegisterColors(cls):
		pass
