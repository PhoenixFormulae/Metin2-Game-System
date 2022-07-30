## System Imports

## Application Imports
from System.Parsers.GuildData import GuildBuildingData

## Library Imports
from dataclasses_json import dataclass_json


@dataclass_json
class GuildBuildingDataBasic(GuildBuildingData):
	pass

