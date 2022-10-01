from math import radians
import pygame
import pymunk.pygame_util
import pymunk

from game.items.Item import Item

class Boundarie(Item):
    def __init__(self, vertices: list, x: int, y: int) -> None:
        super().__init__(vertices, x, y, 0, 0, body_type=pymunk.Body.STATIC)
        self.shape.collision_type = 1

