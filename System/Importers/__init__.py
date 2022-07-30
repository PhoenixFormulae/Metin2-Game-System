## System Imports
import builtins


## Application Imports
from System.Importers.pack_cython import PackCythonLoader


## Library Imports
from Core.Imports import Loaders


def Initialize():
	
	# TODO: Cython modules should only be loaded if cython usage is enabled by the embedder
	#       Also why is this flag in the builtins module? Why was this the idea and how it came to this conclusion
	if builtins.__USE_CYTHON__:
		Loaders.AddLoader(PackCythonLoader)
