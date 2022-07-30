## System Imports
from importlib.abc import Loader
from importlib.machinery import ModuleSpec

## Embedder Imports
from junctions import pack

## Application Imports

## Library Imports


class PackImporter(Loader):
    def __init__(self, py_path):
        """Store path to python file"""
        self.py_path = py_path

    @classmethod
    def find_spec(cls, name, path, target=None):
        """Look for the pack python file in the virtual space"""
        package, _, module_name = name.rpartition(".")
        py_file_name = f"{module_name}.py"
        
        if pack.Exist(py_file_name):
            return ModuleSpec(name, cls(py_file_name))
    
    @classmethod
    def create_module(cls, spec):
        """Returning None uses the standard machinery for creating modules"""
        return None
    
    def exec_module(self, module):
        """Executing the module means reading the python file"""
        module.__file__ = str(self.py_path)
        pass

    def __repr__(self):
        """Nice representation of the class"""
        return f"{self.__class__.__name__}({str(self.py_path)!r})"
    
    def module_repr(self, module):
        pass
