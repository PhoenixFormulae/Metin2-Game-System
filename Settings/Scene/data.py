## System Imports
from dataclasses import dataclass

## Embedder Imports

## Application Imports

## Library Imports
from Settings.Scene.Camera.data import CameraSettings


@dataclass(slots=True, order=True)
class BackgroundSettings:
	
	map_name: str
	x: int
	y: int
	z: int


@dataclass(slots=True, order=True)
class ActorSettings:
	
	index: int
	race: int
	x: int
	y: int
	
	def tuple(self) -> tuple[int, int, int, int]:
		return self.index, self.race, self.x, self.y


@dataclass(slots=True, order=True)
class SceneSettings:

	background: BackgroundSettings | None
	actors: tuple[ActorSettings]
	camera: CameraSettings
	
