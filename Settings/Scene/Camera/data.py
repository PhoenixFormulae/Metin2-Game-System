## System Imports
from dataclasses import dataclass


## Application Imports


## Library Imports


GameCameraDistanceLimits: list[float] = [
	2500,
	8500
]

GameCameraDistance: float = 1550
GameCameraPitch: float = 27
GameCameraRotation: float = 0
GameCameraHeight: float = 100


@dataclass(slots=True, order=True)
class CameraAxisSettings:
	
	x: int
	y: int
	z: int
	zoom: int
	rotation: int
	pitch: int
	
	def xyz_tuple(self) -> tuple[int, int, int]:
		return self.x, self.y, self.z
	
	def dprh_tuple(self) -> tuple[int, int, int, int]:
		return self.zoom, self.pitch, self.rotation, self.z,
	
	def xyzdrp_tuple(self):
		return self.x, self.y, self.z, self.zoom, self.rotation, self.pitch


@dataclass(slots=True, order=True)
class CameraViewportSettings:

	x: int
	y: int
	width: int
	height: int
	
	def xywh_tuple(self) -> tuple[int, int, int, int]:
		return self.x, self.y, self.width, self.height


@dataclass(slots=True, order=True)
class CameraPerspectiveSettings:

	fov: float
	aspect: float
	near: float
	far: float
	
	def fanf_tuple(self) -> tuple[float, float, float, float]:
		return self.fov, self.aspect, self.near, self.far


@dataclass(slots=True, order=True)
class CameraSettings:
	
	axis: CameraAxisSettings
	viewport: CameraViewportSettings
	perspective: CameraPerspectiveSettings
	
