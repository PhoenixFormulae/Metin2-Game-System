# Standard Imports

# Library Imports
from Managers.Input.Keyboard.data import KeyState
from Managers.Input.Keyboard.metaclasses import KEY_ATTRIBUTE_NAME

# External Imports


def Key(state: KeyState, press_key: int | tuple = (), release_key: int | tuple = ()):
	
	def decorator(function):
		setattr(function, KEY_ATTRIBUTE_NAME, True)
		
		function.State = state
		
		function.PressKeys = press_key
		function.ReleaseKeys = release_key
		
		return function
	
	return decorator

