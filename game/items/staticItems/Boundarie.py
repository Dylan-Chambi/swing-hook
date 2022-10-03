from math import radians
import pygame
# import pymunk.pygame_util
# import pymunk

from game.items.Item import Item
from game.items.ItemRect import ItemRect

class Boundarie(ItemRect):
    def __init__(self, x: int, y: int, width: int, heigth: int, bg_color: tuple = (100, 100, 100)) -> None:
        super().__init__(x, y, width, heigth, bg_color=bg_color)
        # self.shape.collision_type = 1
