from ast import main
from math import radians
from game.App import App
from game.items.actors.Player import Player
from game.items.elements.String import String
from game.items.staticItems.Boundarie import Boundarie
from game.scenes.Scene import Scene
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, DT
from game.scenes.levels.Level1 import Level1
from game.scenes.menus.Credits import Credits
from game.scenes.menus.MainMenu import MainMenu

if __name__ == "__main__":
    level1 = Level1()

    app = App(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)

    main_menu = MainMenu(app)
    main_menu.play_scene = level1
    main_menu.credits_scene = level1

    credits = Credits(app)
    credits.back_scene = main_menu

    main_menu.credits_scene = credits

    app.change_scene(main_menu)
    app.run()