## System Imports
from dataclasses import dataclass

## Application Imports

## Library Imports


@dataclass(frozen=True, slots=True, order=True)
class RaceSkinData:

	skin: str
	model: str


@dataclass(frozen=True, slots=True, order=True)
class RaceModelData:

	vnum: int
	model: str


@dataclass(frozen=True, slots=True, order=True)
class RaceData:

	races: list[RaceModelData]
	skins: list[RaceSkinData]

