import timeit
import time
import math
import numpy as np
import random
import pygame
from pygame_boids import *
from helper_functions import *

# features:
# - hovering mouse that repels like a predator
# - sliders for the force of the 3 rules
# - handle movement and positioning with transformation matrices?
# allow for custom starting positions


# ToDo
- decide on vector representation, vpython or create own basic vector class
- adjust Boid rep to use vectors
- Implement rules


n = 25
width = 500
height = 500
position = (100, 125)
delay = 25
position = [250, 250]
# angle = 0  # changed to random
# b = Boid(position, angle, width, height)

# test_flock_from_position = initialize_boids_from_position(n, position, width, height)
# game_loop(test_flock_from_position, width, height, delay)

test_flock = initialize_boids(n, width, height)
game_loop(test_flock, width, height, delay)
