import timeit
import time
import random
import numpy as np
import math

# n = 1_000_000
# width = 500
# height = 500
# start = time.perf_counter()
#
# x = -1
# y = 2
# for i in range(n):
#     # angle = math.atan2(x, y)
#     angle = math.atan(y/x)
#     if x < 0:
#         angle = + 180
# #
# end = time.perf_counter()
#
# print('seconds:', end-start)


# for i in range(n):
#     a = np.array([4, 7])
#     b = math.sqrt(a[0]**2 + a[1]**2)  # about twice as fast
# b = np.linalg.norm(a)


# number = 10000
# #
# for i in range(n):
#     arr = np.array([random.random() * width, random.random() * height])
# arr = np.zeros([2])
# a = np.array([0, 0])
# a = np.array([random.randint(0, width), random.randint(0, height)])
# n = 2_560_000
#
# start = time.perf_counter()
# test1 = [[0.0, 0.0] for i in range(n)]
# end = time.perf_counter()
#
# print('creating {} 2d arrays with lc: {} seconds'.format(n, end-start))
# print("")
#
# start = time.perf_counter()
#
#
# def test_np_with_foo():
#     for i in range(n):
#         a = np.zeros([2])
#
#
# # test2 = np.zeros([2, n])
# test2 = test_np_with_foo()
#
# end = time.perf_counter()
#
#
# print('creating {} 2d arrays with np.zeroes(): {} seconds with np.array'.format(n, end-start))

# ######## np MUCH faster at initializing large number of 2d arrays
# ######## np.zeroes MUCH MUCH MUCH faster at initializing large number of 2d arrays
# ---->>>>> doing it with list comprehension is way faster than iterating


# print('testing for loop version:', timeit.timeit("""
# import random
# points = [[random.randint(0, 500), random.randint(0, 500)] for i in range(100)]
# height = 500
#
# def get_pygame_coords(points, height):
#     "Convert coordinates to pygame standard, meaning (0,0) at top left"
#     converted_points = []
#     for point in points:
#         adj_y = height - point[1]
#         converted_points.append([point[0], adj_y])
#     return converted_points
#
# coordinates = get_pygame_coords(points, height)
# """, number=number))
# --> 1000 trials, ~3.3 seconds
# --> 5000 trials, ~18.3 seconds


# print('testing list comp:', timeit.timeit("""
# import random
# points = [[random.randint(0, 500), random.randint(0, 500)] for i in range(100)]
# height = 500
# def list_comp(points, height):
#     return [[p[0], height-p[1]] for p in points]
#
# coorindate = list_comp(points, height)
# """, number=number))
# --> 1000 trials, ~3.7 seconds
# --> 5000 trials, ~17.5 seconds


# def list_comp(points, height):
#     return [[p[0], height-p[1]] for p in points]


# points = [[random.randint(0, 500), random.randint(0, 500)] for i in range(1000)]
# height = 500


# def get_pygame_coords(points, height):
#     "Convert coordinates to pygame standard, meaning (0,0) at top left"
#
#     converted_points = []
#     for point in points:
#         adj_y = height - point[1]
#         converted_points.append([point[0], adj_y])
#     return converted_points
