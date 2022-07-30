## System Imports


## Application Imports


## Library Imports
from dataclasses import dataclass


@dataclass(frozen=True, slots=True, order=True)
class CubeMaterialData:
	
	vnum: int
	count: int


@dataclass(frozen=True, slots=True, order=True)
class CubeCreationData:
	
	vnum: int
	count: int
	materials: list[CubeMaterialData]


@dataclass(frozen=True, slots=True, order=True)
class CubeResult:
	
	items: dict[int, int]
	
	@classmethod
	def from_simple(cls, raw: str) -> 'CubeResult':
		items = {}
		
		for item_result in raw.split('/'):
			vnum, count = map(int, item_result.split(','))
			
			items[vnum] = count
			
		return cls(items)


@dataclass(frozen=True, slots=True, order=True)
class CubeInformation:

	materials: dict
	gold: int
	
	@classmethod
	def from_simple(cls, raw: str):
		information = {}
		gold = 0
		
		index = 0
		for result in raw.split('@'):
			materials = {}
			
			mats = result.split('/')
			
			if len(mats) > 1:
				gold = mats[1]
			
			i = 0
			for material in mats[0].split('&'):
				vnum, count = map(int, material.split(','))
				materials[i] = (vnum, count)
				
				i += 1
			
			information[index] = materials
			index += 1
		
		return cls(information, gold)
			

if __name__ == '__main__':
	
	info = '14209,1&71123,2&71129,2&50635,3@14209,1&71123,2&71129,2&50636,3@14209,1&71123,2&71129,2&50637,3@14209,1&71123,2&71129,2&50638,3@17209,1&71123,2&71129,2&50635,3@17209,1&71123,2&71129,2&50636,3@17209,1&71123,2&71129,2&50637,3'
	
	cube_materials = CubeInformation.from_simple(info)
	
	another_info = '17209,1&71123,2&71129,2&50638,3@16209,1&71123,2&71129,2&50635,3@16209,1&71123,2&71129,2&50636,3@16209,1&71123,2&71129,2&50637,3@16209,1&71123,2&71129,2&50638,3'
	
	another_cube_materials = CubeInformation.from_simple(info)
	
	pass

