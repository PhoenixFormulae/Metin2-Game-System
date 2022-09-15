# Standard Imports

# Embedder Imports

## Application Imports
from Managers.Network.Connection import ConnectionSettings, ServerConnection

# External Imports


def Initialize():
	connection_settings = ConnectionSettings()
	connection = ServerConnection(connection_settings)
	
	return connection
