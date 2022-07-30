## System Imports


## Embedder Imports
from junctions import window_manager


## Application Imports
from System.Interface.View.Control import Control
from Interface.Frames.Metin2.Controls.types import Layer


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property


@factory.register
class Button(Control):
	"""
	The Button class that represents the Embedder's 'Button' type.
	"""
	
	Type = 'button'
	
	def __init__(self):
		super().__init__()
		
		window_manager.SetPickAlways(self.Handle)
	
	def Register(self, layer: Layer):
		"""
		Registers the control as a 'Button' type in the embedder
		given the button's layer

		:param layer: The layer of the control
		:return: The embedder control handle signature
		"""
		
		return window_manager.RegisterButton(self, layer.value)
	
	@generic_property('default_image', editable=True, required=False)
	def SetUpVisual(self, filename: str):
		window_manager.SetUpVisual(self.Handle, filename)
	
	@generic_property('over_image', editable=True, required=False)
	def SetOverVisual(self, filename):
		window_manager.SetOverVisual(self.Handle, filename)
	
	@generic_property('down_image', editable=True, required=False)
	def SetDownVisual(self, filename):
		window_manager.SetDownVisual(self.Handle, filename)
	
	@generic_property('disable_image', editable=True, required=False)
	def SetDisableVisual(self, filename):
		window_manager.SetDisableVisual(self.Handle, filename)
	
	def Enable(self):
		window_manager.Enable(self.Handle)

	def Disable(self):
		window_manager.Disable(self.Handle)
	
	def Flash(self):
		window_manager.Flash(self.Handle)
	
	def OnUpdate(self):
		super().OnUpdate()
	
	def OnUpdateRect(self):
		super().OnUpdateRect()
	
	def OnRender(self):
		super().OnRender()
	
	def OnMouseOverIn(self):
		super().OnMouseOverIn()
	
	def OnMouseOverOut(self):
		super().OnMouseOverOut()
	
	def ShowToolTip(self):
		pass
	
	def HideToolTip(self):
		pass

	def DownEvent(self):
		super().OnMouseLeftButtonDown()
	
	def CallEvent(self):
		super().OnMouseLeftButtonUp()
