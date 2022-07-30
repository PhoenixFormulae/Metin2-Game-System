## System Imports


## Embedder Imports
from junctions import application


## Application Imports
from System.Interface.View.Control import Control


## Library Imports
from Core.Plugins import factory


@factory.register
class ListItem(Control):
	
	Type = 'List_Item'
	
	def __init__(self):
		super().__init__()
		
		self.__highlight_color: str = "dark_cyan"
	
	def __ProcessChildren(self):
		for child in self.children:
			local_x, local_y = child.GetLocalPosition()
			global_x, global_y = child.GetGlobalPosition()
			width, height = child.GetSize()
			
			if local_y + height < self.__minimum_height or local_y > self.__maximum_height:
				child.Hide()
			else:
				pass
	
	## Embedder Calls
	def OnUpdate(self):
		super().OnUpdate()
	
	def OnUpdateRect(self):
		super().OnUpdateRect()
	
	def OnRender(self):
		super().OnRender()
	
	def OnMouseLeftButtonDown(self):
		self.GetParent().Select(self)
	
	def OnMouseOverIn(self):
		application.SetCursor(application.PICK)
		self.__highlight_color = 'makara'
		super().OnMouseOverIn()
	
	def OnMouseOverOut(self):
		application.SetCursor(application.NORMAL)
		self.__highlight_color = 'dark_cyan'
		super().OnMouseOverIn()

