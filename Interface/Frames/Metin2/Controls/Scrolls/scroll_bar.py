## System Imports
from typing import Optional, List


# Embedder Imports


## Application Imports
from System.Interface.View.Control import Control, rendering
from Interface.Frames.Metin2.Controls.Buttons.drag_button import DragButton


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property


@factory.register
class ScrollBar(Control):
	
	Type = 'Scroll_Bar'
	
	def __init__(self):
		super().__init__()
		
		self.__size_percentage: float = 100
		self.__current_percentage: float = 0
		
		self.__scroll_control: Optional[DragButton] = None
		self.__scroll_control_name: Optional[str] = None
		
		self.__restrictions_horizontal: List[int, int] = [0, 0]
		self.__restrictions_vertical: List[int, int] = [0, 0]
		
		self.__enabled: bool = True
	
	def __del__(self):
		super().__del__()
	
	@generic_property([('width', 'height')], editable=True, required=False)
	def SetSize(self, width: int, height: int):
		super().SetSize(width, height)
		self.SetScrollSize(self.__size_percentage)
	
	@generic_property('scroll', editable=True, required=False)
	def SetScrollName(self, scroll_name: str):
		self.__scroll_control_name = scroll_name
	
	@generic_property('restrict_horizontal', editable=True, required=False)
	def SetRestrictionsHorizontal(self, restrictions: [int, int]):
		self.__restrictions_horizontal = restrictions
	
	@generic_property('restrict_vertical', editable=True, required=False)
	def SetRestrictionsVertical(self, restrictions: [int, int]):
		self.__restrictions_vertical = restrictions
	
	def SetScrollSize(self, size: float):
		self.__size_percentage = max(0.0, min(size, 100.0))
		
		if not self.__scroll_control:
			return
		
		self.__ProcessMovementRestriction()
		
		new_height = self.GetHeight() / self.__size_percentage
		self.__scroll_control.SetSize(self.__scroll_control.GetWidth(), new_height)
	
	def GetScrollPosition(self) -> float:
		return self.__current_percentage
	
	def __ProcessMovementRestriction(self):
		self.__ProcessVerticalMovementRestriction()
	
	def __ProcessHorizontalMovementRestriction(self):
		if not self.__scroll_control:
			return
		
		restrict_area = (
			self.__restrictions_horizontal[0],
			self.__restrictions_vertical[0],
			self.__scroll_control.GetWidth(),
			self.GetHeight() - self.__restrictions_vertical[1],
		)
		
		self.__scroll_control.SetRestrictMovementArea(*restrict_area)
		self.__scroll_control.SetPosition(self.__scroll_control.GetLocalXPosition(), self.__restrictions_vertical[0])
	
	def __ProcessVerticalMovementRestriction(self):
		if not self.__scroll_control:
			return
		
		restrict_area = (
			0,
			self.__restrictions_vertical[0],
			self.GetWidth(),
			self.GetHeight() - self.__restrictions_vertical[1],
		)
		
		self.__scroll_control.SetRestrictMovementArea(*restrict_area)
	
	def __Process(self):
		self.__ProcessScrolling()
	
	def __ProcessScrolling(self):
		if not self.__scroll_control:
			return
	
	def OnUpdate(self):
		super().OnUpdate()
	
	def OnUpdateRect(self):
		if not self.Validated():
			self.__Process()
		
		super().OnUpdateRect()
	
	def OnRender(self):
		super().OnRender()
		
		rendering.HighlightControlGradient(self)
		
		# if self.__scroll_control:
		# 	self.__HighlightMovementArea()
	
	def OnMove(self):
		pass
	
	def OnViewLoad(self):
		if not self.__scroll_control_name:
			return
		
		scroll_control: Optional[DragButton] = self.FindChild(self.__scroll_control_name)
		
		if not scroll_control:
			return
		
		self.__scroll_control = scroll_control
	
	def OnViewLoaded(self):
		if not self.__scroll_control:
			return
		
		self.SetScrollSize(self.__size_percentage)
	
	def __HighlightMovementArea(self):
		x, y = self.GetGlobalPosition()
		restrict_area = self.__scroll_control.restrict_area
		
		rendering.HighlightAreaGradient(x + restrict_area[0], y + restrict_area[1],
		                                         restrict_area[2], restrict_area[3],
		                                         3, "green", "blue")

