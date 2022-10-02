from math import radians
import pygame
import pymunk.pygame_util
import pymunk

from game.items.Item import Item
from game.items.ItemRect import ItemRect

class Boundarie(ItemRect):
    def __init__(self, x: int, y: int, width: int, heigth: int) -> None:
        super().__init__(x, y, width, heigth, body_type=pymunk.Body.STATIC, mass=1, elasticity=1, friction=1)
        self.shape.collision_type = 1

