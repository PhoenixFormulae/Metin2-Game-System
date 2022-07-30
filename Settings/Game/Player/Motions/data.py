## System Imports

## Embedder Imports
from junctions import character

## Application Imports
from Settings.Game.Player.enums import HorseSkill, Job, Race, GuildSkill

## Library Imports


PlayerJobsMotions = {
	'Common': {
		character.MOTION_MODE_GENERAL: {
			'Path': 'general/',
			'Motions': {
				character.MOTION_WAIT: 'wait.msa',
				character.MOTION_WALK: 'walk.msa',
				character.MOTION_RUN: 'run.msa',
				character.MOTION_DAMAGE: (('damage.msa', 50), ('damage_1.msa', 50)),
				character.MOTION_DAMAGE_BACK: (('damage_2.msa', 50), ('damage_3.msa', 50)),
				character.MOTION_DAMAGE_FLYING: 'damage_flying.msa',
				character.MOTION_STAND_UP: 'falling_stand.msa',
				character.MOTION_DAMAGE_FLYING_BACK: 'back_damage_flying.msa',
				character.MOTION_STAND_UP_BACK: 'back_falling_stand.msa',
				character.MOTION_DEAD: 'dead.msa',
				character.MOTION_DIG: 'dig.msa',
			}
		},
		
		character.MOTION_MODE_HORSE: {
			'Path': 'horse/',
			'Motions': {
				character.MOTION_WAIT: (('wait.msa', 90), ('wait_1.msa', 9), ('wait_2.msa', 1)),
				character.MOTION_WALK: 'walk.msa',
				character.MOTION_RUN: 'run.msa',
				character.MOTION_DAMAGE: 'damage.msa',
				character.MOTION_DAMAGE_BACK: 'damage.msa',
				character.MOTION_DEAD: 'dead.msa',
				HorseSkill.Charge: 'skill_charge.msa',
				HorseSkill.Splash: 'skill_splash.msa',
			},
		},
		
		character.MOTION_MODE_FISHING: {
			'Path': 'fishing/',
			'Motions': {
				character.MOTION_WAIT: 'wait.msa',
				character.MOTION_WALK: 'walk.msa',
				character.MOTION_RUN: 'run.msa',
				character.MOTION_FISHING_THROW: 'throw.msa',
				character.MOTION_FISHING_WAIT: 'fishing_wait.msa',
				character.MOTION_FISHING_STOP: 'fishing_cancel.msa',
				character.MOTION_FISHING_REACT: 'fishing_react.msa',
				character.MOTION_FISHING_CATCH: 'fishing_catch.msa',
				character.MOTION_FISHING_FAIL: 'fishing_fail.msa',
			},
		}
	},
	
	'JobsCommon': {
		'Skill': {
			'Guild': {
				GuildSkill.DragonBlood: 'guild_yongsinuipi',
				GuildSkill.DragonBless: 'guild_yongsinuichukbok',
				GuildSkill.BlessArmor: 'guild_seonghwigap',
				GuildSkill.Speedup: 'guild_gasokhwa',
				GuildSkill.DragonWrath: 'guild_yongsinuibunno',
				GuildSkill.MagicUp: 'guild_jumunsul',
			},
		},
	},
	
	'Jobs': {
		Job.Warrior: {
			'Race': {
				Race.WarriorMale: {
					'BasePath': 'd:/ymir work/pc/warrior/'
				},
				Race.WarriorFemale: {
					'BasePath': 'd:/ymir work/pc2/warrior/'
				},
			},
			
			'General': {
				character.MOTION_WAIT: [('wait_1.msa', 30)],
				character.MOTION_COMBO_ATTACK_1: [('attack.msa', 50), ('attack_1.msa', 50)],
			},
			
			'Skills': {
				'Path': 'skill/',
				
				'Groups': {
					1: 'samyeon',
					2: 'palbang',
					3: 'jeongwi',
					4: 'geomgyeong',
					5: 'tanhwan',
					6: 'gihyeol',
					
					16: 'gigongcham',
					17: 'gyeoksan',
					18: 'daejin',
					19: 'cheongeun',
					20: 'geompung',
					21: 'noegeom',
				},
				
				'Battle': {
					character.MOTION_MODE_ONEHAND_SWORD: {
						'Path': 'onehand_sword',
						'Values': {
							character.MOTION_WAIT: [('wait.msa', 50), ('wait_1.msa', 50)],
							character.MOTION_WALK: ['walk.msa', 50],
							character.MOTION_RUN: ['run.msa'],
							character.MOTION_DAMAGE: [('damage.msa', 50), ('damage_1.msa', 50)],
							character.MOTION_DAMAGE_BACK: [('damage_2.msa', 50), ('damage_3.msa', 50)],
							character.MOTION_COMBO_ATTACK_1: ['combo_01.msa'],
							character.MOTION_COMBO_ATTACK_2: ['combo_02.msa'],
							character.MOTION_COMBO_ATTACK_3: ['combo_03.msa'],
							character.MOTION_COMBO_ATTACK_4: ['combo_04.msa'],
							character.MOTION_COMBO_ATTACK_5: ['combo_05.msa'],
							character.MOTION_COMBO_ATTACK_6: ['combo_06.msa'],
							character.MOTION_COMBO_ATTACK_7: ['combo_07.msa'],
							character.MOTION_CHANGE_WEAPON: ['change_weapon.msa'],
							
							'Combos': {
								1: {
									0: character.MOTION_COMBO_ATTACK_1,
									1: character.MOTION_COMBO_ATTACK_2,
									2: character.MOTION_COMBO_ATTACK_3,
									3: character.MOTION_COMBO_ATTACK_4,
								},
								2: {
									0: character.MOTION_COMBO_ATTACK_1,
									1: character.MOTION_COMBO_ATTACK_2,
									2: character.MOTION_COMBO_ATTACK_3,
									3: character.MOTION_COMBO_ATTACK_5,
									4: character.MOTION_COMBO_ATTACK_7,
								},
								3: {
									0: character.MOTION_COMBO_ATTACK_1,
									1: character.MOTION_COMBO_ATTACK_2,
									2: character.MOTION_COMBO_ATTACK_3,
									3: character.MOTION_COMBO_ATTACK_5,
									4: character.MOTION_COMBO_ATTACK_6,
									5: character.MOTION_COMBO_ATTACK_4,
								},
							},
						},
					},
					
					character.MOTION_MODE_TWOHAND_SWORD: {
						'Path': 'twohand_sword',
						'Values': {
							character.MOTION_WAIT: [('wait.msa', 50), ('wait_1.msa', 50)],
							character.MOTION_WALK: ['walk.msa', 50],
							character.MOTION_RUN: ['run.msa'],
							character.MOTION_DAMAGE: [('damage.msa', 50), ('damage_1.msa', 50)],
							character.MOTION_DAMAGE_BACK: [('damage_2.msa', 50), ('damage_3.msa', 50)],
							character.MOTION_COMBO_ATTACK_1: ['combo_01.msa'],
							character.MOTION_COMBO_ATTACK_2: ['combo_02.msa'],
							character.MOTION_COMBO_ATTACK_3: ['combo_03.msa'],
							character.MOTION_COMBO_ATTACK_4: ['combo_04.msa'],
							character.MOTION_COMBO_ATTACK_5: ['combo_05.msa'],
							character.MOTION_COMBO_ATTACK_6: ['combo_06.msa'],
							character.MOTION_COMBO_ATTACK_7: ['combo_07.msa'],
							character.MOTION_CHANGE_WEAPON: ['change_weapon.msa'],
							
							'Combo': {
								1: {
									0: character.MOTION_COMBO_ATTACK_1,
									1: character.MOTION_COMBO_ATTACK_2,
									2: character.MOTION_COMBO_ATTACK_3,
									3: character.MOTION_COMBO_ATTACK_4,
								},
								2: {
									0: character.MOTION_COMBO_ATTACK_1,
									1: character.MOTION_COMBO_ATTACK_2,
									2: character.MOTION_COMBO_ATTACK_3,
									3: character.MOTION_COMBO_ATTACK_5,
									4: character.MOTION_COMBO_ATTACK_7,
								},
								3: {
									0: character.MOTION_COMBO_ATTACK_1,
									1: character.MOTION_COMBO_ATTACK_2,
									2: character.MOTION_COMBO_ATTACK_3,
									3: character.MOTION_COMBO_ATTACK_5,
									4: character.MOTION_COMBO_ATTACK_6,
									5: character.MOTION_COMBO_ATTACK_4,
								},
							},
						},
					},
					
					character.MOTION_MODE_HORSE_ONEHAND_SWORD: {
						'Path': 'horse_onehand_sword',
						'Values': {
						
						},
						
						'Combo': {
							character.MOTION_COMBO_ATTACK_1: {'combo_01.msa'},
							character.MOTION_COMBO_ATTACK_2: {'combo_02.msa'},
							character.MOTION_COMBO_ATTACK_3: {'COMBO_03.MSA'},
						},
						
					},
					
					character.MOTION_MODE_HORSE_TWOHAND_SWORD: {
						'Path': 'horse_twohand_sword',
						'Values': {
							character.MOTION_COMBO_ATTACK_1: {'combo_01.msa'},
							character.MOTION_COMBO_ATTACK_2: {'combo_02.msa'},
							character.MOTION_COMBO_ATTACK_3: {'COMBO_03.MSA'},
						},
						
						'Combo': {
							character.MOTION_COMBO_ATTACK_1: {'combo_01.msa'},
							character.MOTION_COMBO_ATTACK_2: {'combo_02.msa'},
							character.MOTION_COMBO_ATTACK_3: {'COMBO_03.MSA'},
						},
						
					}
					
				}
			}
		},
		
		Job.Assassin: {
			'Race': {
				Race.AssassinMale: {
					'BasePath': 'd:/ymir work/pc/assassin/'
				},
				Race.AssassinFemale: {
					'BasePath': 'd:/ymir work/pc2/assassin/'
				},
			},
			
			'General': {
				character.MOTION_WAIT: [('wait_1.msa', 30)],
				character.MOTION_COMBO_ATTACK_1: [('attack.msa', 50), ('attack_1.msa', 50)],
			},
			
			'Skills': {
				'Path': 'skill/',
				
				'Groups': {
					1: 'amseup',
					2: 'gungsin',
					3: 'charyun',
					4: 'eunhyeong',
					5: 'sangong',
					6: 'seomjeon',
					
					16: 'yeonsa',
					17: 'gwangyeok',
					18: 'hwajo',
					19: 'gyeonggong',
					20: 'dokgigung',
					21: 'seomgwang',
				},
			},
			
			'Battle': {
				character.MOTION_MODE_ONEHAND_SWORD: {
					'Path': 'onehand_sword',
					'Values': {
						character.MOTION_WAIT: [('wait.msa', 50), ('wait_1.msa', 50)],
						character.MOTION_WALK: ['walk.msa', 50],
						character.MOTION_RUN: ['run.msa'],
						character.MOTION_DAMAGE: [('damage.msa', 50), ('damage_1.msa', 50)],
						character.MOTION_DAMAGE_BACK: [('damage_2.msa', 50), ('damage_3.msa', 50)],
						character.MOTION_COMBO_ATTACK_1: ['combo_01.msa'],
						character.MOTION_COMBO_ATTACK_2: ['combo_02.msa'],
						character.MOTION_COMBO_ATTACK_3: ['combo_03.msa'],
						character.MOTION_COMBO_ATTACK_4: ['combo_04.msa'],
						character.MOTION_COMBO_ATTACK_5: ['combo_05.msa'],
						character.MOTION_COMBO_ATTACK_6: ['combo_06.msa'],
						character.MOTION_COMBO_ATTACK_7: ['combo_07.msa'],
						character.MOTION_CHANGE_WEAPON: ['change_weapon.msa'],
						
						'Combo': {
							1: {
								0: character.MOTION_COMBO_ATTACK_1,
								1: character.MOTION_COMBO_ATTACK_2,
								2: character.MOTION_COMBO_ATTACK_3,
								3: character.MOTION_COMBO_ATTACK_4,
							},
							2: {
								0: character.MOTION_COMBO_ATTACK_1,
								1: character.MOTION_COMBO_ATTACK_2,
								2: character.MOTION_COMBO_ATTACK_3,
								3: character.MOTION_COMBO_ATTACK_5,
								4: character.MOTION_COMBO_ATTACK_7,
							},
							3: {
								0: character.MOTION_COMBO_ATTACK_1,
								1: character.MOTION_COMBO_ATTACK_2,
								2: character.MOTION_COMBO_ATTACK_3,
								3: character.MOTION_COMBO_ATTACK_5,
								4: character.MOTION_COMBO_ATTACK_6,
								5: character.MOTION_COMBO_ATTACK_4,
							},
						},
					},
				},
			},
		}
	}
}

PlayerJobBones: dict[int, dict[str, list | dict[int, str]]] = {
	Job.Warrior: {
		'Races': [Race.WarriorMale, Race.WarriorFemale],
		'Bones': {
			character.PART_WEAPON: 'equip_right_hand',
			# chr.PART_ACCE: "Bip01 Spine2",
		}
	},
	
	Job.Assassin: {
		'Races': [Race.AssassinMale, Race.AssassinFemale],
		'Bones': {
			character.PART_WEAPON: 'equip_right',
			character.PART_WEAPON_LEFT: 'equip_left'
		}
	},
	
	Job.Sura: {
		'Races': [Race.SuraMale, Race.SuraFemale],
		'Bones': {
			character.PART_WEAPON: 'equip_right'
		}
	},
	
	Job.Shaman: {
		'Races': [Race.ShamanMale, Race.ShamanFemale],
		'Bones': {
			character.PART_WEAPON: 'equip_right',
			character.PART_WEAPON_LEFT: 'equip_left'
		}
	},
}


PlayerRaces = {
	'Common': {
		'Intro': {
			character.MOTION_INTRO_WAIT: 			'wait.msa',
			character.MOTION_INTRO_SELECTED: 		'selected.msa',
			character.MOTION_INTRO_NOT_SELECTED: 	'not_selected.msa',
		}
	},
	
	'Races': {
		Race.WarriorMale: {
			'RaceData': (
				'warrior_m.msm'
			),
			'Intro': 'd:/ymir work/pc/warrior/intro/'
		},
		
		Race.WarriorFemale: {
			'RaceData': (
				'warrior_w.msm'
			),
			'Intro': 'd:/ymir work/pc2/warrior/intro/'
		},
		
		Race.AssassinMale: {
			'RaceData': (
				'assassin_m.msm'
			),
			'Intro': 'd:/ymir work/pc/assassin/intro/'
		},
		
		Race.AssassinFemale: {
			'RaceData': (
				'assassin_w.msm'
			),
			'Intro': 'd:/ymir work/pc2/assassin/intro/'
		},
		
		Race.SuraMale: {
			'RaceData': (
				'sura_m.msm'
			),
			'Intro': 'd:/ymir work/pc/sura/intro/'
		},
		
		Race.SuraFemale: {
			'RaceData': (
				'sura_w.msm'
			),
			'Intro': 'd:/ymir work/pc2/sura/intro/'
		},
		
		Race.ShamanMale: {
			'RaceData': (
				'shaman_m.msm'
			),
			'Intro': 'd:/ymir work/pc/shaman/intro/'
		},
		
		Race.ShamanFemale: {
			'RaceData': (
				'shaman_w.msm'
			),
			'Intro': 'd:/ymir work/pc2/shaman/intro/'
		},
	}
}
