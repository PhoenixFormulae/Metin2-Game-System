## System Imports
from typing import Optional, List


## Embedder Imports


## Application Imports
from System.Interface.View.Control import rendering
from Interface.Frames.Metin2.Controls.Containers.panel import Panel
from Interface.Frames.Metin2.Controls.List.list_item import ListItem
from Interface.Frames.Metin2.Controls.Scrolls.scroll_bar import ScrollBar


## Library Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property
from Core.Interface.View.Control.interfaces import ControlInterface
from Core.Interface.View.UserControl.interfaces import UserControlInterface


@factory.register
class List(Panel):
	
	Type = 'List'
	
	@property
	def list_items(self) -> List[ControlInterface]:
		list_items: List[ControlInterface] = []
		
		for control in self.children:
			if isinstance(type(control), ListItem.__class__):
				list_items.append(control)
		
		return list_items
	
	def __init__(self):
		super().__init__()
		
		self.__selected_child: Optional[ControlInterface] = None
		
		self.__base_position: int = 0
		
		self.__item_spacing_width: int = 0
		self.__item_spacing_height: int = 0
		
		self.__scroll_control_name: str = ""
		self.__scroll_control: Optional[ScrollBar] = None
		
		self.__list_item_user_control_name: str = ""
		self.__list_item_user_control: Optional[UserControlInterface] = None
	
	@generic_property([('width', 'height')], editable=True, required=False)
	def SetSize(self, width: int, height: int):
		super().SetSize(width, height)
		
		for control in self.children:
			control.SetSize(width, control.GetHeight())
	
	@generic_property([('item_spacing_width', 'item_spacing_height')], editable=True, required=False)
	def SetItemSpacing(self, spacing_width: int, spacing_height: int):
		self.__item_spacing_width = spacing_width
		self.__item_spacing_height = spacing_height
	
	@generic_property('item', editable=True, required=False)
	def SetItemName(self, item_name: str):
		self.__list_item_user_control_name = item_name
	
	@generic_property('scroll', editable=True, required=False)
	def SetScrollName(self, scroll_control_name: str):
		self.__scroll_control_name = scroll_control_name
	
	# endregion
	
	# region ################ List Items Methods ################
	
	def GetListItem(self) -> Optional[UserControlInterface]:
		return self.__list_item_user_control
	
	def SetListItem(self, list_item_user_control: UserControlInterface):
		if not isinstance(list_item_user_control, UserControlInterface):
			print(f"Given List Item '{list_item_user_control.__class__.__name__}' is not of User Control type.")
			return
		
		self.__list_item_user_control = list_item_user_control
	
	def AddItem(self, list_item: ListItem):
		self.AddChild(list_item)
		
		if self.__scroll_control:
			self.__scroll_control.SetScrollSize(self.__TotalHeight() / self.__AverageListItemSize())
		
		self.Invalidate()
	
	def RemoveItem(self, list_item: ListItem):
		pass
	
	def ClearItems(self):
		for control in self.children:
			if isinstance(type(control), ListItem.__class__):
				self.children.remove(control)
				control.__del__()
	
	def __TotalHeight(self) -> int:
		height: int = 0
		
		for child in self.children:
			height += child.GetHeight()
			height += self.__item_spacing_height
		
		return height
	
	def __AverageListItemSize(self) -> float:
		total_height: int = 0
		idx: int = 0
		
		for list_item in self.list_items:
			total_height += list_item.Height + self.__item_spacing_height
			
			idx += 1
		
		return total_height / idx
	
	def SetScroll(self, scroll_control: ControlInterface):
		self.__scroll_control = scroll_control
	
	"""
	def AddUserControl(self, user_control: Union[UserControlInterface, List[UserControlInterface]]):
		if user_control.model.control_properties["name"] == self.__list_item_user_control:
			self.SetListItem(user_control)
			super().AddUserControl(user_control)
	
	def AddUserControls(self, user_controls: List[UserControlInterface]):
		for user_control in user_controls:
			if user_control.control_properties["name"] == self.__list_item_user_control_name:
				self.SetListItem(user_control)
				super().AddUserControl(user_control)
	"""
	
	def __Process(self):
		# self.__ProcessScrolling()
		# self.__ProcessChildren()
		pass
		
	def __ProcessChildren(self):
		self.__ProcessChildrenPositions()
	
	def __ProcessChildrenPositions(self):
		height = self.GetHeight() - (2 * self.__item_spacing_height)
		
		if self.__TotalHeight() < height:
			return
		
		cur_x_pos: int = 0
		for child in self.children:
			child_height = child.GetHeight()
			
			child.SetPosition(0, cur_x_pos + self.__base_position)
			cur_x_pos += child_height + self.__item_spacing_height
	
	def __ProcessScrolling(self):
		if not self.__scroll_control:
			return
		
		scroll_pos = self.__scroll_control.GetScrollPosition()
		to_show = self.__TotalHeight() - self.GetHeight() + (2 * self.__item_spacing_height)
		self.base_position = to_show * scroll_pos
		
		self.Invalidate()
	
	def OnUpdate(self):
		super().OnUpdate()
	
	def OnUpdateRect(self):
		if not self.Validated():
			self.__Process()
		
		super().OnUpdateRect()
	
	def OnRender(self):
		super().OnRender()
		rendering.HighlightControlGradient(self, 'marzipan', 'blue')
	
	def OnViewLoad(self):
		if not self.__scroll_control_name:
			return
		
		scroll_control: Optional[ScrollBar] = self.parent_control.FindChild(self.__scroll_control_name)
		
		if scroll_control:
			self.__scroll_control = scroll_control
