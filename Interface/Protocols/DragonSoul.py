# Standard Imports
from typing import Protocol

# Embedder Imports

# Library Imports

# External Imports


class DragonSoulModelProtocol(Protocol):
	...


class DragonSoulPresenterProtocol(Protocol):
	...


class DragonSoulViewProtocol(Protocol):
	
	def ActivateExternal(self, deck: int):
		...
	
	def Deactivate(self):
		...
	
	def HighlightSlot(self, position: int):
		...
	
	def Qualify(self):
		...
	
