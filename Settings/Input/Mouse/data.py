## System Imports


## Embedder Imports
from junctions import application


## Application Imports


## Library Imports


cursor_path = None

Cursors: dict[int, str] = {
	application.NORMAL: 		f'{cursor_path}/cursor.dds',
	application.ATTACK: 		f'{cursor_path}/attack.dds',
	application.TARGET: 		f'{cursor_path}/attack.dds',
	application.TALK: 			f'{cursor_path}/talk.dds',
	application.CANT_GO: 		f'{cursor_path}/cant.dds',
	application.PICK: 			f'{cursor_path}/pick.dds',
	application.DOOR: 			f'{cursor_path}/door.dds',
	application.CHAIR: 			f'{cursor_path}/chair.dds',
	application.MAGIC: 			f'{cursor_path}/pick.dds',
	application.BUY: 			f'{cursor_path}/buy.dds',
	application.SELL: 			f'{cursor_path}/sell.dds',
	application.CAMERA_ROTATE: 	f'{cursor_path}/camera_rotate.dds',
	application.HSIZE: 			f'{cursor_path}/hdrag.dds',
	application.VSIZE: 			f'{cursor_path}/vdrag.dds',
	application.HVSIZE: 		f'{cursor_path}/hvdrag.dds',
}

CursorPositions: dict[int, tuple[int, int]] = {
	application.NORMAL: 		(0, 0),
	application.TARGET: 		(0, 0),
	application.ATTACK: 		(0, 0),
	application.TALK:			(0, 0),
	application.CANT_GO: 		(0, 0),
	application.PICK: 			(0, 0),
	application.DOOR: 			(0, 0),
	application.CHAIR: 			(0, 0),
	application.MAGIC: 			(0, 0),
	application.BUY: 			(0, 0),
	application.SELL: 			(0, 0),
	application.CAMERA_ROTATE: 	(0, 0),
	application.HSIZE: 			(-16, -16),
	application.VSIZE: 			(-16, -16),
	application.HVSIZE: 		(-16, -16),
}

