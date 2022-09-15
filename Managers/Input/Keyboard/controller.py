# Standard Imports
from typing import Callable
from inspect import signature


# Library Imports
from Managers.Input.Keyboard.data import KeyState
from Managers.Input.Keyboard.metaclasses import KeyboardControllerMixin, KEY_ATTRIBUTE_LIST_NAME


# External Imports
from Core.Utils.zip import unpack_tuples_int


class KeyboardController(metaclass=KeyboardControllerMixin):
	
	def __init__(self):
		self.active_keys = {}
	
	def __Process(self, key: int, state: KeyState):
		self.active_keys[key] = state == KeyState.Press
		
		for key_function in getattr(self, KEY_ATTRIBUTE_LIST_NAME):
			valid = False
			
			press_keys = unpack_tuples_int(key_function.PressKeys)
			release_keys = unpack_tuples_int(key_function.ReleaseKeys)
			
			if key not in press_keys and key not in release_keys:
				continue
			
			pressed_keys = []
			released_keys = []
			
			for press_key in press_keys:
				if self.active_keys.get(press_key, False):
					pressed_keys.append(press_key)
			
			for release_key in release_keys:
				if not self.active_keys.get(release_key, True):
					released_keys.append(release_key)
			
			if key_function.State == KeyState.Both:
				valid = key in self.active_keys
			elif state == key_function.State:
				valid = self.active_keys.get(key, False)
			
			if valid:
				self.__CallKey(key_function, state, pressed_keys, released_keys)
	
	def __CallKey(self, key_function: Callable, state: KeyState, pressed_keys: list[int], released_keys: list[int]):
		key_function.PressedKeys = pressed_keys
		key_function.ReleasedKeys = released_keys
		
		if len(signature(key_function).parameters) > 1:
			key_function(self, state)
			return
		
		key_function(self)
	
	## Embedder Calls
	def OnKeyUp(self, key: int):
		self.__Process(key, KeyState.Release)
	
	def OnKeyDown(self, key: int):
		self.__Process(key, KeyState.Press)
	
