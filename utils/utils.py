import numpy
import pymunk

def calculate_center(vertices: list, x: int, y: int) -> tuple:
    x = numpy.array(vertices)[:, 0] + x
    y = numpy.array(vertices)[:, 1] + y
    return (sum(x) / len(vertices), sum(y) / len(vertices))

def collition_query(space: pymunk.Space, point: tuple) -> bool:
    return space.point_query_nearest(point, 0, pymunk.ShapeFilter())