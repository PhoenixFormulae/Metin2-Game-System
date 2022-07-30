## System Imports

## Embedder Imports
from junctions import chat
from junctions import shop


## Application Imports
from FSM.enums import PhaseState
from FSM.decorators import register_state
from System.Manager.base import BaseManager
from Managers.Input.Mouse.manager import MouseManager
from Managers.System.Command import ServerCommandManager

## Library Imports


@register_state(PhaseState.Game)
class PrivateShopManager(BaseManager):
	
	__presenter = None
	
	@classmethod
	def Ready(cls):
		MouseManager.Subscribe(cls)
		ServerCommandManager.Subscribe(cls)
	
	## State Machine Calls
	def OnEnterGamePhase(self):
		self.__presenter.Clear()
	
	def OnExitGamePhase(self):
		self.__presenter.Clear()
	
	## Embedder Calls
	def BINARY_PrivateShop_Appear(self, virtual_id: int, name: str):
		self.__presenter.OnAppear(virtual_id, name)

	def BINARY_PrivateShop_Disappear(self, virtual_id: int):
		self.__presenter.OnDisappear(virtual_id)
	
	## Command Calls
	def COMMAND_MyShopPriceList(self, item_vnum: int, item_price: int):
		self.__presenter.OnItemPrice(item_vnum, item_price)
	
	def COMMAND_OpenPrivateShop(self):
		self.__presenter.OnOpenNew()
	
	## Mouse Calls
	def OnMouseRequestDropItem(self):
		if not shop.IsBuildingPrivateShop():
			return
		
		MouseManager.CancelRequest()
		chat.AppendChat(chat.CHAT_TYPE_INFO, self.__locale('OpeningPrivateShopCannotDropItem'))
	
	def OnMouseRequestDropMoney(self):
		if not shop.IsBuildingPrivateShop():
			return
		
		MouseManager.CancelRequest()
		chat.AppendChat(chat.CHAT_TYPE_INFO, self.__locale('OpeningPrivateShopCannotDropMoney'))
	
