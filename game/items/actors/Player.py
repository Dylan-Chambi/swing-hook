from turtle import Vec2D
import numpy
import pymunk
import pygame
from pygame.locals import *
from game.items.Item import Item

class Player(Item):

    def __init__(self, vertices: list, x: int, y: int) -> None:
        super().__init__(vertices, x, y, 0, 0, body_type=pymunk.Body.DYNAMIC, mass=10, elasticity=0, friction=0)
        self.density = 0
        self.keys = {K_a: (-1, 0),
        K_d: (1, 0), K_w: (0, -1), K_s: (0, 1)}

    def update(self, event_keys: list) -> None:
        for key in self.keys:
            if event_keys[key]:
                self.body.position += Vec2D(*self.keys[key]) * 2

