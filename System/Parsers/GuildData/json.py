# Standard Imports

# Library Imports
from System.Parsers.GuildData import GuildBuildingData

# External Imports
from dataclasses_json import dataclass_json


@dataclass_json
class GuildBuildingDataBasic(GuildBuildingData):
	pass

