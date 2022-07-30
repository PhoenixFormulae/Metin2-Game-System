## System Imports
from typing import Union, List

## Embedder Imports
from junctions import group
from junctions import window_manager

## Application Imports
from System.Interface.View.Control import Control
from Interface.Frames.Metin2.Controls.types import Layer

## Library Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property

from colour import Color


@factory.register
class Bar(Control):
	"""
	The Bar class that represents the Embedder's bar type.
	...
	"""
	
	Type = 'Bar'
	
	def __init__(self):
		super().__init__()
	
	def __del__(self):
		window_manager.Destroy(self.Handle)
	
	def Register(self, layer: Layer):
		"""
		Registers the control as a 'Bar' type in the embedder
		given the bar's layer

		:param layer: The layer of the control
		:return: The embedder control handle signature
		"""
		
		return window_manager.RegisterBar(self, layer.value)
	
	@generic_property('color', editable=True, required=False)
	def SetColor(self, color: Union[List, int, str]):
		"""
		Sets the bar's color by giving a tuple of integers unpacked
		as argument representing RGB structure(Red Green Blue)

		:param color:
		"""
		
		if isinstance(color, List):
			window_manager.SetColor(self.Handle, group.GenerateColor(color[0], color[1], color[2], color[3]))
		elif type(color) == int:
			window_manager.SetColor(self.Handle, color)
		elif isinstance(color, str):
			window_manager.SetColor(self.Handle, Color(color).hex)
	
	## Embedder Calls
	def OnUpdate(self):
		super().OnUpdate()
	
	def OnUpdateRect(self):
		super().OnUpdateRect()
	
	def OnRender(self):
		super().OnRender()
	