## System Imports

## Embedder Imports

## Application Imports
from Managers.Network.Connection import ConnectionSettings, ServerConnection

## Library Imports


def Initialize():
	connection_settings = ConnectionSettings()
	connection = ServerConnection(connection_settings)
	
	return connection
