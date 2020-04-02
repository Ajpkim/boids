import timeit
import time
import math
import numpy as np
import random
import pygame
from pygame_boids import *
from helper_functions import *
# GlowScript 2.1 VPython
import vpython as vp


# ------ Starting with vpython -----------#
a = vp.vector(0, 0, 0)
print(a.z)

b = vp.vector(5, 6, 7)
c = vp.vector(10, 15, 20)
print(b, c)
d = b + c
print(d)
e = vp.vector(2, 2, 2)
f = e * 3.52
print(f)
g = e.dot(b)
print(g)


# A = vpython.vector(1, 2, 0)
# B = vpython.vector(0, 1, 2)

# Aarr = vpython.arrow(pos=vpython.vector(0, 0, 0), axis=A, color=(255, 0, 0))
# Barr = vpython.arrow(pos=vpython.vector(0, 0, 0), axis=B, color=(0, 255, 0))
# Barr.pos = Aarr.pos+Aarr.axis
#

# vec = pygame.math.Vector2
# help(pygame.math.Vector2)

# help(vp.vector)

# test_flock_offscreen = initialize_boids_off_screen(n, width, height)
# for b in test_flock_offscreen:
#     print("")
#     print(b.position)
#     b.update_position()
#     print(b.position)

# print(random.randrange(-1, 12, 11))

# for i in range(10):
#     flip = random.randint(0, 1)
#     if flip:
#         print(1)
#     else:
#         print(0)

# n = 50
# width = 500
# height = 500
# angle = 0
# position = (100, 125)
# b = Boid(position, angle, width, height)

#
# test_boids = initialize_boids(n, angle, width, height)
# testing_game = game_loop(test_boids, width, height)


# height = 30
# points = [[0, 5], [3, 15], [25, 30]]

# for p in points:
#     print(p[0], height-p[1])
#
#     converted_points = [[p[0], height-p[1]] for p in points]
#     print(converted_points)
# converted_points = [p[p[0], height-p[1]] for p in points]


# single_boid = [Boid(250, 250, 0)]
# game_loop(single_boid, width, height)


# a, b, c = 1, 2, 3
# print(a, b, c)
#
# a, b, c = a+10, b+10, c+10
# print(a, b, c)

# # #Testing tuple coorindate list for drawing   ---> works
# pygame.init()
# win = pygame.display.set_mode((width, height))
# pygame.draw.polygon(win, (0, 255, 0), [(300, 90), (325, 95), (400, 90)], 3)
# pygame.display.update()

# # testing trig function updates... issue was degress v radians
# x = 0
# y = 0
# angle = 45
# b = Boid(x, y, angle)
# angle = b.angle
# print(math.cos(angle+math.pi-18.1))
# print(math.cos(math.pi))
# print(type(math.pi))
# print('angle =', angle)
# print('x = {}, y = {}'.format(x, y))
# b = Boid(x, y, angle)
# for i in range(10):
#     b.update()
#     print('x = {}, y = {}'.format(b.x, b.y))

# boids = initialize_boids(5, 10, 10)
#
# print(boids)
# for boid in boids:
#     print(boid.position)
# help(pygame.draw.circle)

# lambda practice
# print((lambda x, y: [x * random.random(), y * random.random()])(width, height))
# print((lambda x, y: [x * random.random(), y * random.random()])(width, height))
# (lambda x, y: [x * random.random(), y * random.random()])(width, height)

# (lambda x=width, y=height: x * random.random(), y * random.random())
# get_head = lambda x, y: [x * random.random(), y * random.random())
#
# head_points = get_head(width, height)
# print(head_points)

# points = [(lambda x, y: [x * random.random(), y * random.random()), (width, height) for i in range(5)]
# print(points)
# print((lambda x: x * random.random())(width))
# (lambda x, y: x * random.random(), y * random.random())(width, height)

# [lambda x, y: [x * random.random(), y * random.random()], (width, height)

# cube = lambda x: x**3
# cube(4)

# test = game_loop(n, width, height)
# help(pygame.rect)
# help(pygame.draw.polygon)

# # NUMPY IS SLOW
# print(timeit.timeit("""import numpy as np
# a = [np.random.rand(2) * 1000 for i in range(100)]""", number=10000))
# # --> 2.257 sec
# print(timeit.timeit("""import random
# a = [(random.random() * 1000, random.random() * 1000) for i in range(100)]""", number=10000))
# # 0.369 sec
