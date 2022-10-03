import pygame

from game.App import App
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, DT
from game.scenes.levels.Level1 import Level1
from game.scenes.menus.Credits import Credits
from game.scenes.menus.LoseScreen import LoseScreen
from game.scenes.menus.MainMenu import MainMenu
from game.scenes.menus.Splash1 import Splash1
from game.scenes.menus.Splash2 import Splash2
from game.scenes.menus.WinScreen import WinScreen

class GameManager():
    

    def start_game(self):
        app = App(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)

        splash_scene1 = Splash1(app)
        splash_scene2 = Splash2(app)

        level1 = Level1(app)

        lose_screen = LoseScreen(app)
        win_screen = WinScreen(app)

        level1.lose_scene = lose_screen
        level1.win_scene = win_screen


        main_menu = MainMenu(app)
        splash_scene1.next_scene = splash_scene2
        splash_scene2.next_scene = main_menu
        level1.menu_scene = main_menu
        main_menu.play_scene = level1
        main_menu.credits_scene = level1

        lose_screen.retry_scene = level1
        lose_screen.menu_scene = main_menu
        win_screen.menu_scene = main_menu


        credits = Credits(app)
        credits.back_scene = main_menu

        main_menu.credits_scene = credits

        app.change_scene(splash_scene1)
        app.run()