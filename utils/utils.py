import numpy
import pygame
import sys
import os
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
    return pygame.font.Font(get_assets_path("assets/font.ttf"), size)

def get_assets_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)