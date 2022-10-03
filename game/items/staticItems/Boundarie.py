from math import radians
import pygame
# import pymunk.pygame_util
# import pymunk

from game.items.Item import Item
from game.items.ItemRect import ItemRect

class Boundarie(ItemRect):
    def __init__(self, x: int, y: int, width: int, heigth: int, bg_color: tuple = (100, 100, 100), img: pygame.Surface = None) -> None:
        super().__init__(x, y, width, heigth, bg_color=bg_color, img=img)
    
    def draw_in_screen(self, screen: pygame.Surface) -> None:
        screen.blit(self.img, self.rect)
