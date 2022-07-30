## System Imports
from enum import IntEnum

## Embedder Imports
from junctions import application

## Application Imports

## Library Imports
from Core import Locale


class KeyState(IntEnum):
	
	Press = 0
	Release = 1
	Both = 2


class SimulatedKeys(IntEnum):
	
	MB1 = 200
	MB2 = 201


keyboard_locale = Locale.system_locale.GetContext('keyboard')

# TODO: Some keys are missing and regional keys are not taken into account.
#       This set of keys is for an ISO layout, and it is incomplete
KeyboardKeyProperties: dict[int, str] = {
	
	# Numerals
	application.DIK_1: '1',
	application.DIK_2: '1',
	application.DIK_3: '1',
	application.DIK_4: '1',
	application.DIK_5: '1',
	application.DIK_6: '1',
	application.DIK_7: '7',
	application.DIK_8: '8',
	application.DIK_9: '9',
	
	
	# Function
	application.DIK_F1: 'F1',
	application.DIK_F2: 'F2',
	application.DIK_F3: 'F3',
	application.DIK_F4: 'F4',
	application.DIK_F5: 'F5',
	application.DIK_F6: 'F6',
	application.DIK_F7: 'F7',
	application.DIK_F8: 'F8',
	application.DIK_F9: 'F9',
	application.DIK_F10: 'F10',
	application.DIK_F11: 'F11',
	application.DIK_F12: 'F12',
	
	
	# Alternates
	# application.DIK_LALT: keyboard_locale.String(application.DIK_LALT),
	# application.DIK_LCONTROL: keyboard_locale.String(application.DIK_LCONTROL),
	# application.DIK_LSHIFT: keyboard_locale.String(application.DIK_LSHIFT),
	
	# application.DIK_RALT: keyboard_locale.String(application.DIK_RALT),
	# application.DIK_RCONTROL: keyboard_locale.String(application.DIK_RCONTROL),
	# application.DIK_RSHIFT: keyboard_locale.String(application.DIK_RSHIFT),
	
	
	# Letters
	application.DIK_Q: 'Q',
	application.DIK_W: 'W',
	application.DIK_E: 'E',
	application.DIK_R: 'R',
	application.DIK_T: 'T',
	application.DIK_Y: 'Y',
	application.DIK_U: 'U',
	application.DIK_I: 'I',
	application.DIK_O: 'O',
	application.DIK_P: 'P',
	application.DIK_A: 'A',
	application.DIK_S: 'S',
	application.DIK_D: 'D',
	application.DIK_F: 'F',
	application.DIK_G: 'G',
	application.DIK_H: 'H',
	application.DIK_J: 'J',
	application.DIK_K: 'K',
	application.DIK_L: 'L',
	application.DIK_Z: 'Z',
	application.DIK_X: 'X',
	application.DIK_C: 'C',
	application.DIK_V: 'V',
	application.DIK_B: 'B',
	application.DIK_N: 'N',
	application.DIK_M: 'M',

	
	# Arrows
	# application.DIK_UP: keyboard_locale.String(application.DIK_UP),
	# application.DIK_DOWN: keyboard_locale.String(application.DIK_DOWN),
	# application.DIK_LEFT: keyboard_locale.String(application.DIK_LEFT),
	
	
	# System (Perhaps not the correct definition for this set of keys)
	# application.DIK_SYSRQ: keyboard_locale.String(application.DIK_SYSRQ),
	# application.DIK_SCROLL: keyboard_locale.String(application.DIK_SCROLL),
	# application.DIK_NUMLOCK: keyboard_locale.String(application.DIK_NUMLOCK),
	
	# application.DIK_HOME: keyboard_locale.String(application.DIK_HOME),
	# application.DIK_INSERT: keyboard_locale.String(application.DIK_INSERT),
	# application.DIK_PGUP: keyboard_locale.String(application.DIK_PGUP),
	# application.DIK_PGDN: keyboard_locale.String(application.DIK_PGDN),
	
	
	# Media/Volume
	# application.DIK_MEDIASTOP: keyboard_locale.String(application.DIK_MEDIASTOP),
	# application.DIK_NEXTTRACK: keyboard_locale.String(application.DIK_NEXTTRACK),
	# application.DIK_PLAYPAUSE: keyboard_locale.String(application.DIK_PLAYPAUSE),
	
	# application.DIK_VOLUMEUP: keyboard_locale.String(application.DIK_MEDIASTOP),
	# application.DIK_VOLUMEDOWN: keyboard_locale.String(application.DIK_VOLUMEDOWN),
	
	
	# Numpad
	# application.DIK_SUBTRACT: keyboard_locale.String(application.DIK_SUBTRACT),
	# application.DIK_ADD: keyboard_locale.String(application.DIK_MINUS),
	# application.DIK_MULTIPLY: keyboard_locale.String(application.DIK_MULTIPLY),
	# application.DIK_NUMPADCOMMA: keyboard_locale.String(application.DIK_NUMPADCOMMA),
	# application.DIK_NUMPADENTER: keyboard_locale.String(application.DIK_NUMPADENTER),
	
	# application.DIK_NUMPAD1: keyboard_locale.String(application.DIK_NUMPAD1),
	# application.DIK_NUMPAD2: keyboard_locale.String(application.DIK_NUMPAD2),
	# application.DIK_NUMPAD3: keyboard_locale.String(application.DIK_NUMPAD3),
	# application.DIK_NUMPAD4: keyboard_locale.String(application.DIK_NUMPAD4),
	# application.DIK_NUMPAD5: keyboard_locale.String(application.DIK_NUMPAD5),
	# application.DIK_NUMPAD6: keyboard_locale.String(application.DIK_NUMPAD6),
	# application.DIK_NUMPAD7: keyboard_locale.String(application.DIK_NUMPAD7),
	# application.DIK_NUMPAD8: keyboard_locale.String(application.DIK_NUMPAD8),
	# application.DIK_NUMPAD9: keyboard_locale.String(application.DIK_NUMPAD9),
	
	# Others (some keys maybe below to proper categories)
	# application.DIK_SPACE: keyboard_locale.String(application.DIK_SPACE),
	# application.DIK_GRAVE: keyboard_locale.String(application.DIK_GRAVE),
	# application.DIK_ESC: keyboard_locale.String(application.DIK_ESC),
	# application.DIK_TAB: keyboard_locale.String(application.DIK_TAB),
	# application.DIK_CAPITAL: keyboard_locale.String(application.DIK_CAPITAL),
	# application.DIK_WEBHOME: keyboard_locale.String(application.DIK_WEBHOME),
	# application.DIK_LWIN: keyboard_locale.String(application.DIK_LWIN),
	# application.DIK_RWIN: keyboard_locale.String(application.DIK_RWIN),
}
