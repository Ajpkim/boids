import pygame
import random
import math
import numpy as np
from helper_functions import *


class Boid():
    """
    ToDo
    """

    def __init__(self, position, max_x, max_y):
        # Adjustables:
        self.perception_radius = 40
        self.max_speed = 9
        self.max_force = .3

        # sliders for weighting behaviors
        self.separation_weight = .6
        self.alignment_weight = .5
        self.cohesion_weight = .4

        self._position = position
        self.acceleration = np.zeros(2)
        # assign random initial direction
        velocity = np.array([random.random() * random.choice((-1, 1)),
                             random.random() * random.choice((-1, 1))])
        self.velocity = set_mag(velocity, self.max_speed)

        # width, height of window. Enable wrapping around edges.
        self.max_y = max_y
        self.max_x = max_x

        self.points = self.calc_points()  # relies on self.max_x, self.max_y

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        "If magnitude of given velocity is greater than max speed scale it down."
        if np.linalg.norm(velocity) > self.max_speed:
            self._velocity = set_mag(velocity, self.max_speed)
        else:
            self._velocity = velocity

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        """
        Make boid wrap around edges rather than fly offscreen.
        Update self.points when setting position
        """
        self._position = self.edges(position)
        self.points = self.calc_points()

    def update_position(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration = np.zeros(2)

    def calc_acceleration(self, flockmates):
        "calculate the forces on boid movement and apply them to acceleration"
        self.separate(flockmates)
        self.align(flockmates)
        self.cohere(flockmates)

    def apply_force(self, force, weight):
        self.acceleration += force * weight

    def find_flockmates(self, flock):
        "return list of boid within perception_radius"
        return [b for b in flock if b != self and
                euclidean_dist_2d(b.position, self.position) < self.perception_radius]

    def separate(self, flockmates):
        "collision avoidance"
        separation_vec = np.zeros(2)

        if len(flockmates) < 1:
            return separation_vec

        for other in flockmates:
            dist = euclidean_dist_2d(self.position, other.position)
            vec = (self.position - other.position) / dist
            separation_vec += vec

        separation_vec = set_mag(separation_vec, self.max_speed)
        separation_force = separation_vec - self.velocity
        separation_force = limit_mag(separation_force, self.max_force)

        self.apply_force(separation_force, self.separation_weight)

    def align(self, flockmates):
        "velocity matching"

        alignment_vec = np.zeros(2)

        if len(flockmates) == 0:
            return alignment_vec

        else:
            for other in flockmates:
                alignment_vec += other.velocity

        alignment_vec /= len(flockmates)
        alignment_vec = set_mag(alignment_vec, self.max_speed)
        alignment_force = alignment_vec - self.velocity
        alignment_force = limit_mag(alignment_force, self.max_force)

        self.apply_force(alignment_force, self.alignment_weight)

    def cohere(self, flockmates):
        "flock_centering"
        cohesion_vec = np.zeros(2)

        if len(flockmates) < 1:
            return cohesion_vec

        for other in flockmates:
            cohesion_vec += other.position

        cohesion_vec /= len(flockmates)
        cohesion_vec = set_mag(cohesion_vec, self.max_speed)
        cohesion_force = cohesion_vec - self.velocity
        cohesion_force = limit_mag(cohesion_force, self.max_force)

        self.apply_force(cohesion_force, self.cohesion_weight)

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

        angle = math.atan2(self.velocity[1], self.velocity[0])
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

    def edges(self, position):
        "makes boid wrap around window instead of fly off-screen"
        x, y = position[0], position[1]

        if x < 0:
            x = x + self.max_x
        if x > self.max_x:
            x = x - self.max_x

        if y < 0:
            y = y + self.max_y
        if y > self.max_y:
            y = y - self.max_y

        position[0], position[1] = x, y

        return position

    def draw(self, win, height):
        "convert to pygame coordinates because pygame origin is in top left"
        points = get_pygame_coords(self.points, height)
        pygame.draw.polygon(win, (0, 0, 255), points)

    def __repr__(self):
        return 'boid position: {}, velocity: {}, acceleration: {}\n'.format(self.position, self.velocity, self.acceleration)


if __name__ == '__main__':
    pass
