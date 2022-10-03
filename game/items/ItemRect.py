from math import radians
import pygame
# import pymunk.pygame_util
# import pymunk

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
            self.surf = img
            self.surf = pygame.transform.scale(self.surf, (width, heigth))
            self.rect = self.surf.get_rect(center=(x, y))
        else:
            self.surf = pygame.Surface((width, heigth))
            self.surf.fill(self.bg_color)
            self.rect = self.surf.get_rect(center=(x, y))
        
        # self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.rect.center = (x, y)
        self.initial_x = self.rect.x
        self.initial_y = self.rect.y

    def update(self, event_keys: list, scene):
        super().update(event_keys)

    def draw_in_screen(self) -> None:
        screen = pygame.display.get_surface()
        screen.blit(self.surf, self.rect)