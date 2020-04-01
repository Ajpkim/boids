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

n = 50
width = 500
height = 500
angle = 0
position = (100, 125)
delay = 50
# b = Boid(position, angle, width, height)


test_flock = initialize_boids(n, angle, width, height)
testing_game = game_loop(test_flock, width, height, delay)
