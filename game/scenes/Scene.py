from turtle import Vec2D
import pygame
import numpy as np
from game.items.Item import Item
from game.items.actors.Player import Player
from utils.utils import calculate_center, collition_query


class Scene:
    def __init__(self, player: Player) -> None:
        self.item_list: list = []
        # self.space: pymunk.Space = pymunk.Space()
        # self.space.gravity = (0, 981)
        # self.space.add_default_collision_handler()
        self.bg_color: tuple = (39, 185, 245, 0.8)
        self.static_items = pygame.sprite.Group()
        self.player = player
        self.add_item(player)


    def pre_loads(self) -> None:
        pass

    def add_item(self, item: Item) -> None:
        # self.space.add(item.body, item.shape)
        self.item_list.append(item)
        self.static_items.add(item)

    def update(self, screen: pygame.Surface, pressed_keys: list) -> None: 
        # check collition with static items to jump
        # if pygame.sprite.spritecollide(self.player, self.static_items, False):
        #     self.is_jumping = False
        for item in self.item_list:
            item.draw_in_screen(screen)
            item.update(pressed_keys, self.static_items, screen)



    def on_event(self, event: pygame.event) -> None:
        self.player.on_event(event)