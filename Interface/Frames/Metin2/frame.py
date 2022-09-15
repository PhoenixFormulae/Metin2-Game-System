# Standard Imports
from enum import unique, Enum


# Embedder Imports


# Library Imports
from Interface import Events
from Interface.Frames.Metin2 import Controls
from System.Interface.View.Control import Control
from Interface.Frames.Metin2.Sets.Metin2 import UserControls
from Settings.Interface.data import Metin2WindowConfiguration


# External Imports
from Core.Interface.Frame.base import BaseFrame
from Core.Interface.data import BaseWindowConfiguration
from Core.Interface.View.Event.container import EventContainer
from Core.Interface.Set.interfaces import InterfaceSetInterface
from Core.Interface.Frame.interfaces import FrameWindowInterface
from Core.Interface.View.Control.container import ControlContainer
from Core.Interface.View.Control.interfaces import ControlInterface
from Core.Interface.View.UserControl.container import UserControlContainer


class Metin2InterfaceFrame(BaseFrame):
	"""
	Creates a Metin2 Interface frame, handles looping
	and holds its respective compatible Model-View-Presenter
	data model instances.
	
	**Note:** The default embedder only allows the creation
	of one static window, attempts to create more windows
	will result in substitution of the active window and
	probably causes critical internal errors
	
	**Control Notes: Creating a control without initializing
	the frame before will probably result in an exception
	thrown by the embedder**
	
	**Main Loop Note:** Threading for this interface is not
	supported so this has to be the only existent non-concurrent
	frame in the list of active frames
	"""
	
	Type: str = 'Metin2'
	SingleWindow: bool = True
	
	@classmethod
	@property
	def AssetsDirectory(self) -> str:
		return 'Data/Interface/Frames/Metin2/'
	
	InterfaceSets: list[InterfaceSetInterface] = []
	
	WindowConfiguration: BaseWindowConfiguration = Metin2WindowConfiguration
	Window: FrameWindowInterface | None = None
	
	BaseControlType: ControlInterface = Control
	ControlTypes: ControlContainer = ControlContainer(Controls.__path__)
	ControlTypes += BaseControlType
	
	UserControlTypes: UserControlContainer = UserControlContainer(UserControls.__path__)
	EventTypes: EventContainer = EventContainer(Events.__path__)
	
	@classmethod
	def Initialize(cls):
		from Interface.Frames.Metin2.window import Metin2InterfaceFrameWindow
		cls.Window = Metin2InterfaceFrameWindow(cls.WindowConfiguration)
		super().Initialize()
	
	@classmethod
	def Loop(cls):
		cls.Window.Loop()
	

@unique
class CreationError(Enum):
	CREATE_DEVICE = 0

