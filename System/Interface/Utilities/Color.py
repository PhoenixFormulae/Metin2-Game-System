# Standard Imports


# Library Imports
from junctions import group

# External Imports
from colour import Color


class ExtendedColor(Color):
	
	@property
	def hex_int(self):
		return int('0x' + self.get_hex_l()[1:], 0)
