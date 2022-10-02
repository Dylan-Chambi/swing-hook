from math import radians
import pygame
import pymunk.pygame_util
import pymunk
import numpy as np

from game.items.Item import Item

class ItemRect(Item):
    def __init__(self, x: int, y: int, width: int, heigth: int, scale: int = 1, theta = radians(0), body_type: int = pymunk.Body.STATIC, mass: float = 1, elasticity: float = 1.0, friction: float = 1.0) -> None:
        vertices_array = [
            (x + width / 2, y + heigth / 2),
            (x + width / 2, y - heigth / 2),
            (x - width / 2, y - heigth / 2),
            (x - width / 2, y + heigth / 2)
        ]
        if body_type == pymunk.Body.STATIC:
            self.body: pymunk.Body = pymunk.Body(body_type=body_type)
        else:
            self.body: pymunk.Body = pymunk.Body(body_type=body_type, mass=mass, moment=pymunk.moment_for_poly(mass, vertices_array))
        
        super().__init__(vertices_array, x, y, 0, 0, pymunk.Poly.create_box(self.body, (width, heigth)), self.body, scale, theta, body_type, mass, elasticity, friction)
        self.rect = pygame.Rect(x, y, heigth, width)

    def update(self, event_keys: list) -> None:
        super().update(event_keys)
