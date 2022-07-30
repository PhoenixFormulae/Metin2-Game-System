## System imports

## Embedder imports
from junctions import network

## Application imports
from Settings.Network import data


## Library imports


class ConnectionSettings:
    AuthenticationServerAddress = ''
    AuthenticationServerPort = 1000

    GameServerAddress = ''
    GameServerPort = 1000


class ServerConnection:

    def __init__(self, settings: ConnectionSettings):
        self.settings = settings
        self.__setup()

    def __setup(self):
        network.SetHandler(self)

        # TODO: This may be necessary for the regular embedders
        network.SetTCPRecvBufferSize(128 * 1024)
        network.SetTCPSendBufferSize(4096)
        network.SetUDPRecvBufferSize(4096)

    def Connect(self, username: str, password: str):
        network.SetLoginInfo(username, password)

        if data.SequencePacketMode:
            network.SetPacketSequenceMode()

        if data.AccountKeepConnectionAlive:
            network.ConnectToAccountServer(self.settings.GameServerAddress,
                                           self.settings.GameServerPort,
                                           self.settings.AuthenticationServerAddress,
                                           self.settings.AuthenticationServerPort)
        else:
            network.ConnectTCP(ConnectionSettings.GameServerAddress,
                               ConnectionSettings.GameServerPort)

    @staticmethod
    def Disconnect():
        network.Disconnect()
