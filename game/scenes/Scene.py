import pymunk
import pygame

from game.items.Item import Item

class Scene:
    def __init__(self) -> None:
        self.space: pymunk.Space = pymunk.Space()
        self.bg_color: tuple = (39, 185, 245, 0.8)

    def addItem(self, item: Item) -> None:
        self.space.add(item.body, item.shape)

    def update(self, keys: list) -> None:
        pass