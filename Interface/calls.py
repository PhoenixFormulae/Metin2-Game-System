## System Imports

## Embedder Imports
from junctions import window_manager

## Application Imports
from Interface.Frames.Metin2.Controls.types import Layer

## Library Imports


class BaseCalls:
	
	def __init__(self):
		self.__handle = window_manager.Register(self, Layer.UIBottom.value)
		window_manager.Show(self.__handle)
