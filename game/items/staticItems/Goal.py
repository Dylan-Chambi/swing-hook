from math import radians
import pygame

from game.items.Item import Item
from game.items.ItemRect import ItemRect


class Goal(ItemRect):
    def __init__(self, x: int, y: int, width: int, heigth: int, bg_color: tuple = (255, 150, 100), img: pygame.Surface = None):
        super().__init__(x, y, width, heigth, bg_color=bg_color, img=img)