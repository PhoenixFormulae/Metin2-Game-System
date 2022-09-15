# Standard Imports
from importlib.abc import Loader
from importlib.machinery import ModuleSpec

# Embedder Imports
from junctions import root_lib

# Library Imports

# External Imports


class PackCythonLoader(Loader):
	
	def __init__(self, path):
		"""Store path to python file"""
		self.__path = path
	
	@classmethod
	def find_spec(cls, name, path, target=None):
		"""Look for the pack python file in the virtual space"""
		package, _, module_name = name.rpartition(".")
		py_file_name = f"{module_name}.py"
		
		print(path)
		print(target)
		
		if root_lib.isExist(py_file_name):
			return ModuleSpec(name, cls(py_file_name))
	
	@classmethod
	def create_module(cls, spec):
		"""Returning None uses the standard machinery for creating modules"""
		return root_lib.moduleImport(spec.name)
	
	def exec_module(self, module):
		"""Executing the module means reading the python file"""
		module.__file__ = str(self.__path)
	
	def __repr__(self):
		"""Nice representation of the class"""
		return f"{self.__class__.__name__}({str(self.__path)!r})"
	
	def module_repr(self, module):
		module.__repr__()
