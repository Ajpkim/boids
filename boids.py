import pygame
import random
import math
import numpy as np


class Boid(pygame.sprite.Sprite):

    def __init__(self, position, angle, max_x, max_y):
        pygame.sprite.Sprite.__init__(self)  # we'll see if I keep boid as sprite
        self._position = position
        self.x = position[0]
        self.y = position[1]
        self.angle = math.radians(angle)
        self.velocity = 6
        self.acceleration = 2
        self.max_x = max_x  # feels wierd storing this info within the Boid class
        self.max_y = max_y
        self.points = self.calc_points()  # relies on self.max_x, self.max_y

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        "Update self.points, self.x, and self.y when setting position"
        self._position = position
        self.x = position[0]
        self.y = position[1]
        self.points = self.calc_points()

    def update_position(self):
        # going to build on this function when adding boid behavior rules

        x = self.position[0] + int(math.cos(self.angle)*self.velocity)
        y = self.position[1] + int(math.sin(self.angle)*self.velocity)

        if x < 0:
            x = x + self.max_x
        if x > self.max_x:
            x = x - self.max_x

        if y < 0:
            y = y + self.max_y
        if y > self.max_y:
            y = y - self.max_y

        self.position = [x, y]

    def calc_points(self):
        """
        Update points whenever position is updated and make the boids wrap
        around window instead of fly off-screen. Magnitide is the distance from
        self.position to the other 2 points of triangle. pi +/- Theta is the angle
        the long sides of the triangle form from self.position. Both are
        constants used to calculate boid shape.
        """

        magnitide = 15.81139  # size of long side of triangle
        theta = math.radians(18.435)  # angle formed by midline and long sides

        p2x = self.position[0] + magnitide * (math.cos(self.angle + math.pi - theta))
        p2y = self.position[1] + magnitide * (math.sin(self.angle + math.pi - theta))

        p3x = self.position[0] + magnitide * (math.cos(self.angle + math.pi + theta))
        p3y = self.position[1] + magnitide * (math.sin(self.angle + math.pi + theta))

        return [self.position, (p2x, p2y), (p3x, p3y)]  # storing as tuples for speed?

        # # don't think I need to compute for every point, just position point
        # if p1x or p2x or p3x < 0:
        #     p1x, p2x, p3x = p1x+self.max_x, p2x+self.max_x, p3x+self.max_x
        # if p1x or p2x or p3x > self.max_x:
        #     p1x, p2x, p3x = p1x-self.max_x, p2x-self.max_x, p3x-self.max_x
        #
        # if p1y or p2y or p3y < 0:
        #     p1y, p2y, p3y = p1y+self.max_y, p2y+self.max_y, p3y+self.max_y
        # if p1y or p2y or p3y > self.max_y:
        #     p1y, p2y, p3y = p1y-self.max_y, p2y-self.max_y, p3y-self.max_y
        #

        # points = [self.position, [int(p2x), int(p2y)], [int(p3x), int(p3y)]]

        # Make boids wrap around window instead of fly off-screen
        # for p in points:
        #     if p[0] < 0:
        #         p[0] = p[0] + self.max_x
        #     if p[0] > self.max_x:
        #         p[0] = p[0] - self.max_x
        #
        #     if p[1] < 0:
        #         p[1] = p[1] + self.max_y
        #     if p[1] > self.max_y:
        #         p[1] = p[1] - self.max_y
