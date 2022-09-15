## System Imports


# Embedder Imports
from junctions import window_manager


## Application Imports
from Interface.Frames.Metin2.Controls.types import Layer
from System.Interface.View.Control import Control


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property


@factory.register
class Bar3D(Control):
	"""
	The 3D Bar class that represents the Embedder's 'Bar3D' type.
	...
	"""
	
	Type = 'Bar3D'
	
	def __init__(self):
		super().__init__()
	
	def __del__(self):
		"""
		Destroys the 3D bar by calling the control destroyer
		of the embedder and passing the control handle signature

		:return:
		"""
		
		window_manager.Destroy(self.Handle)
	
	def Register(self, layer: Layer):
		"""
		Registers the control as a 'Bar3D' type in the embedder
		given the 3D bar's layer

		:param layer: The layer of the control
		:return: The embedder control handle signature
		"""
		
		return window_manager.RegisterBar3D(self, layer.value)
	
	@generic_property('color', required=False)
	def SetColor(self, color: tuple):
		"""
		Sets the 3d bar's color by giving a tuple of integers unpacked
		as argument representing RGB structure(Red Green Blue)

		:param color:
		"""
		window_manager.SetColor(self.Handle, *color)
