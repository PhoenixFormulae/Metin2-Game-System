# Standard Imports
from enum import Enum
from typing import List


# Embedder Imports
from junctions import application
from junctions import window_manager


# Library Imports
from System.Interface.View.Control import Flag
from Interface.Frames.Metin2.Controls.types import Layer
from Interface.Frames.Metin2.Controls.Buttons.button import Button
from Interface.Events.Control.control_resize import ControlResizeEvent, ControlResizeEventArguments


# External Imports
from Core.Plugins import factory
from Core.Interface.View.decorators import generic_property


class ResizeDirections(Enum):
	Horizontal = 0
	Vertical = 1
	

@factory.register
class DragButton(Button):
	
	Type = 'drag_button'
	
	@property
	def restrict_area(self):
		return self.__restrict_area
	
	def __init__(self):
		super().__init__()
		self.AddStyleFlag(Flag.Movable)
		
		self.__directions: List[ResizeDirections] = []
		self.__restrict_area: List[int, int, int, int] = []
		
		# TODO: Maybe add the ability to disable control movement event trigger?
	
	def Register(self, layer: Layer):
		"""
		Registers the control as a 'Drag Button' type in the embedder
		given the button's layer
		
		:param layer: The layer of the control
		:return: The embedder control handle signature
		"""
		
		return window_manager.RegisterDragButton(self, layer.value)

	@generic_property('restrict', editable=True, required=False)
	def SetRestrictMovementArea(self, x: int, y: int, width: int, height: int):
		window_manager.SetRestrictMovementArea(self.Handle, x, y, width, height)
		
		self.__restrict_area = [x, y, width, height]
	
	def GetRestrictMovementArea(self):
		# return wndMgr.GetRestrictMovementArea(self.Handle)
		pass
	
	@generic_property('directions', editable=True, required=False)
	def SetDirections(self, directions: List[str]):
		for direction in directions:
			if type(direction) == str:
				direction_value = ResizeDirections[direction.capitalize()]
				self.__directions.append(direction_value)
		
		self.__RefreshDirections()
	
	def __RefreshDirections(self):
		if ResizeDirections.Horizontal in self.__directions and ResizeDirections.Vertical not in self.__directions:
			self.AddStyleFlag(Flag.Restrict_Y)
		
		if ResizeDirections.Horizontal not in self.__directions and ResizeDirections.Vertical in self.__directions:
			self.AddStyleFlag(Flag.Restrict_X)
		
		elif ResizeDirections.Horizontal in self.__directions and ResizeDirections.Vertical in self.__directions:
			# todo: Create remove style flag function
			# self.RemoveStyleFlag(Flag.Restrict_X)
			# self.RemoveStyleFlag(Flag.Restrict_Y)
			pass
	
	def OnMove(self):
		x, y = self.GetLocalPreviousPosition()
		
		x_difference = self.GetLocalXPosition() - x
		y_difference = self.GetLocalYPosition() - y
		
		if x_difference == 0 and y_difference == 0:
			return
		
		print(f"xdif: {x_difference} ydif: {y_difference}")
		self.TriggerEvent(ControlResizeEvent, ControlResizeEventArguments(x_difference, y_difference))
	
	def OnMouseOverIn(self):
		if ResizeDirections.Horizontal in self.__directions and ResizeDirections.Vertical not in self.__directions:
			application.SetCursor(application.HSIZE)
		
		elif ResizeDirections.Horizontal not in self.__directions and ResizeDirections.Vertical in self.__directions:
			application.SetCursor(application.VSIZE)
		
		elif ResizeDirections.Horizontal in self.__directions and ResizeDirections.Vertical in self.__directions:
			application.SetCursor(application.HVSIZE)
		else:
			application.SetCursor(application.CANT_GO)
	
	def OnMouseOverOut(self):
		application.SetCursor(application.NORMAL)
	
	def CallEvent(self):
		pass
	