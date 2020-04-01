import timeit
import random
number = 10000

print('testing for loop version:', timeit.timeit("""
import random
points = [[random.randint(0, 500), random.randint(0, 500)] for i in range(100)]
height = 500

def get_pygame_coords(points, height):
    "Convert coordinates to pygame standard, meaning (0,0) at top left"
    converted_points = []
    for point in points:
        adj_y = height - point[1]
        converted_points.append([point[0], adj_y])
    return converted_points

coordinates = get_pygame_coords(points, height)
""", number=number))
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
