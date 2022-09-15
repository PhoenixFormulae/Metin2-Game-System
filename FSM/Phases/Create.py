# Standard Imports

# Embedder Imports

# Library Imports
from FSM.enums import PhaseState
from FSM.Phases import BasePhase

# External Imports


class PhaseCreateState(BasePhase):
	
	def __init__(self):
		super().__init__(name=PhaseState.Create.name, value=PhaseState.Create)

