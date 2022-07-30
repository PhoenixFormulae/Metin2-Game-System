## System Imports


## Application Imports


## Library Imports
from Core.Interface.data import BaseWindowConfiguration


DebugRendering: bool = True

ConsoleEnabled: bool = True

ScreenshotsDirectory: str = 'screenshot'

Metin2WindowConfiguration: BaseWindowConfiguration = BaseWindowConfiguration(
	title="Phoenix Formulae - Metin2",
	width=1024,
	height=700,
	windowed=True
)

