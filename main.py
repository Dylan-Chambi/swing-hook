from math import radians
from game.App import App
from game.items.staticItems.Boundarie import Boundarie
from game.scenes.Scene import Scene


if __name__ == "__main__":
    scene1 = Scene()
    boundarie = Boundarie([(0, 0), (50, 0), (0, 1080), (50, 1080)], 0, 0)
    # boundarie.scale(1, 1)
    boundarie.rotate(radians(90))
    # boundarie.reflect(False, True)
    boundarie.translate(1920/2, 1080/2)
    scene1.addItem(boundarie)
    app = App(0, 0, 144, scene1)
    app.run()