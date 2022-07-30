## System Imports
from enum import unique, IntEnum

## Application Imports

## Library Imports


@unique
class PhaseState(IntEnum):
	
	Logo            = 0
	Login           = 1
	Select          = 2
	Empire          = 3
	ReselectEmpire  = 4
	Create          = 5
	Loading         = 6
	Game            = 7


@unique
class PhaseEnum(IntEnum):
	
	Logo    = 0
	Login   = 1
	Select  = 2
	Create  = 3
	Loading = 4
	Game    = 5
	Empire  = 6

