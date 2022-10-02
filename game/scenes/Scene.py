from turtle import Vec2D
import pymunk
import pygame
import numpy as np
from game.items.Item import Item
from game.items.actors.Player import Player
from utils.utils import calculate_center, collition_query


class Scene:
    def __init__(self, player: Player) -> None:
        self.item_list: list = []
        self.space: pymunk.Space = pymunk.Space()
        self.space.gravity = (0, 981)
        self.space.add_default_collision_handler()
        self.bg_color: tuple = (39, 185, 245, 0.8)
        self.static_items = pygame.sprite.Group()
        self.player = player
        self.add_item(player)
        self.current_joint = None
        self.is_grabbing = False
        self.can_grab = False
        self.is_jumping = False
        self.grabbing_color = (0, 255, 0)
        self.not_grabbing_color = (255, 0, 0)
        self.mouse_x = None
        self.mouse_y = None


    def pre_loads(self) -> None:
        pass

    def add_item(self, item: Item) -> None:
        self.space.add(item.body, item.shape)
        self.item_list.append(item)
        self.static_items.add(item)

    def update(self, screen: pygame.Surface, pressed_keys: list) -> None:
        # check collition with static items to jump
        if pygame.sprite.spritecollide(self.player, self.static_items, False):
            self.is_jumping = False


        if not self.is_grabbing:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        player_x, player_y = self.player.body.position

        distance = ((self.mouse_x - player_x) ** 2 + (self.mouse_y - player_y) ** 2) ** 0.5
        angle = np.arctan2(self.mouse_y - player_y, self.mouse_x - player_x)


        if distance > 500:
            distance = 500
            self.mouse_x = player_x + distance * np.cos(angle)
            self.mouse_y = player_y + distance * np.sin(angle)
        elif distance < 40:
            distance = 40
            self.mouse_x = player_x + distance * np.cos(angle)
            self.mouse_y = player_y + distance * np.sin(angle)


        if collition_query(self.space, (self.mouse_x, self.mouse_y)):
            self.can_grab = True
        else:
            self.can_grab = False

        if self.is_grabbing:
            distance_grab = ((self.mouse_x - player_x) ** 2 + (self.mouse_y - player_y) ** 2) ** 0.5

            if distance_grab > 50:
                direction_x = player_x + distance * np.cos(angle)
                direction_y = player_y + distance * np.sin(angle)
                self.player.body.velocity = Vec2D(direction_x - player_x, direction_y - player_y) * 2
            elif angle < 0:
                self.player.body.velocity = Vec2D(0, 0)


        pygame.draw.line(screen, self.grabbing_color if self.can_grab else self.not_grabbing_color, (player_x, player_y), (self.mouse_x, self.mouse_y), 5)
        pygame.draw.circle(screen, self.grabbing_color if self.can_grab else self.not_grabbing_color, (self.mouse_x, self.mouse_y), 10)


        for item in self.item_list:
            item.update(pressed_keys)

    def on_event(self, event: pygame.event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.can_grab:
                    self.is_grabbing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_grabbing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.player.body.velocity = Vec2D(0, -500)
                self.is_jumping = True