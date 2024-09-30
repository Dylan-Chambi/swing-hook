# import pymunk
import math
import pygame
from game.constants import DT, WIN_EVENT
from pygame.locals import *
from game.items.Item import Item
from game.items.ItemRect import ItemRect

from utils.utils import collition_query, get_assets_path

from game.constants import LOSE_EVENT


class Player(ItemRect):

    def __init__(self, x: int, y: int, width: int, heigth: int, bg_color: tuple = (0, 255, 255), img: pygame.Surface = None):
        super().__init__(x, y, width, heigth, bg_color=bg_color, img=img)
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
        self.lives = 3
        self.orientation = "right"
        self.jump_sound = pygame.mixer.Sound(
            get_assets_path("assets/sounds/jump.ogg"))
        self.grapple_sound = pygame.mixer.Sound(
            get_assets_path("assets/sounds/grapple.ogg"))
        self.die_sound = pygame.mixer.Sound(
            get_assets_path("assets/sounds/die.ogg"))

    def draw_in_screen(self) -> None:
        screen = pygame.display.get_surface()
        if self.orientation == "right":
            screen.blit(pygame.transform.flip(
                self.surf, True, False), (self.rect.x, self.rect.y))
        elif self.orientation == "left":
            screen.blit(self.surf, (self.rect.x, self.rect.y))

    def update(self, event_keys: list, scene):
        super().update(event_keys, scene)

        self.dx = 0
        self.dy = 0

        if event_keys[K_a]:
            self.dx -= (self.velocity_x)
            self.orientation = "left"
        if event_keys[K_d]:
            self.dx += (self.velocity_x)
            self.orientation = "right"
        if event_keys[K_SPACE] and not self.is_jumping and not self.is_grabbing:
            self.is_jumping = True
            self.force_y = -18
            self.jump_sound.play()

        self.force_y += 1
        if self.force_y > 10:
            self.force_y = 10
        self.dy += self.force_y

        self.grapple_handler(scene.grabbable_items)

        self.check_collision(
            scene.grabbable_items, scene.dangerous_items, scene.static_items, scene.goal)

        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.bottom > 1080:
            self.rect.bottom = 1080
            self.dy = 0
        if self.rect.top < 0:
            print("Player is out of screen")

        if self.rect.left < 0:
            self.rect.left = 0
            self.dx = 0

    def on_event(self, event: pygame.event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.can_grab:
                    self.is_grabbing = True
                    self.is_jumping = True
                    self.grapple_sound.play()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_grabbing = False

    def check_collision(self, grabbable_items: list, dangerous_items: list, static_items: list, goal: ItemRect) -> None:
        for item in dangerous_items:
            if self.rect.colliderect(item.rect):
                self.lives -= 1
                if self.lives >= 0:
                    self.die_sound.play()
                if self.lives < 0:
                    pygame.event.post(pygame.event.Event(LOSE_EVENT))
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
                    else:
                        self.is_jumping = False
                    self.jump_sound.stop()
                    self.force_y = 0
                    self.dy = 0

        if goal.rect.colliderect(self.rect):
            pygame.event.post(pygame.event.Event(WIN_EVENT))

    def grapple_handler(self, grabbable_items: list) -> None:
        screen = pygame.display.get_surface()
        if not self.is_grabbing:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        player_x, player_y = self.rect.centerx, self.rect.centery

        distance = ((self.mouse_x - player_x) ** 2 +
                    (self.mouse_y - player_y) ** 2) ** 0.5
        angle = math.atan2(self.mouse_y - player_y, self.mouse_x - player_x)

        if distance > 400:
            distance = 400
            self.mouse_x = player_x + distance * math.cos(angle)
            self.mouse_y = player_y + distance * math.sin(angle)
        elif distance < 40:
            distance = 40
            self.mouse_x = player_x + distance * math.cos(angle)
            self.mouse_y = player_y + distance * math.sin(angle)

        if collition_query(grabbable_items, (self.mouse_x, self.mouse_y)):
            self.can_grab = True
        else:
            self.can_grab = False

        if self.is_grabbing:
            distance_grab = ((self.mouse_x - player_x) ** 2 +
                             (self.mouse_y - player_y) ** 2) ** 0.5

            if distance_grab > 30:
                direction_x = self.velocity_x * math.cos(angle)
                direction_y = self.velocity_x * math.sin(angle)
                self.dx += (direction_x) + (math.cos(angle) * self.force_y)
                self.dy += (direction_y) - self.force_y * 0.8

        pygame.draw.line(screen, self.grabbing_color if self.can_grab else self.not_grabbing_color,
                         (player_x, player_y), (self.mouse_x, self.mouse_y), 5)
        pygame.draw.circle(
            screen, self.grabbing_color if self.can_grab else self.not_grabbing_color, (self.mouse_x, self.mouse_y), 10)
