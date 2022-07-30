## System Imports
from typing import NoReturn


## Embedder Imports
from junctions import input_method


## Application Imports
from Interface.Frames.Metin2.Controls.Lines.text_line import TextLine


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property


@factory.register
class EditLine(TextLine):
	
	type = 'EditLine'
	
	def __init__(self):
		super().__init__()
		
		self.__character_maximum_limit: int = 0
	
	@generic_property('input_limit', editable=True, required=False)
	def SetInputMaximumLimit(self, maximum_limit: int) -> NoReturn:
		self.__character_maximum_limit = maximum_limit
		
		input_method.SetMax(maximum_limit)
		return input_method.SetUserMax(maximum_limit)
