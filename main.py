from math import radians
from game.App import App
from game.items.actors.Player import Player
from game.items.elements.String import String
from game.items.staticItems.Boundarie import Boundarie
from game.scenes.Scene import Scene


if __name__ == "__main__":
    player = Player([(0, 0), (50, 0), (0, 50), (50, 50)], 500, 500)
    scene1 = Scene(player)
    boundarie = Boundarie([(0, 0), (50, 0), (0, 1080), (50, 1080)], 0, 0)
    boundarie2 = Boundarie([(0, 0), (50, 0), (0, 1080), (50, 1080)], 1870, 0)
    boundarie3 = Boundarie([(0, 0), (1920, 0), (0, 50), (1920, 50)], 0, 0)
    boundarie4 = Boundarie([(0, 0), (1920, 0), (0, 50), (1920, 50)], 0, 1030)

    # boundarie.scale(1, 1)
    # boundarie.rotate(radians(90))
    # boundarie.reflect(False, True)
    # boundarie.translate(1920/2, 1080/2)
    scene1.add_item(boundarie)
    scene1.add_item(boundarie2)
    scene1.add_item(boundarie3)
    scene1.add_item(boundarie4)


    # string1 = String(player, (0, 0))


    app = App(0, 0, 60, scene1)
    app.run()