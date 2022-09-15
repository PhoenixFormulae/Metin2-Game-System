# Standard Imports


# Embedder Imports
from junctions import window_manager


# Library Imports
from System.Interface.View.Control import Control
from Interface.Frames.Metin2.Controls.types import Layer


# External Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property


@factory.register
class Box(Control):
	"""
	The Box class that represents the Embedder's 'Box' type
	"""
	
	Type = 'box'
	
	def __init__(self):
		super().__init__()
	
	def __del__(self):
		"""
		Destroys the box by calling the control destroyer
		of the embedder and passing the control handle signature

		:return:
		"""
		
		window_manager.Destroy(self.Handle)
	
	def Register(self, layer: Layer):
		"""
		Registers the control as a 'Box' type in the embedder
		given the box's layer

		:param layer: The layer of the control
		:return: The embedder control handle signature
		"""
		
		return window_manager.RegisterBox(self, layer.value)
	
	@generic_property('color', editable=True, required=False)
	def SetColor(self, color: tuple):
		"""
		Sets the box's color by giving a tuple of integers unpacked
		as argument representing RGB structure(Red Green Blue)

		:param color:
		"""
		window_manager.SetColor(self.Handle, *color)
