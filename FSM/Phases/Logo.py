# Standard Imports


# Embedder Imports
from junctions import network


# Library Imports
from FSM.enums import PhaseState
from FSM.Phases import BasePhase


# External Imports


class PhaseLogoState(BasePhase):
	
	def __init__(self):
		super().__init__(name=PhaseState.Logo.name, value=PhaseState.Logo, initial=True)
	
	## State Machine Calls
	def OnEnter(self, state):
		network.Disconnect()
		self.Enter(state)
	
	def OnExit(self, state):
		self.Exit(state)
	
