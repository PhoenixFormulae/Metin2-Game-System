## System Imports

## Embedder Imports

## Application Imports
from Settings.Game.Player.enums import WarriorSkillGroup, Job, ShamanSkillGroup, SuraSkillGroup, \
	AssassinSkillGroup

## Library Imports


JobsPassiveSkills: tuple = (122, 123, 121, 124, 125, 129, 0, 0, 130, 131, 141, 142,)

JobsSkills: dict[int, dict[int, list[int]]] = {
	
	Job.Warrior: {
		WarriorSkillGroup.Aura: [1, 2, 3, 4, 5, 6, 0, 0, 137, 0, 138, 0, 139, 0],
		WarriorSkillGroup.Mental: [16, 17, 18, 19, 20, 21, 0, 0, 137, 0, 138, 0, 139, 0],
	},
	
	Job.Assassin: {
		AssassinSkillGroup.Dagger: [31, 32, 33, 34, 35, 36, 0, 0, 137, 0, 138, 0, 139, 0, 140],
		AssassinSkillGroup.Bow: [46, 47, 48, 49, 50, 51, 0, 0, 137, 0, 138, 0, 139, 0, 140],
	},
	
	Job.Sura: {
		SuraSkillGroup.Weapons: [61, 62, 63, 64, 65, 66, 0, 0, 137, 0, 138, 0, 139, 0],
		SuraSkillGroup.Magic: [76, 77, 78, 79, 80, 81, 0, 0, 137, 0, 138, 0, 139, 0],
	},
	
	Job.Shaman: {
		ShamanSkillGroup.Blessing: [91, 92, 93, 94, 95, 96, 0, 0, 137, 0, 138, 0, 139, 0],
		ShamanSkillGroup.Dragon: [106, 107, 108, 109, 110, 111, 0, 0, 137, 0, 138, 0, 139, 0],
	},
}

GuildPassiveSkills: list[int] = [151, ]
GuildActiveSkills: list[int] = [152, 153, 154, 155, 156, 157, ]

