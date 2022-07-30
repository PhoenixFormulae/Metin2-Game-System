## System Imports
from typing import Protocol

## Application Imports

## Library Imports


class MessengerModelProtocol(Protocol):
	...


class MessengerPresenterProtocol(Protocol):
	...


class MessengerViewProtocol(Protocol):
	
	def OnToggle(self):
		...
	
	def OnMobile(self):
		...
	
	def OnAuthority(self):
		...
	
	def OnBlock(self):
		...
	
