## System Imports


## Application Imports
from Interface.Frames.Metin2.frame import Metin2InterfaceFrame


## Library Imports
from Core.Interface.Set.base import BaseInterfaceSet
from Core.Interface.Set.decorators import register_interface_set
from Core.Interface.Presenter.interfaces import PresenterInterface
from Core.Interface.View.UserControl.container import UserControlContainer


@register_interface_set(Metin2InterfaceFrame)
class Metin2InterfaceSet(BaseInterfaceSet):
	
	Name = 'Metin2'
	FrameType = Metin2InterfaceFrame
	
	@classmethod
	@property
	def AssetsDirectory(cls):
		return f'{cls.FrameType.AssetsDirectory}/Sets/Metin2/'
	
	@classmethod
	@property
	def UserControlTypes(cls) -> UserControlContainer:
		return cls.__user_control_types
	
	@classmethod
	def Initialize(cls):
		cls.__user_control_types: UserControlContainer = UserControlContainer(
			scripts_path=f'{cls.AssetsDirectory}/UserControls')
