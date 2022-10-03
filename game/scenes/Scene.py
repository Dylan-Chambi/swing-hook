from turtle import Vec2D
import pygame
import numpy as np
from game.items.Item import Item
from game.items.actors.Player import Player
from utils.utils import calculate_center, collition_query


class Scene:
    def __init__(self) -> None:
        self.item_list: list = []
        self.bg_color: tuple = (39, 185, 245, 0.8)
        self.grabbable_items = pygame.sprite.Group()
        self.dangerous_items = pygame.sprite.Group()
        self.static_items = pygame.sprite.Group()
        self.players = pygame.sprite.Group()


    def pre_loads(self) -> None:
        pass

    def add_grabbable_item(self, item: Item) -> None:
        self.item_list.insert(0, item)
        self.grabbable_items.add(item)
    
    def add_dangerous_item(self, item: Item) -> None:
        self.item_list.insert(0, item)
        self.dangerous_items.add(item)
    
    def add_static_item(self, item: Item) -> None:
        self.item_list.insert(0, item)
        self.static_items.add(item)

    def add_player(self, player: Player) -> None:
        self.item_list.insert(-1, player)
        self.static_items.add(player)
        self.players.add(player)

    def update(self, screen: pygame.Surface, pressed_keys: list) -> None:
        for item in self.item_list:
            item.draw_in_screen(screen)
            item.update(pressed_keys, self.grabbable_items, self.dangerous_items, self.static_items, screen)



    def on_event(self, event: pygame.event) -> None:
        for player in self.players:
            player.on_event(event)