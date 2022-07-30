## System Imports


## Embedder Imports
from junctions import player
from junctions import character
from junctions import application


## Application imports


## Library Imports


battle_affects_path = '' # InterfaceInformation.GetBattleAffectsPathName()
bonus_affects_path = '' # InterfaceInformation.GetBonusAffectsPathName()
passive_affects_path = '' # InterfaceInformation.GetPassiveAffectsPathName()
fishing_affects_path = '' # InterfaceInformation.GetFishingAffectsPathName()

pattern_path = '' # InterfaceInformation.Metin2.METIN2_INTERFACE_PATTERN_PATH


AffectData: dict[int, tuple[str, str, str, int]] = {
	character.AFFECT_POISON: ('TOOLTIP_POISON_NAME', 'SKILL_TOXICDIE', f'{battle_affects_path}/poison.dds', 3),
	character.AFFECT_SLOW: 	('TOOLTIP_SLOW_NAME', 'SKILL_SLOW', f'{battle_affects_path}/slow.dds', 3),
	character.AFFECT_STUN: ('TOOLTIP_STUN_NAME', 'SKILL_STUN', f'{battle_affects_path}/stun.dds', 3),
	
	character.AFFECT_ATT_SPEED_POTION: ('TOOLTIP_ATTACK_SPEED_NAME', 'SKILL_INC_ATKSPD',
										f'{battle_affects_path}/attack_speed.dds', 4),
	character.AFFECT_MOV_SPEED_POTION: ('TOOLTIP_MOVEMENT_SPEED_NAME', 'SKILL_INC_MOVSPD',
										f'{bonus_affects_path}/move_speed.dds', 2),
	
	character.AFFECT_FISH_MIND: ('TOOLTIP_FISHMIND_NAME', 'SKILL_FISHMIND',
								 f'{fishing_affects_path}/fish_mind.dds', 5),
}


AffectData.update({
	character.AFFECT_JEONGWI: ('SKILL_JEONGWI_NAME', 'SKILL_JEONGWI', None, 1),
	character.AFFECT_GEOMGYEONG: ('SKILL_GEOMGYEONG_NAME', 'SKILL_GEOMGYEONG', None, 1),
	character.AFFECT_CHEONGEUN: ('SKILL_CHEONGEUN_NAME', 'SKILL_CHEONGEUN', None, 1),
	character.AFFECT_GYEONGGONG: ('SKILL_GYEONGGONG_NAME', 'SKILL_GYEONGGONG', None, 1),
	character.AFFECT_EUNHYEONG: ('SKILL_EUNHYEONG_NAME', 'SKILL_EUNHYEONG', None, 1),
	character.AFFECT_GWIGEOM: ('SKILL_GWIGEOM_NAME', 'SKILL_GWIGEOM', None, 1),
	character.AFFECT_GONGPO: ('SKILL_GONGPO_NAME', 'SKILL_GONGPO', None, 1),
	character.AFFECT_JUMAGAP: ('SKILL_JUMAGAP_NAME', 'SKILL_JUMAGAP', None, 1),
	character.AFFECT_HOSIN: ('SKILL_HOSIN_NAME', 'SKILL_HOSIN', None, 1),
	character.AFFECT_BOHO: ('SKILL_BOHO_NAME', 'SKILL_BOHO', None, 1),
	character.AFFECT_KWAESOK: ('SKILL_KWAESOK_NAME', 'SKILL_KWAESOK', None, 1),
	character.AFFECT_HEUKSIN: ('SKILL_HEUKSIN_NAME', 'SKILL_HEUKSIN', None, 1),
	character.AFFECT_MUYEONG: ('SKILL_MUYEONG_NAME', 'SKILL_MUYEONG', None, 1),
	character.AFFECT_GICHEON: ('SKILL_GICHEON_NAME', 'SKILL_GICHEON', None, 1),
	character.AFFECT_JEUNGRYEOK: ('SKILL_JEUNGRYEOK_NAME', 'SKILL_JEUNGRYEOK', None, 1),
	character.AFFECT_PABEOP: ('SKILL_PABEOP_NAME', 'SKILL_PABEOP', None, 1),
	character.AFFECT_FALLEN_CHEONGEUN: ('SKILL_CHEONGEUN_NAME', 'SKILL_CHEONGEUN', None, 1),
	
	# character.AFFECT_FIRE: ('SKILL_FIRE_NAME', 'SKILL_FIRE', None, 3),
})


AffectData.update({
	
	
	character.AFFECT_CHINA_FIREWORK: 			('SKILL_POWERFUL_STRIKE_NAME', 'SKILL_POWERFUL_STRIKE',
										  		'ui/metin2/skill/common/affect/powerfulstrike.tga', 5),
	
	character.NEW_AFFECT_EXP_BONUS:  			('TOOLTIP_MALL_EXPBONUS_NAME', 'TOOLTIP_MALL_EXPBONUS_STATIC',
											   	f'{bonus_affects_path}/exp.dds', 5),

	character.NEW_AFFECT_ITEM_BONUS: 			('TOOLTIP_MALL_ITEMBONUS_NAME', 'TOOLTIP_MALL_ITEMBONUS_STATIC',
											   	f'{bonus_affects_path}/items.dds', 6),
	character.NEW_AFFECT_SAFEBOX: 				('TOOLTIP_MALL_SAFEBOX_NAME', 'TOOLTIP_MALL_SAFEBOX',
											   	f'{passive_affects_path}/safebox.dds', 6),
	character.NEW_AFFECT_AUTOLOOT:            	('TOOLTIP_MALL_AUTOLOOT_NAME', 'TOOLTIP_MALL_AUTOLOOT',
												f'{passive_affects_path}/autoloot.dds', 6),
	character.NEW_AFFECT_FISH_MIND:           	('TOOLTIP_MALL_FISH_MIND_NAME', 'TOOLTIP_MALL_FISH_MIND',
												f'{fishing_affects_path}/fish_mind.dds', 6),
	character.NEW_AFFECT_MARRIAGE_FAST:       	('TOOLTIP_MALL_MARRIAGE_FAST_NAME', 'TOOLTIP_MALL_MARRIAGE_FAST',
												f'{passive_affects_path}/love_points.dds', 6),
	character.NEW_AFFECT_GOLD_BONUS:          	('TOOLTIP_MALL_MARRIAGE_FAST_NAME', 'TOOLTIP_MALL_MARRIAGE_FAST',
												f'{passive_affects_path}/gold.dds', 6),

	character.NEW_AFFECT_NO_DEATH_PENALTY:    	('TOOLTIP_APPLY_NO_DEATH_PENALTY_NAME', 'TOOLTIP_APPLY_NO_DEATH_PENALTY',
												f'{passive_affects_path}/gold_premium.tga', 3),
	character.NEW_AFFECT_SKILL_BOOK_BONUS:    	('TOOLTIP_APPLY_SKILL_BOOK_BONUS_NAME', 'TOOLTIP_APPLY_SKILL_BOOK_BONUS',
												f'{bonus_affects_path}/learning_bless.dds', 3),
	character.NEW_AFFECT_SKILL_BOOK_NO_DELAY: 	('TOOLTIP_APPLY_SKILL_BOOK_NO_DELAY_NAME', 'TOOLTIP_APPLY_SKILL_BOOK_NO_DELAY',
												f'{bonus_affects_path}/learning_bless.dds', 3),


	character.NEW_AFFECT_AUTO_HP_RECOVERY:    	('TOOLTIP_AUTO_POTION_REST_NAME', 'TOOLTIP_AUTO_POTION_REST',
												f'{pattern_path}/auto_hpgauge/05.dds', 4),
	character.NEW_AFFECT_AUTO_SP_RECOVERY:    	('TOOLTIP_AUTO_POTION_REST_NAME', 'TOOLTIP_AUTO_POTION_REST',
												f'{pattern_path}/auto_spgauge/05.dds', 4)
})


MallIndex = 1000
common_affects_path = 'ui/metin2/skill/common/affect/'

AffectData.update({
	character.NEW_AFFECT_AUTO_HP_RECOVERY:		('TOOLTIP_AUTO_POTION_REST_NAME', 'TOOLTIP_AUTO_POTION_REST',
												f'{common_affects_path}/gold_premium.tga', 4),
	
	character.NEW_AFFECT_AUTO_SP_RECOVERY:		('TOOLTIP_AUTO_POTION_REST_NAME', 'TOOLTIP_AUTO_POTION_REST',
												f'{common_affects_path}/gold_bonus.tga', 4),
	
	
	MallIndex+player.POINT_MALL_ATTBONUS: 		('TOOLTIP_MALL_ATTBONUS_STATIC_NAME', 'TOOLTIP_MALL_ATTBONUS_STATIC',
												f'{common_affects_path}/att_bonus.tga', 6),
	
	MallIndex+player.POINT_MALL_DEFBONUS: 		('TOOLTIP_MALL_DEFBONUS_STATIC_NAME', 'TOOLTIP_MALL_DEFBONUS_STATIC',
												f'{common_affects_path}/def_bonus.tga', 6),
	
	MallIndex+player.POINT_MALL_EXPBONUS: 		('TOOLTIP_MALL_EXPBONUS_NAME', 'TOOLTIP_MALL_EXPBONUS',
												f'{bonus_affects_path}/exp.dds', 6),
	
	MallIndex+player.POINT_MALL_ITEMBONUS: 		('TOOLTIP_MALL_ITEMBONUS_NAME', 'TOOLTIP_MALL_ITEMBONUS',
												f'{common_affects_path}/item_bonus.tga', 6),
	
	MallIndex+player.POINT_MALL_GOLDBONUS: 		('TOOLTIP_MALL_GOLDBONUS_NAME', 'TOOLTIP_MALL_GOLDBONUS',
												f'{common_affects_path}/gold_bonus.tga', 6),
	
	MallIndex+player.POINT_CRITICAL_PCT: 		('TOOLTIP_APPLY_CRITICAL_PCT_NAME', 'TOOLTIP_APPLY_CRITICAL_PCT',
												f'{common_affects_path}/critical.tga', 6),
	
	MallIndex+player.POINT_PENETRATE_PCT: 		('TOOLTIP_APPLY_PENETRATE_PCT_NAME', 'TOOLTIP_APPLY_PENETRATE_PCT',
												f'{common_affects_path}/gold_premium.tga', 6),
	
	MallIndex+player.POINT_MAX_HP_PCT:			('TOOLTIP_MAX_HP_PCT_NAME', 'TOOLTIP_MAX_HP_PCT',
												f'{common_affects_path}/gold_premium.tga', 6),
	
	MallIndex+player.POINT_MAX_SP_PCT:			('TOOLTIP_MAX_SP_PCT_NAME', 'TOOLTIP_MAX_SP_PCT',
												f'{common_affects_path}/gold_premium.tga', 6),
	
	
	MallIndex+player.POINT_PC_BANG_EXP_BONUS: 	('TOOLTIP_MALL_EXPBONUS_P_STATIC_NAME', 'TOOLTIP_MALL_EXPBONUS_P_STATIC',
												f'{common_affects_path}/EXP_Bonus_p_on.tga', 6),
	
	MallIndex+player.POINT_PC_BANG_DROP_BONUS: 	('TOOLTIP_MALL_ITEMBONUS_P_STATIC_NAME', 'TOOLTIP_MALL_ITEMBONUS_P_STATIC',
												f'{common_affects_path}/Item_Bonus_p_on.tga', 6),
	
})


if application.ENABLE_DRAGON_SOUL_SYSTEM:
	AffectData.update({
		character.NEW_AFFECT_DRAGON_SOUL_DECK1: ('TOOLTIP_DRAGON_SOUL_DECK1', '',
												 'ui/metin2/dragounsoul/buff_ds_sky1.tga', 7),
		
		character.NEW_AFFECT_DRAGON_SOUL_DECK2: ('TOOLTIP_DRAGON_SOUL_DECK2', '',
												 'ui/metin2/dragonsoul/buff_ds_land1.tga', 7)
	})
	
