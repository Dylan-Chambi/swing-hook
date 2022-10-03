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
from game.scenes.menus.LoseScreen import LoseScreen
from game.scenes.menus.MainMenu import MainMenu
from game.scenes.menus.WinScreen import WinScreen

if __name__ == "__main__":

    app = App(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)

    level1 = Level1(app)

    lose_screen = LoseScreen(app)
    win_screen = WinScreen(app)

    level1.lose_scene = lose_screen
    level1.win_scene = win_screen


    main_menu = MainMenu(app)
    main_menu.play_scene = level1
    main_menu.credits_scene = level1

    lose_screen.menu_scene = main_menu
    win_screen.menu_scene = main_menu


    credits = Credits(app)
    credits.back_scene = main_menu

    main_menu.credits_scene = credits

    app.change_scene(main_menu)
    app.run()