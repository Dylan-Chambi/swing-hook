from turtle import Vec2D
import numpy
# import pymunk
import pygame
import numpy as np
from game.constants import DT
from pygame.locals import *
from game.items.Item import Item
from game.items.ItemRect import ItemRect

from utils.utils import collition_query


class Player(ItemRect):

    def __init__(self, x: int, y: int, width: int, heigth: int, bg_color: tuple = (0, 255, 255)) -> None:
        super().__init__(x, y, width, heigth,bg_color=bg_color)
        self.density = 0
        self.velocity_x = 5
        self.force_y = 0
        self.is_jumping = False
        self.dx = 0
        self.dy = 0
        self.is_grabbing = False
        self.can_grab = False
        self.grabbing_color = (0, 255, 0)
        self.not_grabbing_color = (255, 0, 0)
        self.mouse_x = None
        self.mouse_y = None
        self.initial_x = x
        self.initial_y = y

    def update(self, event_keys: list, grabbable_items: list, dangerous_items: list, static_items: list, screen: pygame.Surface) -> None:
        super().update(event_keys, grabbable_items, dangerous_items, static_items, screen)

        self.dx = 0
        self.dy = 0

        if event_keys[K_a]:
            self.dx -= (self.velocity_x)
        if event_keys[K_d]:
            self.dx += (self.velocity_x)
        if event_keys[K_SPACE] and not self.is_jumping and not self.is_grabbing:
            self.is_jumping = True
            self.force_y = -18

        self.force_y += 1 
        if self.force_y > 10:
            self.force_y = 10
        self.dy += self.force_y

        
        self.grapple_handler(grabbable_items, screen)

        self.check_collision(grabbable_items, dangerous_items, static_items)



        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.bottom > 1080:
            self.rect.bottom = 1080
            self.dy = 0
        if self.rect.top < 0:
            print("Player is out of screen")

    def on_event(self, event: pygame.event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.can_grab:
                    self.is_grabbing = True
                    self.is_jumping = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_grabbing = False

    def check_collision(self, grabbable_items: list, dangerous_items: list, static_items: list) -> None:
        for item in dangerous_items:
            if self.rect.colliderect(item.rect):
                self.rect.x = self.initial_x
                self.rect.y = self.initial_y
                self.dx = 0
                self.dy = 0
                self.is_jumping = False
                self.force_y = 0
                self.is_grabbing = False
                self.can_grab = False
            
        new_list = []

        for item in static_items:
            if item != self:
                new_list.append(item)
        for item in grabbable_items:
            new_list.append(item)
        

        for item in new_list:
            if item != self:
                if item.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.rect.width, self.rect.height):
                    self.dx = 0

                if item.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.rect.width, self.rect.height):
                    if self.force_y > 0:
                        self.is_jumping = False
                    elif self.force_y < 0:
                        self.is_jumping = True
                    else :
                        self.is_jumping = False
                    self.force_y = 0
                    self.dy = 0

    def grapple_handler(self, grabbable_items: list, screen: pygame.Surface) -> None:
        if not self.is_grabbing:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        player_x, player_y = self.rect.centerx, self.rect.centery

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


        if collition_query(grabbable_items, (self.mouse_x, self.mouse_y)):
            self.can_grab = True
        else:
            self.can_grab = False

        if self.is_grabbing:
            distance_grab = ((self.mouse_x - player_x) ** 2 + (self.mouse_y - player_y) ** 2) ** 0.5

            if distance_grab > 30:
                direction_x = self.velocity_x * np.cos(angle)
                direction_y = self.velocity_x * np.sin(angle)
                self.dx += (direction_x) + (np.cos(angle) * self.force_y)
                self.dy += (direction_y) - self.force_y * 0.8
                


        pygame.draw.line(screen, self.grabbing_color if self.can_grab else self.not_grabbing_color, (player_x, player_y), (self.mouse_x, self.mouse_y), 5)
        pygame.draw.circle(screen, self.grabbing_color if self.can_grab else self.not_grabbing_color, (self.mouse_x, self.mouse_y), 10)