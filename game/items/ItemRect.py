from math import radians
import pygame
# import pymunk.pygame_util
# import pymunk
import numpy as np

from game.items.Item import Item

class ItemRect(Item):
    def __init__(self, x: int, y: int, width: int, heigth: int, scale: int = 1, theta = radians(0), bg_color: tuple = (0, 100, 255), img: pygame.Surface = None) -> None:
        vertices_array = [
            (x + width / 2, y + heigth / 2),
            (x + width / 2, y - heigth / 2),
            (x - width / 2, y - heigth / 2),
            (x - width / 2, y + heigth / 2)
        ]
        
        super().__init__(vertices_array, x, y, 0, 0, scale, theta, bg_color=bg_color)
        if img is not None:
            self.img = pygame.transform.scale(img, (width, heigth))
            self.rect = self.img.get_rect(center=(x, y))
        else:
            self.img = None
            self.surf = pygame.Surface((width, heigth))
            self.surf.fill(self.bg_color)
            self.rect = self.surf.get_rect(center=(x, y))
        self.rect.center = (x, y)
        self.initial_x = self.rect.x
        self.initial_y = self.rect.y

    def update(self, event_keys: list, scene):
        super().update(event_keys)

    def draw_in_screen(self) -> None:
        screen = pygame.display.get_surface()
        if self.img is not None:
            screen.blit(self.img, self.rect)
        else:
            screen.blit(self.surf, self.rect)