import random
import math
import numpy as np


def get_pygame_coords(points, height):
    "Convert coordinates to pygame standard, meaning (0,0) at top left"
    return [[p[0], height-p[1]] for p in points]


def set_mag(vec, mag):
    "set the magnitude of a vector"
    v_hat = vec / math.sqrt(vec[0]**2 + vec[1]**2)
    return v_hat * mag


def limit_mag(vec, limit):
    "ensure vector magnitude is equal to or less than limit"
    if math.sqrt(vec[0]**2 + vec[1]**2) > limit:
        return set_mag(vec, limit)
    return vec


def euclidean_dist_2d(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)


if __name__ == '__main__':
    pass
