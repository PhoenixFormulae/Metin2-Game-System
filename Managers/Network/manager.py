# Standard Imports

# Library Imports
from FSM.decorators import register_state
from System.Manager.base import BaseManager
from Managers.Network.Connection import ServerConnection

# Library Imports


@register_state()
class NetworkManager(BaseManager):
	
	__connection: ServerConnection = None
	
	@classmethod
	def Ready(cls):
		from Managers.Network import Connection
		cls.__connection = Connection.Initialize()
