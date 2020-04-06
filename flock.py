from boids import Boid
import numpy as np
import random


class Flock():
    "Class for creating and handling boid objects within pygame loop"

    def __init__(self, n, width, height):
        self.boids = [Boid(np.array([random.random()*width, random.random()*height]),
                           width, height) for i in range(n)]
        self.width = width
        self.height = height

    def update_positions(self):

        for b in self.boids:
            flockmates = b.find_flockmates(self.boids)
            b.calc_acceleration(flockmates)
            b.update_position()

    def draw_flock(self, win):
        for boid in self.boids:
            boid.draw(win, self.height)

    def __repr__(self):
        return 'Flock with {} boids\n'.format(len(self.boids))


if __name__ == '__main__':
    pass
