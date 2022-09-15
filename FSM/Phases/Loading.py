# Standard Imports


# Embedder Imports


# Library Imports
from FSM.enums import PhaseState
from FSM.Phases import BasePhase


# External Imports


class PhaseLoadingState(BasePhase):
	
	def __init__(self):
		super().__init__(name=PhaseState.Loading.name, value=PhaseState.Loading)

