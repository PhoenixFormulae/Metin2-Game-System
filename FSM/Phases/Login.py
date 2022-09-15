# Standard Imports


# Embedder Imports
from junctions import network


# Library Imports
from FSM.enums import PhaseState
from FSM.Phases import BasePhase


# External Imports


class PhaseLoginState(BasePhase):
	
	def __init__(self):
		super().__init__(name=PhaseState.Login.name, value=PhaseState.Login)
	
	## State Machine Calls
	def OnEnter(self, state):
		network.Disconnect()
		self.Enter(state)
	
	def OnExit(self, state):
		self.Exit(state)

