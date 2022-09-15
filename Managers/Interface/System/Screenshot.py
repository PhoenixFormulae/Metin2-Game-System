## System Imports
import os
from pathlib import Path

# Embedder Imports
from junctions import group

## Application Imports
from FSM.decorators import register_state
from System.Manager.base import BaseManager
from Settings.Interface.data import ScreenshotsDirectory
from Interface.Presenters.System.Screenshot import ScreenshotPresenter

## Library Imports


@register_state()
class ScreenshotManager(BaseManager):

	__presenter = ScreenshotPresenter()

	@classmethod
	def Ready(cls):
		...

	def Screenshot(self):
		succeeded = False
		name = None
		
		if ScreenshotsDirectory:
			screenshots_directory = Path(f'{os.getcwd()}/{ScreenshotsDirectory}/')
			
			if not screenshots_directory.exists():
				screenshots_directory.mkdir()
				
				succeeded, name = group.SaveScreenShotToPath(screenshots_directory.__str__())[0]
		else:
			succeeded, name = group.SaveScreenShot()
		
		if succeeded:
			self.__presenter.OnSuccess(name)
		else:
			self.__presenter.OnFailure()

	
