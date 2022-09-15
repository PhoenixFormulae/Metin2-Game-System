# Standard Imports

# Embedder Imports
from junctions import group
from junctions import application
from junctions import input_method

# Library Imports
from FSM.enums import PhaseState
from FSM.decorators import register_state
from System.Manager.base import BaseManager
from Settings.Input.data import IMEPasteEnabled

# External Imports
from game_system import Metin2GameSystem
from Core.Manager.decorators import register_manager


@register_state()
@register_manager(Metin2GameSystem)
class InterfaceManager(BaseManager):
	
	@classmethod
	def Ready(cls):
		input_method.EnablePaste(IMEPasteEnabled)
	
	## Embedder Calls
	def OnUpdate(self):
		if self.__current_phase == PhaseState.Game:
			self.OnUpdateGame()
	
	def OnRender(self):
		if self.__current_phase == PhaseState.Game:
			self.OnRenderGame()
	
	@classmethod
	def OnRenderGame(cls):
		application.RenderGame()
		
		group.PopState()
		group.SetInterfaceRenderState()

