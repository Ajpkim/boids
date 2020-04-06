import timeit
import time
import math
import numpy as np
import random
from initializers import *
import pygame
from flock import Flock
from pygame_boids import *
from helper_functions import *
# #import vpython as vp


# a = Boid(np.array([3, 4]), 10, 10)
# b = Boid(np.array([4, 4]), 10, 10)
# f = [a, b]
# af = a.find_flockmates(f)
# print('a', a)
# print('flockmate', af)
# print('align_vec', a.calc_align_force(af))


# print(a, b)

# a = np.array([5, 5])
# print(np.linalg.norm(a))
# print(set_mag(a, 15))


# flock = Flock(5, 50, 50)
# print(flock)
# for b in flock.boids:
#     print(b)
# for i in range(10):
#     print("")
#     print('steering forces:', flock.calc_steering_forces())
#     flock.update_positions()
#     for b in flock.boids:
#         print(b)


# a = np.array([3, 5])
# b = a * 3
# print(type(b))


# flock = initialize_random_boids(10, 100, 100)
# # print(flock)
#
# for b in flock:
#     print('')
#     print(b)
#     print(b.find_flockmates(flock))

# b = Boid(np.array([2, 3]), 120, 250, 250)
# print(b)

#
# a = np.array([2.0, 4.0])
# a /= 2
# print(a)


# x = -1
# y = -2
# print(math.degrees(math.atan2(x, y)))


#
# a = np.array([20.1, 30.1])
# print(np.linalg.norm(a))
# print(a/np.linalg.norm(a))
#
# while np.linalg.norm(a) > 10:
#     a -= (a/np.linalg.norm(a))
#     print(a)
#
# print('done:', a)


# a = np.array([5, 10])
# b = math.atan(a[0]/a[1])
# print(math.degrees(b))

# print(math.atan(math.pi))
# print(math.tan(math.pi))
# help(math.atan2)

# help(pygame.display.set_mode)
# a = np.array([random.random(), random.random()])
# print(a)
# a[0] += 5
# print(type(a))
#
# a[0], a[1] = 5, 9
# print(a)
# print(type(a))
# b = Boid(np.array([50, 60.1]), 90, 500, 500)
# print(b.position)
# print(b.points)
# print("")
# print(b.x)
# print(b.y)
# print(b.velocity)
# print("")
# print(type(b.position))
# print(type(b.velocity))
#
# print(b.update_position())
# print(b.position)
# print(b.points)
# print(b.x)
# print(b.y)


# n = 5
# width = 500
# height = 500
# vec = np.array([5, 10])
# angle = random.random() * 360
# b = Boid(vec, angle, width, height)
# print(b.points)s


# a = np.array([1, 2])
# b = [4, 5]
# print(type(a+b))


# flock = initialize_random_boids(n, width, height)
# print(flock)
#
# # print(np.mag(flock[0].velocity))
# b0 = flock[0]
#
# print(np.linalg.norm(b0.velocity))
# flock = initialize_boids(n, width, height, np.array([5, 5]))

# ------ Starting with vpython -----------#
# a = vp.vector(0, 0, 0)
# print(a.z)
#
# b = vp.vector(5, 6, 7)
# c = vp.vector(10, 15, 20)
# print(b, c)
# d = b + c
# print(d)
# e = vp.vector(2, 2, 2)
# f = e * 3.52
# print(f)
# g = e.dot(b)
# print(g)


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
