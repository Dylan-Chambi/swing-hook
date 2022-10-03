from math import radians
import pygame
# import pymunk.pygame_util
# import pymunk
import numpy as np

from game.items.Item import Item

class ItemRect(Item):
    def __init__(self, x: int, y: int, width: int, heigth: int, scale: int = 1, theta = radians(0), bg_color: tuple = (0, 100, 255)) -> None:
        vertices_array = [
            (x + width / 2, y + heigth / 2),
            (x + width / 2, y - heigth / 2),
            (x - width / 2, y - heigth / 2),
            (x - width / 2, y + heigth / 2)
        ]
        # if body_type == pymunk.Body.STATIC:
        #     self.body: pymunk.Body = pymunk.Body(body_type=body_type)
        # else:
        #     self.body: pymunk.Body = pymunk.Body(body_type=body_type, mass=mass, moment=pymunk.moment_for_poly(mass, vertices_array))
        
        super().__init__(vertices_array, x, y, 0, 0, scale, theta, bg_color=bg_color)

        self.surf = pygame.Surface((width, heigth))
        self.surf.fill(self.bg_color)
        self.rect = self.surf.get_rect(center=(x, y))
        # self.rect.center = self.body.position

    def update(self, event_keys: list, static_items: list) -> None:
        super().update(event_keys)
        # self.body.angle = self.theta
        # self.rect.center = self.body.position

    def draw_in_screen(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.bg_color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        # pygame.draw.circle(screen, (255, 0, 0), (int(self.rect.left), int(self.rect.top)), 5)
        # pygame.draw.rect(screen, (0, 0, 0), (self.rect.left, self.rect.top, self.rect.width, self.rect.height), 1)


    # def transform(self, t_matrix: list) -> None:
    #     vert_list = [[v[0], v[1], 1] for v in self.vertices] 
    #     vert_matrix = np.transpose(np.array(vert_list))
    #     new_matrix = np.transpose(np.dot(t_matrix, vert_matrix))
    #     new_vertices = [(v[0], v[1]) for v in new_matrix]
    #     self.vertices = new_vertices
    #     self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))