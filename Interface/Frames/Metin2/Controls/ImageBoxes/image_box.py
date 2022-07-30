## System Imports


## Embedder Imports
from junctions import group_image
from junctions import window_manager


## Application Imports
from System.Interface.View.Control import Control
from Interface.Frames.Metin2.Controls.types import Layer


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property


@factory.register
class ImageBox(Control):
	
	Type = 'image'
	
	def __init__(self):
		self.__image_file_path: str = ''
		self.__image_pointer: int = 0
		
		super().__init__()
	
	def Register(self, layer: Layer) -> int:
		"""
		Registers the control as a 'Image Box' type in the embedder
		given the image box's layer

		:param layer: The layer of the control
		:return: The embedder control handle signature
		"""
		
		return window_manager.RegisterImageBox(self, layer.value)
	
	@generic_property('image', editable=True, required=False)
	def SetImage(self, image_file_path: str):
		"""
		Sets the image of the control by loading
		the specified image in the embedder
		
		*Note:* The resolution of the location of the
		image and path related operations are made in
		the embedder
		
		**Exception Note:** If the image is not found
		or cannot be loaded, an exception is thrown
		
		:param image_file_path: Image file path to load
		"""
		
		self.__image_file_path = image_file_path
		
		try:
			self.__image_pointer = window_manager.LoadImage(self.Handle, image_file_path)
		except FileNotFoundError:
			...
		except FileExistsError:
			...
	
	def GetImagePath(self) -> str:
		return self.__image_file_path
	
	def SetTransparency(self, transparency: float):
		"""
		Sets the alpha transparency of the control image
		to the specified value in the embedder
		
		:param transparency: Alpha value to set
		"""
		
		window_manager.SetDiffuseColor(self.color_handle, 1.0, 1.0, 1.0, transparency)
	
	def GetWidth(self) -> int:
		if not self.__image_pointer:
			return -1
		
		try:
			return group_image.GetWidth(self.__image_pointer)
		except RuntimeError:
			return -1
	
	def GetHeight(self) -> int:
		if not self.__image_pointer:
			return -1
		
		try:
			return group_image.GetHeight(self.__image_pointer)
		except RuntimeError:
			return -1
	
	## Embedder Calls
	def OnUpdate(self):
		super().OnUpdate()
	
	def OnUpdateRect(self):
		super().OnUpdateRect()
	
	def OnRender(self):
		super().OnRender()
	
