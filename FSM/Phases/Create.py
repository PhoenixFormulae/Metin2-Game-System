## System Imports

## Embedder Imports

## Application Imports
from FSM.enums import PhaseState
from FSM.Phases import BasePhase

## Library Imports


class PhaseCreateState(BasePhase):
	
	def __init__(self):
		super().__init__(name=PhaseState.Create.name, value=PhaseState.Create)

