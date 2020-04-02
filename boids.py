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
        Calculate boid coordinates given current position and angle. Boid
        dimensions are a triangle with height=15, base=10. Theta and
        the magnitudes 10, 7.071 that are used to calc points are constants
        given triangle dimensions.

        P1 is "head" of boid and is 10 away from centriod along the angle.

        P2 and P3 are the "tails" which are 7.071 away from centriod along
        (angle +/- theta).
        """
        # 4/2 implementation
        angle = self.angle
        centriod_x = self.position[0]
        centriod_y = self.position[1]
        theta = math.radians(135)
        tail_dist_from_centriod = 7.071

        p1 = (centriod_x + (10 * math.cos(angle)),
              centriod_y + (10 * math.sin(angle)))
        p2 = (centriod_x + (tail_dist_from_centriod * math.cos(angle + theta)),
              centriod_y + (tail_dist_from_centriod * math.sin(angle + theta)))
        p3 = (centriod_x + (tail_dist_from_centriod * math.cos(angle - theta)),
              centriod_y + (tail_dist_from_centriod * math.sin(angle - theta)))

        return [p1, p2, p3]
