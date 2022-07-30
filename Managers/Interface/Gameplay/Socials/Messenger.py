## System Imports

## Embedder Imports
from junctions import network
from junctions import messenger

## Application Imports
from FSM.enums import PhaseState
from FSM.decorators import register_state
from System.Manager.base import BaseManager

## Library Imports

	
@register_state(PhaseState.Game)
class MessengerManager(BaseManager):
	
	@classmethod
	def Ready(cls):
		cls.__friend_requests: list[str] = []
	
	## State Machine Calls
	def OnEnterGamePhase(self):
		pass
	
	@classmethod
	def OnExitGamePhase(cls):
		messenger.Destroy()
	
	def AcceptFriendRequest(self, name: str):
		network.SendChatPacket("/messenger_auth y " + name)
		self.__friend_requests.remove(name)
	
	def DenyFriendRequest(self, name: str):
		network.SendChatPacket("/messenger_auth n " + name)
		self.__friend_requests.remove(name)
	
	def OnMessengerAddFriendQuestion(self, name: str):
		self.__friend_requests.append(name)

