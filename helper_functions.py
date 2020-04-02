import random
from boids import Boid


def get_pygame_coords(points, height):
    "Convert coordinates to pygame standard, meaning (0,0) at top left"
    return [[p[0], height-p[1]] for p in points]


def initialize_boids(n, width, height):
    """
    Create list of boid objects with random positions within the given width, height
    """
    return [Boid([(random.randint(0, width)), (random.randint(0, height))], random.randint(0, 360), width, height)
            for i in range(n)]


def initialize_boids_from_position(n, position, width, height):
    return [Boid(position, random.randint(0, 360), width, height)
            for i in range(n)]

#
# def initialize_boids_off_screen(n, width, height):
#     "DNU, doesnt work bc of boid autorepositioning"
#     boids = []
#     for i in range(n):
#         vertical = random.randint(0, 1)
#
#         if vertical:
#             x = random.randint(0, width)
#             up = random.randint(0, 1)
#             if up:
#                 y = random.randint(height+1, height*2)
#             else:
#                 y = random.randint(-height, -1)
#
#         else:
#             y = random.randint(0, height)
#             left = random.randint(0, 1)
#             if left:
#                 x = random.randint(-width, -1)
#             else:
#                 x = random.randint(width+1, width*2)
#
#         b = Boid([x, y], random.randint(0, 360), width, height)
#         boids.append(b)
#
#     return boids
