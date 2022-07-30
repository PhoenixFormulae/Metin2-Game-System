## System Imports

## Application Imports
from FSM.enums import PhaseState
from FSM.Phases.Logo import PhaseLogoState
from FSM.Phases.Game import PhaseGameState
from FSM.Phases.Login import PhaseLoginState
from FSM.Phases.Create import PhaseCreateState
from FSM.Phases.Select import PhaseSelectState
from FSM.Phases.Loading import PhaseLoadingState
from System.FSM.interfaces import PhaseInterface

## Library Imports
from statemachine import StateMachine


class GameFiniteStateMachine(StateMachine):
	
	previous_state = None
	
	# States declarations
	logo = PhaseLogoState()
	login = PhaseLoginState()
	select = PhaseSelectState()
	create = PhaseCreateState()
	loading = PhaseLoadingState()
	game = PhaseGameState()
	
	Phases: dict[PhaseState, PhaseInterface] = {
		PhaseState.Logo: logo,
		PhaseState.Login: login,
		PhaseState.Select: select,
		PhaseState.Create: create,
		PhaseState.Loading: loading,
		PhaseState.Game: game,
	}
	
	# Transitions
	to_logo = logo.to.itself()
	to_login = logo.to(login) | game.to(login)
	to_select = login.to(select)
	to_create = select.to(create)
	to_loading = select.to(loading)
	to_game = loading.to(game)
	
	def on_enter_state(self, state):
		if state == self.previous_state:
			return
		
		self.current_state.OnEnter(self.previous_state)
	
	def on_exit_state(self, state):
		if state == self.previous_state:
			return
		
		self.previous_state = state
		self.current_state.OnExit(state)


FiniteStateMachine = GameFiniteStateMachine()
