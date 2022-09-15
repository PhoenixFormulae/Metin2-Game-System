# Standard Imports
from enum import Enum, unique
from contextlib import suppress
from typing import Union, NoReturn, List


# Embedder Imports
from junctions import window_manager


# Library Imports
from System.Interface.View.Control import Anchor
from System.Interface.View.Control import rendering
from Interface.Frames.Metin2.Controls.types import Layer
from Interface.Frames.Metin2.Controls.ImageBoxes.image_box import ImageBox


# External Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property


@unique
class RenderingRectangle(Enum):
	Left = 0
	Top = 1
	Right = 2
	Bottom = 3


@unique
class RenderingMode(Enum):
	"""
	Rendering color blending of a Expanded Image Box
	"""
	
	Normal = 0
	Screen = 1
	DodgeColor = 2
	Modulate = window_manager.RENDERING_MODE_MODULATE


@factory.register
class ExpandedImageBox(ImageBox):
	
	Type = 'expanded_image'
	
	def __init__(self):
		super().__init__()
		
		self.__image_width: int = 0
		self.__image_height: int = 0
		self.__width_scale: float = 1.0
		self.__height_scale: float = 1.0
	
	def __del__(self):
		super().__del__()
	
	def Register(self, layer: Layer) -> int:
		"""
		Registers the control as a 'Expanded Image Box' type in the embedder
		given the expanded image box's layer

		:param layer: The layer of the control
		:return: The embedder control handle signature
		"""
		
		return window_manager.RegisterExpandedImageBox(self, layer.value)
	
	@generic_property('image', editable=True, required=False)
	def SetImage(self, image_file_path: str):
		super().SetImage(image_file_path)
		self.SetScale(self.__width_scale, self.__height_scale)
	
	@generic_property([('x_scale', 'y_scale')], editable=True, required=False)
	def SetScale(self, width_scale: float, height_scale: float):
		"""
		Sets the scale multipliers of the control image
		to the specified values in the embedder.
		
		For example, the scale is default (1.0) and the
		image width is 100, if the X axis scale is set
		to 1.25, the render width will now be 125 but
		the real width will still be 100
		
		*Example not realistic but achieves wanted result*
		
		:param width_scale: X axis scale multiplier
		:param height_scale: Y axis scale multiplier
		"""
		
		self.__width_scale = width_scale
		self.__height_scale = height_scale
		
		window_manager.SetScale(self.Handle, width_scale, height_scale)
	
	def SetWidthScale(self, scale: float) -> NoReturn:
		"""
		Sets the width scale multiplier of the control
		
		:param scale: Width scale value
		"""
		
		self.SetScale(scale, self.height_scale)
	
	def SetHeightScale(self, scale: float):
		"""
		Sets the width scale multiplier of the control
		
		:param scale: Height scale value
		"""
		
		self.SetScale(self.width_scale, scale)
	
	@generic_property([('x_origin', 'y_origin')], editable=True, required=False)
	def SetOrigin(self, x: float, y: float):
		"""
		Sets the control origin
		TODO: Make an actual explanation
		
		:param x:
		:param y:
		:return:
		"""
		
		window_manager.SetOrigin(self.Handle, x, y)
	
	def SetRotation(self, rotation: int):
		"""
		Sets the image rotation of the control to the
		specified value in the embedder
		
		*Note:* The rotation value caps at -360 or +360,
		if the value exceeds negatively/positively these
		limits, the value is subtract and is set to 0,
		the remaining value is processed again by the
		previous calculation until its stable.
		
		For example, if the value is +400, the processed
		value will be +40 or if the value is -400, the
		processed value will be +40.
		
		:param rotation: Rotation value preferably between 0 and 360
		"""
		
		window_manager.SetRotation(self.Handle, rotation)
	
	@generic_property('mode', editable=True, required=False)
	def SetRenderingMode(self, mode: Union[str, RenderingMode]):
		"""
		Sets the rendering mode of the control's image to
		the specified value in the embedder
		
		:param mode: Rendering mode of the image
		"""
		
		if type(mode) == RenderingMode:
			mode_value = mode.value
		elif type(mode) == str:
			mode_value = RenderingMode[mode.capitalize()].value
		else:
			raise Exception("Unexpected rendering mode value type")
		
		window_manager.SetRenderingMode(self.Handle, mode_value)
	
	@generic_property('rect', editable=True, required=False)
	def SetRenderingRect(self, left: int, top: int, right: int, bottom: int):
		"""
		
		:param left:
		:param top:
		:param right:
		:param bottom:
		:return:
		"""
		
		window_manager.SetRenderingRect(self.Handle, left, top, right, bottom)
	
	def GetRenderingRect(self) -> List[float]:
		rendering_rect = window_manager.GetRenderingRect(self.Handle)
		
		with suppress(ZeroDivisionError):
			left = rendering_rect[0] / self.GetWidth()
			
		with suppress(ZeroDivisionError):
			top = rendering_rect[1] / self.GetHeight()
			
		with suppress(ZeroDivisionError):
			right = rendering_rect[2] / self.GetWidth()
			
		with suppress(ZeroDivisionError):
			bottom = rendering_rect[3] / self.GetHeight()
			
		normalized_rendering_rect: List[float] = [
			left,
			top,
			right,
			bottom
		]
		
		return normalized_rendering_rect
	
	def __Process(self):
		# FIXME: this refreshes the position according to the parent
		#        but maybe this shouldn't be here
		self.SetPosition(self.GetLocalXPosition(), self.GetLocalYPosition())
		
		self.__ProcessAnchoring()
		
		self.Validate()
	
	def __ProcessAnchoring(self):
		self.__ProcessAnchoringOnXAxis()
		self.__ProcessAnchoringOnYAxis()
	
	def __ProcessAnchoringOnXAxis(self):
		if not self.Parent:
			return
		
		if not self.force_initial_validation:
			if self.Parent.PreviousWidth == 0:
				return
		
		parent_width_difference = self.Parent.Width - self.Parent.PreviousWidth
		
		# Process X axis anchoring
		if Anchor.Left in self.anchors and Anchor.Right not in self.anchors:
			# new_local_x_pos = self.GetLocalXPosition() + parent_width_difference
			# self.SetPosition(new_local_x_pos, self.GetLocalXPosition())
			pass
			
		elif Anchor.Right in self.anchors and Anchor.Left not in self.anchors:
			x, y = self.GetLocalPosition()
			
			self.SetPosition(x + parent_width_difference, y)
		
		elif Anchor.Left in self.anchors and Anchor.Right in self.anchors:
			rendering_rect = self.GetRenderingRect()
			
			cur_rendering_width = self.GetWidth() * rendering_rect[2]
			if cur_rendering_width == 0:
				cur_rendering_width = self.GetWidth()
			
			new_rendering_rect_width = abs(cur_rendering_width + parent_width_difference)
			
			if rendering_rect[2] != 0:
				new_rendering_rect_left = rendering_rect[2] * (new_rendering_rect_width / cur_rendering_width)
			else:
				new_rendering_rect_left = new_rendering_rect_width / cur_rendering_width
			
			new_rendering_rect: List[4] = [
				0,
				0,
				new_rendering_rect_left,
				0
			]
			
			self.SetRenderingRect(new_rendering_rect[0], new_rendering_rect[1], new_rendering_rect[2], new_rendering_rect[3])
	
	def __ProcessAnchoringOnYAxis(self):
		if not self.Parent:
			return
		
		if not self.force_initial_validation:
			if self.Parent.PreviousHeight == 0:
				return
		
		parent_height_difference = self.Parent.Height - self.Parent.PreviousHeight
		
		# Process X axis anchoring
		if Anchor.Top in self.anchors and Anchor.Bottom not in self.anchors:
			# new_local_x_pos = self.GetLocalXPosition() + parent_width_difference
			# self.SetPosition(new_local_x_pos, self.GetLocalXPosition())
			pass
		
		elif Anchor.Bottom in self.anchors and Anchor.Top not in self.anchors:
			x, y = self.GetLocalPosition()
			
			self.SetPosition(x, y + parent_height_difference)
		
		elif Anchor.Top in self.anchors and Anchor.Bottom in self.anchors:
			rendering_rect = self.GetRenderingRect()
			
			cur_rendering_height = self.GetHeight() * (rendering_rect[1] + rendering_rect[3])
			if cur_rendering_height == 0:
				cur_rendering_height = self.GetHeight()
			
			new_rendering_rect_height = abs(cur_rendering_height + parent_height_difference)
			
			if rendering_rect[3] != 0:
				new_rendering_rect_bottom = rendering_rect[3] * (new_rendering_rect_height / cur_rendering_height)
			else:
				new_rendering_rect_bottom = new_rendering_rect_height / cur_rendering_height
			
			new_rendering_rect: List[4] = [
				0,
				0,
				0,
				new_rendering_rect_bottom
			]
			
			self.SetRenderingRect(new_rendering_rect[0], new_rendering_rect[1], new_rendering_rect[2], new_rendering_rect[3])
	
	def OnUpdate(self):
		super().OnUpdate()
	
	def OnUpdateRect(self):
		if not self.Validated():
			self.__Process()
	
	def OnRender(self):
		self.OnUpdateRect()
		
		rendering.HighlightControlGradient(self)
	
