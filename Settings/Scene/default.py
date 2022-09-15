# Standard Imports

# Library Imports
from Settings.Scene.data import SceneSettings, CameraSettings, ActorSettings, BackgroundSettings
from Settings.Scene.Camera.data import CameraAxisSettings, CameraViewportSettings, CameraPerspectiveSettings

# External Imports


DefaultScene: SceneSettings = SceneSettings(
	
	background=BackgroundSettings(
		map_name='metin2_map_c1', x=30000, y=40000, z=0
	),
	
	actors=(
		ActorSettings(index=1, race=0, x=0, y=0),
	),
	
	camera=CameraSettings(
		axis=CameraAxisSettings(x=2000, y=-6000, z=1000, zoom=10, rotation=100, pitch=5),
		viewport=CameraViewportSettings(x=1000, y=1000, width=800, height=800),
		perspective=CameraPerspectiveSettings(100, 1, 1000, 1000)
	)
)
