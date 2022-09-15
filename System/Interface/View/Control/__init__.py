# Standard Imports
from typing import NoReturn, Union, List, Optional


# Embedder Imports
from junctions import application
from junctions import window_manager


# Library Imports
from System.Interface.View.Control import rendering
from Interface.Frames.Metin2.Controls.types import Layer
from Interface.Events.General.timed_delay import TimedEvent, TimedEventArguments
from Interface.Events.Mouse.mouse_over import MouseOverEvent, MouseOverEventArguments
from System.Interface.View.Control.enums import Anchor, Flag, HorizontalAlignment, VerticalAlignment
from Interface.Events.Mouse.mouse_click import MouseClickEvent, MouseClickEventArguments, MouseButton


# External Imports
from Core.Interface.View.decorators import generic_property
from Core.Interface.View.Control.interfaces import ControlInterface
from Core.Interface.View.UserControl.interfaces import UserControlInterface
from Core.Interface.View.Event.interfaces import EventInterface, EventArgumentsInterface
from Core.Interface.View.Control.metaclasses import REQUIRED_ATTRIBUTE_LIST_NAME, OPTIONAL_ATTRIBUTE_LIST_NAME


class Control(ControlInterface):
	"""
	This is the base control were any controls should
	be based of.
	
	*Nomenclature Note*: The embedder names this as a 'Window' but since
	the controls act and work like a control, duck typing
	is preferred for clearer understanding.
	
	To create an automatically managed control, subclass
	from this class, to add automatic property registering
	use the Control Properties Decorators
	
	**Control Properties**
	Control Properties are attributes that can be set using
	*decorators* (check **decorators.py** for insight) that
	mark which class properties/attributes are for special
	treatment such as control loading and handling
	
	*Note*: Properties registry persists parent class property information
	however they can be overridden by hierarchic subclasses
	
	**Events**
	Events are actions that can be triggered when something happens
	inside/outside the control, check **Events Package** for insight.
	"""
	
	Type: str = "control"
	
	@property
	def Name(self) -> str:
		return self.GetName()
	
	@Name.setter
	def Name(self, value):
		self.SetName(value)
	
	@property
	def RequiredProperties(self) -> list[str]:
		return getattr(self, REQUIRED_ATTRIBUTE_LIST_NAME)
	
	@property
	def OptionalProperties(self) -> list[str]:
		return getattr(self, OPTIONAL_ATTRIBUTE_LIST_NAME)
	
	@property
	def Children(self) -> List[ControlInterface]:
		return self.__children
	
	@property
	def User_controls(self) -> List[UserControlInterface]:
		return self.__user_controls
	
	@property
	def Events(self) -> List[EventInterface]:
		return self.__events
	
	@property
	def Handle(self) -> int:
		return self.__control_handle
	
	@property
	def Parent(self) -> 'Control':
		return self.__parent_control
	
	@property
	def Width(self) -> int:
		return self.GetWidth()
	
	@property
	def Height(self) -> int:
		return self.GetHeight()
	
	@property
	def GlobalPosition(self) -> tuple[int, int]:
		return self.GetGlobalPosition()
	
	@property
	def PreviousWidth(self) -> int:
		return self.__previous_width
	
	@property
	def PreviousHeight(self) -> int:
		return self.__previous_height
	
	@property
	def MinimumWidth(self) -> int:
		return self.__minimum_width
	
	@property
	def MinimumHeight(self) -> int:
		return self.__minimum_height
	
	@property
	def anchors(self) -> List[Anchor]:
		return self.__anchors
	
	@property
	def force_initial_validation(self):
		return self.__force_initial_validation
	
	@property
	def skip_validation_parent_unloaded(self):
		return self.__skip_validation_parent_unloaded
	
	@property
	def loaded(self):
		return self.__loaded
	
	def __init__(self, control_handle: int = None):
		self.__control_handle: int = control_handle if control_handle is not None else self.Register(Layer.UI)
		
		self.__children: List[ControlInterface] = []
		
		self.__user_controls: List[UserControlInterface] = []
		
		self.__anchors: List[Anchor] = []
		
		self.__events: List[EventInterface] = []
		
		self.__parent_control: Control | None = None
		
		self.__previous_width: int = 0
		self.__previous_height: int = 0
		
		self.__minimum_width: int = 0
		self.__minimum_height: int = 0
		
		self.__maximum_width: Optional[int] = None
		self.__maximum_height: Optional[int] = None
		
		self.__validated: bool = False
		self.__force_initial_validation: bool = False
		self.__skip_validation_parent_unloaded: bool = False
		
		self.__loaded: bool = False
		
		self.Show()
	
	def __del__(self):
		"""
		Destroys the control by calling the control destructor
		of the embedder and passing the control handle signature
		"""
		
		window_manager.Destroy(self.Handle)
	
	def Register(self, layer: Layer) -> int:
		"""
		Registers the control as a 'window' type in the embedder
		given the control's layer

		:param layer: The layer of the control
		:return: The embedder control handle signature
		"""
		
		return window_manager.Register(self, layer.value)
	
	def Validate(self):
		self.__validated = True
		self.__InvalidateChildren()
	
	def Invalidate(self):
		self.__validated = False
	
	def Validated(self) -> bool:
		return self.__validated
	
	def AddChild(self, child: ControlInterface) -> bool:
		if child not in self.__children:
			self.__children.append(child)
			child.SetParent(self)
			return True
		
		return False
	
	def AddChildren(self, children: list[ControlInterface]) -> NoReturn:
		for child in children:
			self.AddChild(child)
	
	def FindChild(self, control_name: str, recursive: bool = True) -> Optional[ControlInterface]:
		for child_control in self.__children:
			if child_control.Name == control_name:
				return child_control
			
			if recursive:
				found_child: ControlInterface = child_control.FindChild(control_name)
				
				if found_child:
					return found_child
		
		return None
	
	def __InvalidateChildren(self):
		for control in self.Children:
			control.Invalidate()
	
	def AddUserControl(self, user_control: Union[UserControlInterface]):
		self.__user_controls.append(user_control)
	
	def AddUserControls(self, user_controls: List[UserControlInterface]):
		for user_control in user_controls:
			self.__user_controls.append(user_control)
	
	def Show(self) -> NoReturn:
		"""
		Shows the control by setting it as visible
		"""
		
		window_manager.Show(self.Handle)

	def Hide(self) -> NoReturn:
		"""
		Hides the control by setting it as invisible
		"""
		
		window_manager.Hide(self.Handle)
	
	def UpdateRect(self):
		window_manager.UpdateRect(self.Handle)
	
	def AddEvent(self, event: EventInterface):
		if event not in self.__events:
			self.__events.append(event)
	
	def FindEvent(self, event_name: str) -> Optional[EventInterface]:
		for event in self.__events:
			if event.Name == event_name:
				return event
		
		return None
	
	def TriggerEvent(self, event_type: type(EventInterface), arguments: Optional[EventArgumentsInterface] = None):
		for event in self.Events:
			if isinstance(event, EventInterface):
				if event.Type == event_type.Type:
					event.Trigger(arguments)
	
	# region ############### Embedder Getters, Setters and Others ################
	
	@generic_property('force_initial_validation', editable=True, required=False)
	def SetForceInitialValidation(self, force: bool):
		self.__force_initial_validation = force
		
	@generic_property('name', editable=True, required=True)
	def SetName(self, Name):
		"""
		Sets the control name with the specified given name
		in the embedder
		
		:param Name: Name of the control
		"""
		
		window_manager.SetName(self.Handle, Name)
	
	def GetName(self) -> str:
		"""
		Gets the control name set matching this control
		in the embedder
		
		:return: Name of the control
		"""
		
		return window_manager.GetName(self.Handle)
	
	def GetGlobalPosition(self) -> tuple[int, int]:
		"""
		Gets the global X and Y position of the control
		relative to the frame
		
		:return: Global X and Y control's position values
		"""
		
		return window_manager.GetWindowGlobalPosition(self.Handle)
	
	def GetGlobalXPosition(self) -> int:
		"""
		Gets the global X position of the control relative
		to its frame

		:return: Global X control's position value
		"""
		
		x, y = self.GetGlobalPosition()
		
		return x
	
	def GetGlobalYPosition(self) -> int:
		"""
		Gets the global Y position of the control relative
		to its frame

		:return: Global Y control's position value
		"""
		
		x, y = self.GetGlobalPosition()
		
		return y
	
	@generic_property([('x', 'y')], editable=True, required=False)
	def SetPosition(self, x: int, y: int):
		"""
		Sets the control position in the frame window

		Note: The position is the local position
		relative to the parent control

		:param x: X position
		:param y: Y position
		"""
		
		window_manager.SetWindowPosition(self.Handle, x, y)
		self.Invalidate()
	
	def GetLocalPosition(self) -> tuple[int, int]:
		"""
		Gets the local X and Y position of the control
		relative to the control parent
		
		:return: Local X and Y control's position values
		"""
		
		return window_manager.GetWindowLocalPosition(self.Handle)
	
	def GetLocalXPosition(self) -> int:
		"""
		Gets the local X position of the control relative
		to its parent
		
		:return: Local X control's position value
		"""
		
		x, y = self.GetLocalPosition()
		return x
	
	def GetLocalYPosition(self) -> int:
		"""
		Gets the local Y position of the control relative
		to its parent

		:return: Local Y control's position value
		"""
		
		x, y = self.GetLocalPosition()
		return y
	
	def GetLocalPreviousPosition(self) -> tuple[int, int]:
		return window_manager.GetWindowLocalPreviousPosition(self.Handle)
	
	def GetMouseLocalPosition(self):
		return window_manager.GetMouseLocalPosition(self.Handle)
	
	@generic_property([('minimum_width', "minimum_height")], editable=True, required=False)
	def SetMinimumSize(self, minimum_width: int, minimum_height: int):
		self.__minimum_width = minimum_width
		self.__minimum_height = minimum_height
	
	@generic_property([('width', 'height')], editable=True, required=False)
	def SetSize(self, width: int, height: int):
		"""
		Sets the control size by providing the width and height
		
		:param width: The width of the control
		:param height: The height of the control
		"""
		
		set_width = max(self.__minimum_width, width)
		set_height = max(self.__minimum_height, height)
		
		if self.__maximum_width:
			set_width = min(self.__maximum_width, width)
		
		if self.__maximum_height:
			set_height = min(self.__maximum_height, height)
		
		self.__previous_width = self.GetWidth()
		self.__previous_height = self.GetHeight()
		
		window_manager.SetWindowSize(self.Handle, set_width, set_height)
		
		self.Invalidate()
	
	def GetWidth(self):
		return window_manager.GetWindowWidth(self.Handle)
	
	def GetHeight(self):
		return window_manager.GetWindowHeight(self.Handle)
	
	def SetVisibility(self, visible: bool):
		"""
		Sets the visibility of the control
		
		:param visible: Whether its visible or not
		:return:
		"""
		
		self.Show() if visible else self.Hide()
	
	def IsVisible(self) -> int:
		"""
		Checks if the control is visible
		
		:return: Whether its visible or not
		"""
		
		return window_manager.IsShow(self.Handle)
	
	def AddStyleFlag(self, style_flag: Union[Flag, str]):
		"""
		Adds a style flag to this control
		
		Note: Removing flags is not supported by origin in
		the embedder.
		
		:param style_flag: Style flag to set/unset
		"""
		
		flag_value: str = ""
		
		if type(style_flag) == Flag:
			flag_value = style_flag.name.lower()
		elif type(style_flag) == str:
			for flag in Flag:
				if flag.name.lower() == style_flag.lower():
					flag_value = flag.name.lower()
					break
		else:
			raise Exception("Unexpected style flag")
		
		window_manager.AddFlag(self.Handle, flag_value)
	
	@generic_property('style', editable=True, required=False)
	def AddStyleFlags(self, style_flags: Union[list[Flag], tuple[str]]):
		"""
		Adds multiple style flags to the control
		
		Note: Removing flags is not supported by origin in
		the embedder.

		:param style_flags: The multiple style flags to add
		"""
		
		for flag in style_flags:
			self.AddStyleFlag(flag)
	
	@generic_property('horizontal_align', editable=True, required=False)
	def SetHorizontalAlign(self, alignment: HorizontalAlignment | str):
		"""
		Sets the horizontal alignment of the control

		:param alignment: A HorizontalAlign enumeration member or a string corresponding
		to the enumeration member key
		"""
		
		if type(alignment) == HorizontalAlignment:
			align_value = alignment.value
		elif type(alignment) == str:
			align_value = HorizontalAlignment[alignment.capitalize()].value
		else:
			raise Exception("Unexpected alignment value type")
		
		window_manager.SetWindowHorizontalAlign(self.Handle, align_value)
	
	@generic_property("vertical_align", editable=True, required=False)
	def SetVerticalAlign(self, alignment: VerticalAlignment | str):
		"""
		Sets the vertical alignment of the control

		:param alignment: A VerticalAlign enumeration member or a string corresponding
		to the enumeration member key
		"""
		
		if type(alignment) == VerticalAlignment:
			align_value = alignment.value
		elif type(alignment) == str:
			align_value = VerticalAlignment[alignment.capitalize()].value
		else:
			raise Exception("Unexpected alignment value type")
		
		window_manager.SetWindowVerticalAlign(self.Handle, align_value)
	
	def SetParent(self, parent: 'Control'):
		"""
		
		:param parent:
		"""
		
		window_manager.SetParent(self.Handle, parent.Handle)
		
		self.__parent_control = parent
		self.Invalidate()
	
	@generic_property('anchors', editable=True, required=False)
	def SetAnchors(self, anchors: List[str] | List[Anchor]):
		if isinstance(anchors, List):
			for anchor in anchors:
				if type(anchor) is str:
					for anch in Anchor:
						if anch.name.lower() == anchor.lower():
							if anch not in self.__anchors:
								self.__anchors.append(anch)
							else:
								self.__anchors.remove(anch)
			
		elif type(anchors) == List[Anchor]:
			self.__anchors = anchors
	
	def IsFocused(self) -> int:
		"""
		Checks if this control is focused

		:return: Control focus state
		"""
		
		return window_manager.IsFocus(self.Handle)
	
	def SetFocus(self):
		"""
		Sets the focus on this control
		"""
		
		window_manager.SetFocus(self.Handle)
	
	def IsIn(self) -> int:
		"""
		Checks mouse locations its withing the bounds of
		the control's rectangular area
		
		return: Whether the mouse is within the control's bounds
		"""
		
		return window_manager.IsIn(self.Handle)
	
	def IsRTL(self) -> int:
		"""
		Checks if the RTL (Right To Left) style flag is set
		"""
		
		return window_manager.IsRTL(self.Handle)
	
	# endregion
	
	# region ############### Processing Methods ###############
	
	def __Process(self):
		self.__ProcessAnchoring()
		
		# fixme: this refreshes the position according to the parent
		# but maybe this shouldn't be here
		self.SetPosition(self.GetLocalXPosition(), self.GetLocalYPosition())
		
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
		
		parent_width = self.Parent.Width
		
		parent_width_difference = parent_width - self.Parent.PreviousWidth
		
		# Process X axis anchoring
		if Anchor.Left in self.__anchors and Anchor.Right not in self.__anchors:
			# TODO: Create Left relation anchoring only, it should be checked if the
			# parent was resized from the left or the right by checking its local
			# position along with its width to determine the proper location
			pass
		
		elif Anchor.Right in self.__anchors and Anchor.Left not in self.__anchors:
			# TODO: Create Right relation anchoring only, same logic as above,
			# since the existing code does not care from where the parent was resized
			# although behaves correctly if parent is resized from the Right
			
			x, y = self.GetLocalPosition()
			
			self.SetPosition(x + parent_width_difference, y)
		
		elif Anchor.Left in self.anchors and Anchor.Right in self.anchors:
			# TODO: Create Right and Left relation anchoring, by taking in account
			# from which direction the parent was resized, the control should also
			# change size by the same amount and be repositioned if parent was resized
			# from the Left probably the same amount on X
			
			new_width = self.GetWidth() + parent_width_difference
			
			self.SetSize(new_width, self.GetHeight())
	
	def __ProcessAnchoringOnYAxis(self):
		if not self.Parent:
			return
		
		if not self.__force_initial_validation:
			if self.Parent.PreviousWidth == 0:
				return
		
		parent_height = self.Parent.Height
		
		parent_height_difference = parent_height - self.Parent.PreviousHeight
		
		if Anchor.Top in self.anchors and Anchor.Bottom not in self.anchors:
			# TODO: Create Left relation anchoring only, it should be checked if the
			# 		parent was resized from the left or the right by checking its local
			#		position along with its width to determine the proper location
			pass
		
		elif Anchor.Bottom in self.anchors and Anchor.Top not in self.anchors:
			# TODO: Create Right relation anchoring only, same logic as above,
			# 		since the existing code does not care from where the parent was resized
			# 		although behaves correctly if parent is resized from the Right
			
			x, y = self.GetLocalPosition()
			
			self.SetPosition(x, y + parent_height_difference)
		
		elif Anchor.Top in self.anchors and Anchor.Bottom in self.anchors:
			# TODO: Create Right and Left relation anchoring, by taking in account
			# 		from which direction the parent was resized, the control should also
			# 		change size by the same amount and be repositioned if parent was resized
			# 		from the Left probably the same amount on X
			
			new_height = self.GetHeight() + parent_height_difference
			
			self.SetSize(self.GetWidth(), new_height)
	
	# endregion
	
	# region ############### Embedder Calls ###############
	
	def OnUpdate(self):
		"""
		Triggered by the embedder when the control is updated by the loop cycle
		"""
		
		self.TriggerEvent(TimedEvent, TimedEventArguments(application.GetTime()))
	
	def OnUpdateRect(self):
		"""
		Triggered by the embedder when the control rect is updated by parent tree
		changing location, size or alignment
		"""
		
		# fixme: This function should be called by the embedder
		
		if not self.Validated():
			if self.Parent:
				if not self.Parent.loaded and self.skip_validation_parent_unloaded:
					self.__Process()
				elif self.Parent:
					self.__Process()
			else:
				self.__Process()
	
	def OnRender(self):
		"""
		Triggered by the embedder when the control was rendered by the embedder
		"""
		
		rendering.HighlightControlGradient(self)
		
		self.OnUpdateRect()
	
	def OnTop(self):
		pass
	
	def OnDrop(self):
		pass
	
	def OnSetFocus(self):
		"""
		Triggered by the embedder when the control gets focused
		"""
		
		pass
	
	def OnKillFocus(self):
		pass
	
	def OnMouseLeftButtonDown(self):
		"""
		This method gets triggered by the embedder when
		the mouse left button is pressed down
		"""
		
		# self.TriggerEvent(MouseClickEvent, MouseClickEventArguments(MouseButton.Left, False))
		
		# self.SetFocus()
	
	def OnMouseLeftButtonUp(self):
		"""
		This method gets triggered by the embedder when
		the mouse left button is let go up
		"""
		
		self.TriggerEvent(MouseClickEvent, MouseClickEventArguments(MouseButton.Left, True))
	
	def OnMouseWheel(self, length: int):
		"""
		Triggered by the embedder when the mouse wheel
		is rolled up or down.
		
		:param length: Amount rolled up/down (positive/negative)
		"""
		
		self.TriggerEvent(MouseClickEvent, MouseClickEventArguments(MouseButton.Wheel, length))
	
	def OnMouseOverIn(self):
		"""
		Triggered by the embedder when the mouse pointer
		overs in/points to this control
		"""
		
		self.TriggerEvent(MouseOverEvent, MouseOverEventArguments(False))
	
	def OnMouseOverOut(self):
		"""
		Triggered by the embedder when the mouse pointer
		overs out/leaves this control
		"""
		
		self.TriggerEvent(MouseOverEvent, MouseOverEventArguments(True))
	
	@staticmethod
	def OnMouseDrag(self):
		pass
	
	@staticmethod
	def OnMoveWindow(self, xy: tuple[2]):
		pass
	
	# endregion
	
	def OnControlLoaded(self):
		self.__loaded = True
	
	def OnViewLoaded(self):
		self.OnControlLoaded()
