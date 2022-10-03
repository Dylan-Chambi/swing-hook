from math import radians
from game.App import App
from game.items.actors.Player import Player
from game.items.elements.String import String
from game.items.staticItems.Boundarie import Boundarie
from game.scenes.Scene import Scene
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, DT
from game.scenes.levels.Level1 import Level1

if __name__ == "__main__":
    level1 = Level1()


    app = App(SCREEN_WIDTH, SCREEN_HEIGHT, FPS, level1)
    app.run()