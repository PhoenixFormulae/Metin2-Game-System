## System Imports

## Embedder Imports

## Application Imports
from game_system import Metin2GameSystem
from System.Manager.base import BaseManager

## Library Imports
from Core.Manager.decorators import register_manager


@register_manager(Metin2GameSystem)
class NotificationsManager(BaseManager):
	
	def __init__(self):
		super().__init__()

	## Embedder Calls
	def BINARY_SetBigMessage(self, message: str):
		self.__presenter.OnBigTipMessage(message)

	def BINARY_SetTipMessage(self, message: str):
		self.__presenter.OnTipMessage(message)
	
	def BINARY_AppendNotifyMessage(self, notification_type: int):
		self.__presenter.OnMessage(notification_type)
	
