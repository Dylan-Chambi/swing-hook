from math import radians
import pygame

from game.items.Item import Item
from game.items.ItemRect import ItemRect


class Spike(ItemRect):
    def __init__(self, x: int, y: int, width: int, heigth: int, bg_color: tuple = (255, 150, 100)) -> None:
        super().__init__(x, y, width, heigth, bg_color=bg_color)

    # def update(self, event_keys: list, static_items: list, screen: pygame.Surface) -> None:
    #     # super().update(event_keys, static_items)
    #     pass

    def draw_in_screen(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.bg_color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height))