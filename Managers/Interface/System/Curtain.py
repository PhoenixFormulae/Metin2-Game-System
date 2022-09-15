# Standard Imports

# Library Imports

# External Imports
from FSM.decorators import register_state
from FSM.enums import PhaseState
from System.Manager.base import BaseManager


@register_state(PhaseState.Game)
class CurtainManager(BaseManager):
	pass
