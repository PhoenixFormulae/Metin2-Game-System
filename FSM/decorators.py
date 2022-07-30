## System Imports


## Application Imports
from FSM import model
from FSM.enums import PhaseState


## Library Imports


def register_state(phase: PhaseState | None = None):
	
	def decorator(subscriber: object):
		if not phase:
			for key, state in model.FiniteStateMachine.Phases.items():
				state.Dispatcher.add(subscriber)
		else:
			model.FiniteStateMachine.Phases[phase].Dispatcher.add(subscriber)
		
		return subscriber
	
	return decorator
