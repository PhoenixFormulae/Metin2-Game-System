## System Imports

## Embedder Imports
from junctions import character
from junctions import character_manager

## Application Imports
from Settings.Game.Player.Emotions.enums import Emotion

## Library Imports


PlayerEmotions = {
	Emotion.Clap:           ('EMOTION_CLAP',            'clap'),
	Emotion.Dance1:         ('EMOTION_DANCE_1',         'dance1'),
	Emotion.Dance2:         ('EMOTION_DANCE_2', 	    'dance2'),
	Emotion.Dance3:         ('EMOTION_DANCE_3', 		'dance3'),
	Emotion.Dance4:         ('EMOTION_DANCE_4', 		'dance4'),
	Emotion.Dance5:         ('EMOTION_DANCE_5', 		'dance5'),
	Emotion.Dance6:         ('EMOTION_DANCE_6', 		'dance6'),
	Emotion.Congratulate:   ('EMOTION_CONGRATULATION',	'congratulate'),
	Emotion.Forgive:        ('EMOTION_FORGIVE', 		'forgive'),
	Emotion.Anger:          ('EMOTION_ANGRY', 			'angry'),
	Emotion.Attract:        ('EMOTION_ATTRACTIVE', 		'attract'),
	Emotion.Sad:            ('EMOTION_SAD', 			'sad'),
	Emotion.Shy:            ('EMOTION_SHY', 			'shy'),
	Emotion.Cheer:          ('EMOTION_CHEERUP', 		'cheer'),
	Emotion.Banter:         ('EMOTION_BANTER', 			'banter'),
	Emotion.Joy:            ('EMOTION_JOY', 			'joy'),
	Emotion.Cheer1:         ('EMOTION_CHEERS_1', 		'cheer1'),
	Emotion.Cheer2:         ('EMOTION_CHEERS_2', 		'cheer2'),
	Emotion.Kiss:           ('EMOTION_CLAP_KISS', 	    'kiss'),
	Emotion.FrenchKiss:     ('EMOTION_FRENCH_KISS', 	'french_kiss'),
	Emotion.Slap:           ('EMOTION_SLAP', 			'slap'),
}


PlayerEmoticonsIcons: dict[int, str] = {
	Emotion.Clap:           'clap.tga',
	Emotion.Cheer1:         'cheers_1.tga',
	Emotion.Cheer2:         'cheers_2.tga',
	Emotion.Congratulate:   'congratulation.tga',
	Emotion.Forgive:        'forgive.tga',
	Emotion.Anger:          'angry.tga',
	Emotion.Attract:        'attractive.tga',
	Emotion.Sad:            'sad.tga',
	Emotion.Shy:            'shy.tga',
	Emotion.Cheer:          'cheerup.tga',
	Emotion.Banter:         'banter.tga',
	Emotion.Joy:            'joy.tga',
	Emotion.Dance1:         'dance_1.tga',
	Emotion.Dance2:         'dance_2.tga',
	Emotion.Dance3:         'dance_3.tga',
	Emotion.Dance4:         'dance_4.tga',
	Emotion.Dance5:         'dance_5.tga',
	Emotion.Dance6:         'dance_6.tga',
	Emotion.Kiss:           'kiss.tga',
	Emotion.FrenchKiss:     'french_kiss.tga',
	Emotion.Slap:           'slap.tga',
}


PlayerEmotionMotions: dict[int, str] = {
	character.MOTION_CLAP:	                    'clap.msa',
	character.MOTION_CHEERS_1:	                'cheers_1.msa',
	character.MOTION_CHEERS_2:	                'cheers_2.msa',
	character.MOTION_DANCE_1:	                    'dance_1.msa',
	character.MOTION_DANCE_2:	                    'dance_2.msa',
	character.MOTION_DANCE_3:	                    'dance_3.msa',
	character.MOTION_DANCE_4:	                    'dance_4.msa',
	character.MOTION_DANCE_5:	                    'dance_5.msa',
	character.MOTION_DANCE_6:	                    'dance_6.msa',
	character.MOTION_CONGRATULATION:	            'congratulation.msa',
	character.MOTION_FORGIVE:	                    'forgive.msa',
	character.MOTION_ANGRY:	                    'angry.msa',
	character.MOTION_ATTRACTIVE:	                'attractive.msa',
	character.MOTION_SAD:	                        'sad.msa',
	character.MOTION_SHY:	                        'shy.msa',
	character.MOTION_CHEERUP:	                    'cheerup.msa',
	character.MOTION_BANTER:	                    'banter.msa',
	character.MOTION_JOY:                 	    'joy.msa',
	character.MOTION_FRENCH_KISS_WITH_WARRIOR:	'french_kiss_with_warrior.msa',
	character.MOTION_FRENCH_KISS_WITH_ASSASSIN:	'french_kiss_with_assassin.msa',
	character.MOTION_FRENCH_KISS_WITH_SURA:	    'french_kiss_with_sura.msa',
	character.MOTION_FRENCH_KISS_WITH_SHAMAN:	    'french_kiss_with_shaman.msa',
	character.MOTION_KISS_WITH_WARRIOR:	        'kiss_with_warrior.msa',
	character.MOTION_KISS_WITH_ASSASSIN:	        'kiss_with_assassin.msa',
	character.MOTION_KISS_WITH_SURA:	            'kiss_with_sura.msa',
	character.MOTION_KISS_WITH_SHAMAN:	        'kiss_with_shaman.msa',
	character.MOTION_SLAP_HIT_WITH_WARRIOR:	    'slap_hit.msa',
	character.MOTION_SLAP_HIT_WITH_ASSASSIN:	    'slap_hit.msa',
	character.MOTION_SLAP_HIT_WITH_SURA:	        'slap_hit.msa',
	character.MOTION_SLAP_HIT_WITH_SHAMAN:	    'slap_hit.msa',
	character.MOTION_SLAP_HURT_WITH_WARRIOR:	    'slap_hurt.msa',
	character.MOTION_SLAP_HURT_WITH_ASSASSIN:	    'slap_hurt.msa',
	character.MOTION_SLAP_HURT_WITH_SURA:	        'slap_hurt.msa',
	character.MOTION_SLAP_HURT_WITH_SHAMAN:	    'slap_hurt.msa',
}


ChatEmoticons: dict[int, tuple[str, str]] = {
	character_manager.EFFECT_EMOTICON + 0:     ('', '(È²ï¿½ï¿½)', 		'sweat.mse'),
	character_manager.EFFECT_EMOTICON + 1:     ('', '(ï¿½ï¿½)', 		'money.mse'),
	character_manager.EFFECT_EMOTICON + 2:     ('', '(ï¿½ï¿½ï¿½)', 	'happy.mse'),
	character_manager.EFFECT_EMOTICON + 3:     ('', '(ï¿½ï¿½ï¿½ï¿½)', 	'love_s.mse'),
	character_manager.EFFECT_EMOTICON + 4:     ('', '(ï¿½ï¿½ï¿½)', 	'love_l.mse'),
	character_manager.EFFECT_EMOTICON + 5:     ('', '(ï¿½Ð³ï¿½)', 		'angry.mse'),
	character_manager.EFFECT_EMOTICON + 6:     ('', '(ï¿½ï¿½ï¿½ï¿½)', 	'aha.mse'),
	character_manager.EFFECT_EMOTICON + 7:     ('', '(ï¿½ï¿½ï¿½)', 	'gloom.mse'),
	character_manager.EFFECT_EMOTICON + 8:     ('', '(ï¿½Ë¼ï¿½)', 		'sorry.mse'),
	character_manager.EFFECT_EMOTICON + 9:     ('', '(!)', 			'!_mix_back.mse'),
	character_manager.EFFECT_EMOTICON + 10:    ('', '(?)', 			'question.mse'),
	character_manager.EFFECT_EMOTICON + 11:    ('', '(fish)', 			'fish.mse'),
}
