## System Imports
from typing import NoReturn


## Embedder Imports
from junctions import window_manager


## Application Imports
from System.Interface.View.Control import Control
from Interface.Frames.Metin2.Controls.types import Layer


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property


@factory.register
class Line(Control):
	"""
	The Line class that represents the Embedder's Line type.
	"""
	
	Type = 'line'
	
	def __init__(self):
		super().__init__()
		
	def __del__(self):
		super().__del__()
	
	def Register(self, layer: Layer):
		"""
		Registers the control as a 'Line' type in the embedder
		given the line's layer
		
		:param layer: The layer of the control
		:return: The embedder control handle signature
		"""
		
		return window_manager.RegisterLine(self, layer.value)
	
	@generic_property('color', editable=True, required=False)
	def SetColor(self, color: tuple) -> NoReturn:
		"""
		Sets the line's color by giving
		
		:param color:
		"""
		
		return window_manager.SetColor(self.Handle, *color)
