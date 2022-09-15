# Standard Imports
from enum import unique, IntEnum


# Embedder Imports
from junctions import character

# Library Imports

# External Imports


@unique
class Job(IntEnum):
	
	Warrior    	= 0
	Assassin    = 1
	Sura        = 2
	Shaman      = 3


@unique
class Race(IntEnum):
	
	WarriorMale    	= 0
	AssassinFemale 	= 1
	SuraMale       	= 2
	ShamanFemale   	= 3
	WarriorFemale  	= 4
	AssassinMale   	= 5
	SuraFemale     	= 6
	ShamanMale     	= 7


@unique
class Combo(IntEnum):
	
	Normal = 0
	Medium = 1
	Expert = 2


@unique
class ComboIndex(IntEnum):
	
	COMBO_INDEX_1 = 0
	COMBO_INDEX_2 = 1
	COMBO_INDEX_3 = 2
	COMBO_INDEX_4 = 3
	COMBO_INDEX_5 = 4
	COMBO_INDEX_6 = 5


@unique
class WarriorSkillGroup(IntEnum):
	
	Aura = 0
	Mental = 1


@unique
class AssassinSkillGroup(IntEnum):
	
	Dagger = 0
	Bow = 1


@unique
class SuraSkillGroup(IntEnum):
	
	Weapons = 0
	Magic = 1


@unique
class ShamanSkillGroup(IntEnum):
	
	Blessing = 0
	Dragon = 1


@unique
class HorseSkill(IntEnum):
	
	WildAttack = character.MOTION_SKILL + 121
	Charge = character.MOTION_SKILL + 122
	Splash = character.MOTION_SKILL + 123


@unique
class GuildSkill(IntEnum):
	
	DragonBlood = character.MOTION_SKILL + 101
	DragonBless = character.MOTION_SKILL + 102
	BlessArmor = character.MOTION_SKILL + 103
	Speedup = character.MOTION_SKILL + 104
	DragonWrath = character.MOTION_SKILL + 105
	MagicUp = character.MOTION_SKILL + 106
	
