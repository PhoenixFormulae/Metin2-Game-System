## System Imports
from enum import unique, IntEnum


## Embedder Imports
from junctions import application
from junctions import group
from junctions import window_manager


## Application Imports
from Settings.Scene.data import CameraSettings


## Library Imports
from Interface.calls import BaseCalls


class CameraController(BaseCalls):
	
	@property
	def Speed(self) -> int:
		return self.__speed
	
	@property
	def Settings(self) -> CameraSettings:
		return self.__settings
	
	@Speed.setter
	def Speed(self, value: int):
		application.SetCameraSpeed(value)
		self.__speed = value
	
	def __init__(self, settings: CameraSettings):
		super().__init__()
		self.__settings = settings
		
		width, height = wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight()
		new_width, new_height = float(width), float(height)
		
		self.__camera_settings: tuple[float, float, float, float] = 1550.0, 15.0, 180.0, 95.0
		self.__viewport: tuple[float, float, float, float] = (0, 0, new_width / width, new_height / height)
		self.__perspective: tuple[float, float, float, float] = (10, new_width / new_height, 1000, 3000)
		
		self.__axis: tuple[float, float, float] = self.__settings.axis.xyz_tuple()
		
		self.__speed: int = 200  # TODO: Move speed setting to somewhere more proper
		
		self.axis_delta: tuple[float, float, float] = 10, 10, 10
		
		self.__move: MovementAxis = MovementAxis.Neutral
		self.__direction: bool = True
	
	def Setup(self):
		# application.EnableSpecialCameraMode()
		
		application.SetCameraSetting(*self.__settings.axis.xyzdrp_tuple())
		grp.SetViewport(*self.__settings.viewport.xywh_tuple())
		grp.SetPerspective(*self.__settings.perspective.fanf_tuple())
		application.SetCamera(*self.__settings.axis.dprh_tuple())
		application.SetCenterPosition(*self.__settings.axis.xyz_tuple())
	
	def SetAxis(self, axis: 'MovementAxis', direction: bool = False):
		self.__move = axis
		self.__direction = direction
	
	def MoveXAxis(self, direction: bool):
		if direction:
			new_x = self.__axis[0] + (self.__speed / 100 * self.axis_delta[0])
		else:
			new_x = self.__axis[0] - (self.__speed / 100 * self.axis_delta[0])
			
		self.__axis = new_x, self.__axis[1], self.__axis[2]
		
		application.SetCenterPosition(*self.__axis)
	
	def MoveYAxis(self, direction: bool):
		if direction:
			new_y = self.__axis[1] + (self.__speed / 100 * self.axis_delta[1])
		else:
			new_y = self.__axis[1] - (self.__speed / 100 * self.axis_delta[1])
		
		self.__axis = self.__axis[0], new_y, self.__axis[2]
		
		application.SetCenterPosition(*self.__axis)
	
	def MoveZAxis(self, direction: bool):
		if direction:
			new_z = self.__axis[2] + (self.__speed / 100 * self.axis_delta[2])
		else:
			new_z = self.__axis[2] - (self.__speed / 100 * self.axis_delta[2])
		
		self.__axis = self.__axis[0], self.__axis[1], new_z
		
		application.SetCenterPosition(*self.__axis)
	
	## Embedder Calls
	def OnUpdate(self):
		pass
	
	def OnRender(self):
		if self.__move == MovementAxis.X:
			self.MoveXAxis(self.__direction)
			
		elif self.__move == MovementAxis.Z:
			self.MoveZAxis(self.__direction)
		
		elif self.__move == MovementAxis.Y:
			self.MoveYAxis(self.__direction)
		
	

@unique
class MovementAxis(IntEnum):
	
	Neutral = 0
	X = 1
	Y = 2
	Z = 3
