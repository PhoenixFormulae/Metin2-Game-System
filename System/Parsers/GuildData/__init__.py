# Standard Imports
from dataclasses import dataclass

# Library Imports

# External Imports


@dataclass(frozen=True, slots=True, order=True)
class GuildBuildingData:
	
	vnum: int
	type: str
	model: str
	name: str
	registry: list[str, str, str, str]
	rotation_limit_x: int
	rotation_limit_y: int
	rotation_limit_z: int
	price: int
	materials: int
	npc: int
	group: int
	depend_group: int
