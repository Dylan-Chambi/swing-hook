from math import radians
from game.App import App
from game.items.actors.Player import Player
from game.items.elements.String import String
from game.items.staticItems.Boundarie import Boundarie
from game.scenes.Scene import Scene
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, DT

if __name__ == "__main__":
    player = Player(500, 500, 50, 50)
    scene1 = Scene(player)

    BOUNDARIES_WIDTH = 50
    boundarie = Boundarie(SCREEN_WIDTH / 2, SCREEN_HEIGHT - BOUNDARIES_WIDTH / 2, SCREEN_WIDTH, BOUNDARIES_WIDTH)
    boundarie2 = Boundarie(SCREEN_WIDTH / 2, BOUNDARIES_WIDTH / 2, SCREEN_WIDTH, BOUNDARIES_WIDTH)
    boundarie3 = Boundarie(BOUNDARIES_WIDTH / 2, SCREEN_HEIGHT / 2, BOUNDARIES_WIDTH, SCREEN_HEIGHT)
    boundarie4 = Boundarie(SCREEN_WIDTH - BOUNDARIES_WIDTH / 2, SCREEN_HEIGHT / 2, BOUNDARIES_WIDTH, SCREEN_HEIGHT)

    # boundarie.scale(1, 1)
    # boundarie.rotate(radians(90))
    # boundarie.reflect(False, True)
    # boundarie.translate(1920/2, 1080/2)
    scene1.add_item(boundarie)
    scene1.add_item(boundarie2)
    scene1.add_item(boundarie3)
    scene1.add_item(boundarie4)


    # string1 = String(player, (0, 0))


    app = App(SCREEN_WIDTH, SCREEN_HEIGHT, FPS, scene1)
    app.run()