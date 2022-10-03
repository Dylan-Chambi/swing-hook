from math import radians
import pygame
# import pymunk.pygame_util
# import pymunk
import numpy as np

from game.items.Item import Item

class ItemRect(Item):
    def __init__(self, x: int, y: int, width: int, heigth: int, scale: int = 1, theta = radians(0), bg_color: tuple = (0, 100, 255)) -> None:
        vertices_array = [
            (x + width / 2, y + heigth / 2),
            (x + width / 2, y - heigth / 2),
            (x - width / 2, y - heigth / 2),
            (x - width / 2, y + heigth / 2)
        ]
        
        super().__init__(vertices_array, x, y, 0, 0, scale, theta, bg_color=bg_color)

        self.surf = pygame.Surface((width, heigth))
        self.surf.fill(self.bg_color)
        self.rect = self.surf.get_rect(center=(x, y))
        self.initial_x = self.rect.x
        self.initial_y = self.rect.y

    def update(self, event_keys: list, grabbable_items: list, danger_items: list, static_items: list, screen: pygame.Surface) -> None:
        super().update(event_keys)

    def draw_in_screen(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.bg_color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height))