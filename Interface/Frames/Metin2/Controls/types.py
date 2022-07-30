## System Imports


## Application Imports


## Library Imports
from enum import Enum, unique


@unique
class Layer(Enum):
	"""
	Controls act in different layers according to the embedder,
	the order of the layers match this enumerator's items order
	"""
	
	UI = "UI"
	Game = "GAME"
	UIBottom = "UI_BOTTOM"
	TopMost = "TOP_MOST"
	Curtain = "CURTAIN"

