## System Imports
from typing import Optional


## Embedder Imports


## Application Imports
from System.Interface.View.Control import Control
from System.Interface.View.Control import rendering
from Interface.Frames.Metin2.Controls.Scrolls.scroll_bar import ScrollBar


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property
from Core.Interface.View.Control.interfaces import ControlInterface


@factory.register
class Panel(Control):
	
	Type = 'panel'
	
	def __init__(self):
		super().__init__()
		
		self.__scroll_control_name: Optional[str] = None
		self.__scroll_control: Optional[ScrollBar] = None
		
		self.__visibility_index: float = 1.0
	
	def __del__(self):
		super().__del__()
	
	@generic_property('scroll', editable=True, required=False)
	def SetScrollName(self, scroll_name):
		self.__scroll_control_name = scroll_name
	
	def AddChild(self, child: ControlInterface):
		super().AddChild(child)
		
		self.__ProcessScrollBarScrollSize()
	
	def GetChildrenMinimumXPosition(self) -> int:
		min_x: int = 0
		
		for child in self.children:
			x_pos = child.GetLocalXPosition()
			
			if x_pos < min_x:
				min_x = x_pos
		
		return min_x
	
	def GetChildrenMinimumYPosition(self) -> int:
		min_y: int = 0
		
		for child in self.children:
			y_pos = child.GetLocalXPosition()
			
			if y_pos < min_y:
				min_y = y_pos
		
		return min_y
	
	def GetChildrenMaximumXPosition(self) -> int:
		min_x: int = 0
		
		for child in self.children:
			x_pos = child.GetLocalXPosition()
			
			if x_pos > min_x:
				min_x = x_pos
		
		return min_x
	
	def GetChildrenMaximumYPosition(self) -> int:
		min_y: int = 0
		
		for child in self.children:
			y_pos = child.GetLocalXPosition()
			
			if y_pos > min_y:
				min_y = y_pos
		
		return min_y
	
	def __ProcessScrollBarScrollSize(self):
		if not self.__scroll_control:
			return
		
		total_height: int = self.GetChildrenMaximumYPosition() - self.GetChildrenMinimumYPosition()
		
		self.__scroll_control.SetScrollSize(self.GetHeight() / total_height)
		
	def __Process(self):
		self.__ProcessChildren()
	
	def __ProcessChildren(self):
		# self.__ProcessChildrenPositions()
		# self.__ProcessChildrenVisibility()
		pass
	
	def __ProcessChildrenPositions(self):
		if not self.__scroll_control:
			return
		
		scroll_previous_x, scroll_previous_y = self.__scroll_control.GetLocalPreviousPosition()
		
		x_difference: int = scroll_previous_x - self.__scroll_control.GetLocalXPosition()
		y_difference: int = scroll_previous_y - self.__scroll_control.GetLocalYPosition()
		
		for control in self.children:
			control.SetPosition(control.GetLocalXPosition() - x_difference, y_difference)
		
	def __ProcessChildrenVisibility(self):
		self_height = self.GetHeight()
		self_width = self.GetWidth()
		
		for control in self.children:
			if control == self.__scroll_control:
				continue
			
			control_x, control_y = control.GetLocalPosition()
			control_width, control_height = control.GetWidth(), control.GetHeight()
			
			if control_x + control_width < 0:
				control.Hide()
			elif control_x + control_width > self_width:
				control.Hide()
			elif control_y + control_height < 0:
				control.Hide()
			elif control_y + control_height > self_height:
				control.Hide()
			else:
				control.Show()
	
	def OnUpdate(self):
		super().OnUpdate()
	
	def OnUpdateRect(self):
		if not self.Validated():
			self.__Process()
		
		super().OnUpdateRect()
	
	def OnRender(self):
		super().OnRender()
		rendering.HighlightControlGradient(self, "white", "green")
	
	def OnViewLoad(self):
		if not self.__scroll_control_name:
			return
		
		scroll_control: Optional[ScrollBar] = self.Parent.FindChild(self.__scroll_control_name)
		
		if scroll_control:
			self.__scroll_control = scroll_control
		
		self.__ProcessScrollBarScrollSize()
	
	def OnViewLoaded(self):
		pass
