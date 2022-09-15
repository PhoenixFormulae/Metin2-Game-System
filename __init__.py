# Standard Imports


# Library Imports
from game_system import Metin2GameSystem

# External Imports
import Core
from Core import CoreSystem
from Core.System.data import GameSystemConfiguration, GameSystemDetails


def init():
    Core.Initialize()

    configuration = GameSystemConfiguration('Metin2 Game System',
                                            GameSystemDetails('Data/Resources/Graphics/2D/Logos/pxf-logo.tga'))

    CoreSystem.GameSystem = Metin2GameSystem(configuration)
    CoreSystem.Run()


if __name__ == '__main__':
    init()
