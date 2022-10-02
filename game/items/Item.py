from math import radians
import pygame
# import pymunk.pygame_util
# import pymunk
import numpy as np

from pygame.sprite import Sprite

class Item(Sprite):
    def __init__(self, vertices: list, x: int, y: int, vx: float, vy: float, scale: int = 1, theta = radians(0), bg_color: tuple = (0, 100, 255)) -> None:
        super().__init__()
        self.vertices: list = vertices
        # self.body: pymunk.Body  = body
        # self.body.position: tuple = x, y
        # self.body.velocity: tuple = vx, vy
        # self.body.angular_velocity: float = 0
        # self.body.angle: float = theta
        self.theta: float = theta
        # self.shape: pymunk.Shape = shape
        # self.shape.elasticity = elasticity
        # self.shape.friction = friction
        # self.shape.collision_type = 2
        self.item_scale_x: float = scale
        self.item_scale_y: float = scale
        self.bg_color: tuple = bg_color

    def transform(self, t_matrix: list) -> None:
        vert_list = [[v[0], v[1], 1] for v in self.vertices] 
        vert_matrix = np.transpose(np.array(vert_list))
        new_matrix = np.transpose(np.dot(t_matrix, vert_matrix))
        new_vertices = [(v[0], v[1]) for v in new_matrix]
        self.vertices = new_vertices
        # self.shape = pymunk.Poly(self.body, self.vertices)

    def rotate(self, angle: float) -> None:
        rotate_matrix = [[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]]
        # self.theta += angle
        self.transform(rotate_matrix)    
    
    def scale(self, scale_x: float, scale_y: float = None) -> None:
        scale_matrix = [[scale_x, 0, 0], [0, scale_y, 0], [0, 0, 1]]
        self.item_scale_x *= scale_x
        self.item_scale_y *= scale_y
        self.transform(scale_matrix)

    def translate(self, x: int, y: int) -> None:
        translate_matrix = [[1, 0, x], [0, 1, y], [0, 0, 1]]
        # self.body.position = x, y # TODO: Check if this is correct
        self.transform(translate_matrix)
    
    def reflect(self, reflect_y: bool, reflect_x: bool) -> None:
        reflect_matrix = [[-1 if reflect_x else 1, 0, 0], [0, -1 if reflect_y else 1, 0], [0, 0, 1]]
        self.transform(reflect_matrix)

    def update(self, event_keys: list) -> None:
        pass

    def draw_in_screen(self, screen: pygame.Surface) -> None:
        pass