# Standard Imports


# Library Imports
from Managers.Network.Connection.Methods.ServerConnection import ConnectionSettings, ServerConnection

# External Imports


def Initialize():
	connection_settings = ConnectionSettings()
	connection = ServerConnection(connection_settings)
	
	return connection
