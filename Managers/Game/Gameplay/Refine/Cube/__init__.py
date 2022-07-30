## System Imports


## Embedder Imports
from junctions import network


## Application Imports
from FSM.enums import PhaseState
from FSM.decorators import register_state
from System.Manager.base import BaseManager
from Managers.Game.Gameplay.Refine.Cube.data import CubeResult, CubeInformation


## Library Imports


@register_state(PhaseState.Game)
class CubeManager(BaseManager):
	
	def __init__(self):
		super().__init__()
		
		self.__presenter = None
		
		self.__npc_vnum: int = 0
		self.__information: dict[int, CubeInformation] = {}
		self.__results: dict[int, CubeResult] = {}
	
	## Embedder Calls
	def BINARY_Cube_Open(self, vnum: int):
		self.__npc_vnum = vnum
		
		if vnum not in self.__information:
			network.SendChatPacket("/cube r_info")
			return
		
		creation_index = 0
		for creation in self.__information[vnum]:
			self.__presenter.AddResultItem(creation.vnum, creation.count)
			
			material_index = 0
			for material in creation.materials:
				self.__presenter.AddMaterialInfo(creation_index, material_index, material.vnum, material.count)
				material_index += 1
			
			creation_index += 1
		
		self.__presenter.Refresh()
	
	def BINARY_Cube_ResultList(self, vnum: int, result: str):
		if vnum == 0:
			self.__npc_vnum = self.__npc_vnum
		
		result = CubeResult.from_simple(result)
		self.__results[vnum] = result
		
		for item, count in result.items.items():
			self.__presenter.AddResultItem(item, count)
			
			result_count = len(result.items)
			request_count = 7
			
			mod_count = result_count % request_count
			split_count = int(result_count / request_count)
			
			for i in range(split_count):
				network.SendChatPacket(f'/cube r_info {i * request_count} {request_count}')
			
			if mod_count > 0:
				network.SendChatPacket(f'/cube r_info {split_count * request_count} {mod_count}')
	
	def BINARY_Cube_MaterialInfo(self, start_index: int, information: str):
		information = CubeInformation.from_simple(information)
		
		self.__information[start_index] = information
		
		for index, information in information.materials.items():
			for material_index, material in information:
				item, count = material
				self.__presenter.AddMaterial(start_index + index, material_index, item, count)
		
		self.__presenter.Refresh()
	
	def BINARY_Cube_Close(self):
		self.__presenter.Close()
	
	def BINARY_Cube_UpdateInfo(self, gold: int, item_vnum: int, count: int):
		self.__presenter(gold, item_vnum, count)
	
	def BINARY_Cube_Succeed(self, item_vnum: int, count: int):
		self.__presenter.Sucess(item_vnum, count)
	
	def BINARY_Cube_Failed(self):
		self.__presenter.Failed()
