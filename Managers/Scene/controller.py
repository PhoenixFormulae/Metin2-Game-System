# Standard Imports

# Embedder Imports
from junctions import group, sound, character, background

# Library Imports
from Interface.calls import BaseCalls
from Settings.Scene.data import SceneSettings
from Managers.Scene.Camera.controller import CameraController


# External Imports


class SceneController(BaseCalls):

    @property
    def Camera(self) -> CameraController:
        return self.__camera

    def __init__(self, settings: SceneSettings):
        super().__init__()

        self.__settings = settings

        self.__camera = CameraController(settings.camera)

    def Setup(self):
        self.SetupScene()
        self.SetupActors()
        self.Camera.Setup()

    def SetupScene(self):
        background.Initialize()
        background.LoadMap(self.__settings.background.map_name,
                           self.__settings.background.x, self.__settings.background.y, self.__settings.background.z)

    # background.SetShadowLevel(background.SHADOW_ALL)
    # background.VisibleGuildArea()

    # background.SetViewDistanceSet(2000, 25600)
    # background.SelectViewDistanceNum(background.DISTANCE0)

    def SetupActors(self):
        for actor in self.__settings.actors:
            self.MakeCharacter(*actor.tuple())

    # player.SetMainCharacterIndex(1)

    @staticmethod
    def MakeCharacter(index: int, race: int, x: int, y: int):
        character.CreateInstance(index)
        character.SelectInstance(index)
        character.SetVirtualID(index)
        character.SetInstanceType(character.INSTANCE_TYPE_PLAYER)

        character.SetRace(race)
        character.SetArmor(0)
        character.SetHair(0)
        character.Refresh()
        character.SetMotionMode(character.MOTION_MODE_GENERAL)
        character.SetLoopMotion(character.MOTION_WAIT)

        character.SetPixelPosition(x, y, 0)
        character.SetDirection(character.DIR_NORTH)

    @staticmethod
    def SetupSound():
        sound.SetMusicVolume(50)
        sound.FadeInMusic("bgm/another_way.mp3")

    ## Embedder Calls
    @staticmethod
    def OnRender():
        group.ClearDepthBuffer()
        group.SetOmniLight()

        character.Deform()
        character.Render()
        character.RenderCollision()

        # grp.RestoreViewport()

        group.SetInterfaceRenderState()

    # background.RenderCollision()
