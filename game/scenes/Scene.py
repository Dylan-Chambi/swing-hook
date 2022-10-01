import pymunk
import pygame

from game.items.Item import Item
from game.items.actors.Player import Player
from utils.utils import calculate_center

class Scene:
    def __init__(self, player: Player) -> None:
        self.item_list: list = []
        self.space: pymunk.Space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.space.add_default_collision_handler()
        self.bg_color: tuple = (39, 185, 245, 0.8)
        self.player = player
        self.add_item(player)


    def pre_loads(self) -> None:
        pygame.mouse.set_visible(False)

    def add_item(self, item: Item) -> None:
        self.space.add(item.body, item.shape)
        self.item_list.append(item)

    def update(self, screen: pygame.Surface, event_keys: list) -> None:
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)
        xp, yp = calculate_center(self.player.vertices, self.player.body.position.x, self.player.body.position.y)

        pygame.draw.line(screen, (255, 0, 0), (xp, yp), (x, y), 2)

        for item in self.item_list:
            item.update(event_keys)