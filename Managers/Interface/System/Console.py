## System Imports

## Embedder Imports
from junctions import application

## Application Imports

## Library Imports
from System.Manager.base import BaseManager


class ConsoleManager(BaseManager):
	
	@classmethod
	def Ready(cls):
		cls.__enabled = False
	
	@classmethod
	def COMMAND_ConsoleEnable(cls):
		cls.__enabled = True
		application.EnableSpecialCameraMode()

	

