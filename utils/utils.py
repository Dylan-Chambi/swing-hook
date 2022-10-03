import numpy
import pygame
from game.items.ItemRect import ItemRect

def calculate_center(vertices: list, x: int, y: int) -> tuple:
    x = numpy.array(vertices)[:, 0] + x
    y = numpy.array(vertices)[:, 1] + y
    return (sum(x) / len(vertices), sum(y) / len(vertices))

def collition_query(static_items: list, point: tuple) -> bool:
    for item in static_items:
        if item.rect.collidepoint(point):
            return True
    return False

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)