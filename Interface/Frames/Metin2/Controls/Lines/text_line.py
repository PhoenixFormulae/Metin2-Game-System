## System Imports
from enum import Enum
from typing import NoReturn, Union


# Embedder Imports
from junctions import window_manager


## Application Imports
from Interface.Frames.Metin2.Controls.types import Layer
from System.Interface.View.Control import Control


## Library Imports
from colour import Color

from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property


class TextHorizontalAlign(Enum):
	
	Left = window_manager.TEXT_HORIZONTAL_ALIGN_LEFT
	Center = window_manager.TEXT_HORIZONTAL_ALIGN_CENTER
	Right = window_manager.TEXT_HORIZONTAL_ALIGN_RIGHT
	

class TextVerticalAlign(Enum):
	
	Top = window_manager.TEXT_VERTICAL_ALIGN_TOP
	Center = window_manager.TEXT_VERTICAL_ALIGN_CENTER
	Bottom = window_manager.TEXT_VERTICAL_ALIGN_BOTTOM


@factory.register
class TextLine(Control):
	
	Type = 'Text'
	
	def __init__(self, ):
		super().__init__()
		
		self.__limit_width: int = 0
		self.__multiline: bool = False
		
		self.SetFontName('Tahoma:16')
		
	def Register(self, layer: Layer):
		"""
		Registers the control as a 'text line' type in the embedder
		given the text line's layer

		:param layer: The layer of the control
		:return: The embedder control handle signature
		"""
		
		return window_manager.RegisterTextLine(self, layer.value)
	
	def GetText(self) -> str:
		"""
		Gets the current control's text string
		
		:return: Control's text string
		"""
		
		return window_manager.GetText(self.Handle)
	
	@generic_property('text', editable=True, required=False)
	def SetText(self, text: str) -> NoReturn:
		"""
		Sets the text line's text by setting
		the specified value in the embedder

		:param text: Text to set
		"""
		
		return window_manager.SetText(self.Handle, text)
	
	def GetTextSize(self) -> tuple[int, int]:
		"""
		Gets the text line's current text's width
		and height
		
		:return: Text's width and height
		"""
		
		return window_manager.GetTextSize(self.Handle)
	
	def GetTextWidth(self) -> int:
		"""
		Gets the text line's current text width
		
		:return: Current text width
		"""
		
		return self.GetTextSize()[0]
	
	def GetTextHeight(self) -> int:
		"""
		Gets the text line's current text height
		
		:return: Current text height
		"""
		
		return self.GetTextSize()[1]
	
	def GetLimitWidth(self) -> int:
		"""
		Gets the limit width from the control's
		local context
		
		:return: Local limit width
		"""
		
		return self.__limit_width
	
	def SetLimitWidth(self, limit: int):
		"""
		Sets the limit width of the control by setting
		the specified value in the embedder
		
		:param limit: The limit width
		"""
		
		self.__limit_width = limit
		
		window_manager.SetLimitWidth(self.Handle, limit)
	
	@generic_property('fontname', required=False)
	def SetFontName(self, font_name: str):
		"""
		Sets the text line's font to the specified
		font and size by providing the font name
		
		:param font_name: Font and font size to set
		"""
		
		window_manager.SetFontName(self.Handle, font_name)
		self.SetText(self.GetText())
	
	@generic_property('multiline', required=False)
	def SetMultiLine(self, wrap: bool):
		"""
		Sets if the text line's text can be wrapped underneath
		the initial text line if the is enough height space
		for it to happen
		
		:param wrap: Enables/Disables the multiline wrap
		"""
		
		self.__multiline = wrap
		
		window_manager.SetMultiLine(self.Handle, wrap)
	
	def IsMultiLine(self) -> bool:
		"""
		Gets if the control's text is multiline, meaning
		if the text is wrapped underneath the first line
		if more than one line exists
		
		:return: Whether the text line is multiline or not
		"""
		
		return self.__multiline
	
	@generic_property('secret_flag', required=False)
	def SetSecret(self, hide: bool = True) -> NoReturn:
		"""
		Sets if the control's text should be replaced
		with an asterisk for the purpose of hiding the
		real text from being visible, used normally
		for hiding sensitive text like credentials
		
		:param hide: Whether the text should be hidden
		"""
		
		return window_manager.SetSecret(self.Handle, hide)
	
	@generic_property('outline', required=False)
	def SetOutline(self, outline: bool = True) -> NoReturn:
		"""
		Sets the text line's characters with an outline,
		a black 1 pixel wide cover around each character
		
		:param outline: Whether the text is outlined
		"""
		
		return window_manager.SetOutline(self.Handle, outline)
	
	@generic_property('feather', required=False)
	def SetFeather(self, feather: int = 1) -> NoReturn:
		"""
		Sets the text line's character with a feather effect,
		however seems to not work
		
		:param feather: Whether the text if feathered
		"""
		
		return window_manager.SetFeather(self.Handle, feather)
	
	@generic_property('color_name', required=False)
	def SetTextColorByName(self, color_name: str) -> NoReturn:
		"""
		Sets the text line's current text color by getting the
		current color hexadecimal name representation from
		color information name getter
		
		:param color_name: Color name to set to the text
		"""
		
		return self.SetPackedFontColor(Color(color_name).hex)
	
	@generic_property('text_horizontal_align', required=False)
	def SetTextHorizontalAlign(self, vertical_align: Union[TextHorizontalAlign, str]):
		
		if type(vertical_align) == TextHorizontalAlign:
			align_value = vertical_align
		elif type(vertical_align) == str:
			align_value = TextHorizontalAlign[vertical_align.capitalize()]
		else:
			raise Exception("Unexpected alignment value type")
		
		window_manager.SetHorizontalAlign(self.Handle, align_value.value)
	
	@generic_property('text_vertical_align', required=False)
	def SetTextVerticalAlign(self, vertical_align: Union[TextVerticalAlign, str]):
		
		if type(vertical_align) == TextVerticalAlign:
			align_value = vertical_align
		elif type(vertical_align) == str:
			align_value = TextVerticalAlign[vertical_align.capitalize()]
		else:
			raise Exception("Unexpected alignment value type")
		
		window_manager.SetVerticalAlign(self.Handle, align_value.value)
	
	def __Process(self):
		self.__ProcessSize()
	
	def __ProcessSize(self):
		text_width, text_height = self.GetTextSize()[0]
		
		control_width, control_height = self.GetWidth(), self.GetWidth()
		
		if text_width != control_width or text_height != control_height:
			self.SetSize(text_width, text_height)
	
	def OnUpdateRect(self):
		if not self.Validated():
			self.__Process()
		
		super().OnUpdateRect()
	
	def OnRender(self):
		super().OnRender()
	
