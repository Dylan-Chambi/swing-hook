from turtle import Vec2D
import numpy
import pymunk
import pygame
from pygame.locals import *
from game.items.Item import Item

class Player(Item):

    def __init__(self, vertices: list, x: int, y: int) -> None:
        super().__init__(vertices, x, y, 0, 0, body_type=pymunk.Body.DYNAMIC, mass=10, elasticity=0, friction=1)
        self.density = 0
        self.velocity_x = 300

    def update(self, event_keys: list) -> None:
        if event_keys[K_a]:
            self.body.velocity = Vec2D(-self.velocity_x, self.body.velocity.y)
        elif event_keys[K_d]:
            self.body.velocity = Vec2D(self.velocity_x, self.body.velocity.y)

