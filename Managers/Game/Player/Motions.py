# Standard Imports

# Embedder Imports
from junctions import skill, character, character_manager

# Library Imports
from System.Manager.base import BaseManager
from Settings.Game.Player.Motions.data import PlayerJobsMotions, PlayerJobBones

# External Imports


class PlayerMotionsManager(BaseManager):
 
	__registered: bool = False
 
	@classmethod
	def Ready(cls):
		if cls.__registered:
			raise AttributeError('Cannot register motions more than once')
		
		cls.RegisterPlayerMotions()
	
	@classmethod
	def RegisterPlayerMotions(cls):
		for job_index, job in PlayerJobsMotions['Jobs'].items():
			for race in job['Race']:
				character_manager.SelectRace(race.value)
				
				base_path = job['Race'][race]['BasePath']
				character_manager.SetPathName(base_path)
				
				cls.RegisterCommon(base_path, PlayerJobsMotions['Common'])
				cls.RegisterBones(PlayerJobBones[job_index]['Bones'])
				
				# cls.RegisterJobsCommon(PlayerJobsMotions['JobsCommon'])
				#cls.RegisterGroupSkills(base_path, job['Skills'])
				#cls.RegisterSkills(job['Skills'])
				# cls.__RegisterIntroMotions(chr.MOTION_MODE_GENERAL, race['Intro'])
	
	@classmethod
	def RegisterCommon(cls, base_path: str, common: dict):
		for mode, info in common.items():
			character_manager.RegisterMotionMode(mode)
			character_manager.SetPathName(f"{base_path}{info['Path']}")
			
			for index, motion in info['Motions'].items():
				for value in tuple_up(motion):
					character_manager.RegisterCacheMotionData(mode, index, *value)
	
	@classmethod
	def RegisterJobsCommon(cls, common: dict):
		for mode, info in common:
			...
		

	@classmethod
	def RegisterGroupSkills(cls, base_path: str, skills: dict):
		character_manager.SetPathName(f"{base_path}{skills['Path']}")
		
		for skill_index, name in skills['Groups'].items():
			for index in range(skill.SKILL_EFFECT_COUNT):
				file_name = f'{name}.msa' if index == 0 else f'{name}_{index + 1}.msa'
				idx = chr.MOTION_SKILL + (index * skill.SKILL_GRADEGAP) + index
				
				character_manager.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, idx, file_name, 100)
	
	
	@classmethod
	def RegisterSkills(cls, skills: dict):
		for skill in skills:
			pass
		
		
	
	@classmethod
	def RegisterPlayerGeneralMotions(cls):
		"""
		for key, motion in PlayerGeneralMotions:
			for index, animation in motion:
				character_manager.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,
											   key,
											   animation[0], animation[1])
		"""
	
	@classmethod
	def __RegisterPlayerGeneralMotions(cls, mode, folder):
		character_manager.SetPathName(folder)
		character_manager.RegisterMotionMode(mode)

		"""
		for motion in PlayerGeneralMotions:
			character_manager.RegisterCacheMotionData(mode, motion[0], motion[1], motion[2])
		"""
		
	@classmethod
	def RegisterMotion(cls, motion: dict):
		character_manager.SetMotionRandomWeight(character.MOTION_MODE_GENERAL, character.MOTION_WAIT,
									 0, motion['General']['Weight'])
	
	@classmethod
	def RegisterCombos(cls, combo: dict):
		pass
	
	@classmethod
	def RegisterBones(cls, bones: dict):
		for index, name in bones.items():
			character_manager.RegisterAttachingBoneName(index, name)
	
	@classmethod
	def __RegisterIntroMotions(cls, mode, directory):
		character_manager.SetPathName(directory)
		character_manager.RegisterMotionMode(mode)

		"""
		for index, motion in data.PlayerIntroductionMotions.keys():
			character_manager.RegisterCacheMotionData(index, motion[0], motion[1])
		"""

	
	
	
def tuple_up(value):
	values = ()
	
	if not isinstance(value, tuple):
		values = ((value, 100), )
	else:
		values = value
	
	return values

