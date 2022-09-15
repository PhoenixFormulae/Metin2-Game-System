# Standard Imports

# Embedder Imports
from junctions import player
from junctions import network
from junctions import exchange
from junctions import character

# Library Imports
from FSM.enums import PhaseState
from FSM.decorators import register_state
from Managers.Input.Mouse.manager import MouseManager

# External Imports
from Core.Manager.interfaces import ManagerInterface


@register_state(PhaseState.Game)
class ExchangeManager(ManagerInterface):
    _protocol = None

    @classmethod
    def Ready(cls):
        MouseManager.Subscribe(cls)

    ## State Machine Calls
    @classmethod
    def OnEnterGamePhase(cls):
        exchange.InitTrading()

    def OnExitGamePhase(self):
        pass

    ## Mouse Calls
    @classmethod
    def OnMouseRequestMoveItem(cls, target_id: int, amount: int):
        if not character.HasInstance(target_id):
            return

        if player.GetMainCharacterIndex() == target_id:
            return

        network.SendExchangeStartPacket(target_id)
        network.SendExchangeElkAddPacket(amount)

    @classmethod
    def StartExchange(cls):
        cls._protocol.StartExchange()

    @classmethod
    def EndExchange(cls):
        cls._protocol.EndExchange()

    @classmethod
    def RefreshExchange(cls):
        cls._protocol.RefreshExchange()
