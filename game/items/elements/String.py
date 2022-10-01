import numpy
import pygame
import pymunk
from game.items.Item import Item

class String():
    def __init__(self, item: Item, attachment: tuple) -> None:
        self.item = item
        self.attachment = attachment


    def update(self, screen: pygame.Surface, event_keys: list) -> None:
        pygame.draw.line(screen, (255, 0, 0), self.attachment, self.item.body.position, 5)