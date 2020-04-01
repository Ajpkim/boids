import random
from boids import Boid


def initialize_boids(n, angle, width, height):
    """
    Create list of boid objects with random positions within the given width, height
    """
    return [Boid([int(random.random()*width), int(random.random()*height)], angle, width, height)
            for i in range(n)]


def get_pygame_coords(points, height):
    "Convert coordinates to pygame standard, meaning (0,0) at top left"
    return [[p[0], height-p[1]] for p in points]
