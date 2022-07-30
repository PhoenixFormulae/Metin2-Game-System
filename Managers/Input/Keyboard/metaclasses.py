## System Imports
from abc import ABCMeta

## Application Imports

## Library Imports

# Keyboard Attribute Names
KEY_ATTRIBUTE_NAME = '_key'
KEY_ATTRIBUTE_LIST_NAME = 'key_functions'


class KeyboardControllerMeta(type):
	@classmethod
	def __prepare__(mcs, name: str, bases: tuple):
		return super(KeyboardControllerMeta, mcs).__prepare__(name, bases)
	
	def __new__(mcs, name: str, bases: tuple, dct: dict):
		if len(bases) > 0:
			mcs.__determine_keys(dct, bases)
		
		return super(KeyboardControllerMeta, mcs).__new__(mcs, name, bases, dct)
	
	@staticmethod
	def __determine_keys(dct: dict, bases: tuple):
		if KEY_ATTRIBUTE_LIST_NAME not in dct:
			dct[KEY_ATTRIBUTE_LIST_NAME] = []
		
		for base in bases:
			if hasattr(base, KEY_ATTRIBUTE_LIST_NAME):
				base_functions = getattr(base, KEY_ATTRIBUTE_LIST_NAME)
				for attr, val in base_functions.items():
					dct[KEY_ATTRIBUTE_LIST_NAME][val.property_types_list[0]] = val
		
		for attr, val in dct.items():
			if hasattr(val, KEY_ATTRIBUTE_NAME):
				dct[KEY_ATTRIBUTE_LIST_NAME].append(val)
	

KeyboardControllerMixin = type('KeyboardControllerMixin', (ABCMeta, KeyboardControllerMeta), {})
