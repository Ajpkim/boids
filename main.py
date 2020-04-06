from flock import Flock
from boids import Boid
from pygame_boids import game_loop

# slides on sptial efficiency
# https://cse.buffalo.edu/faculty/miller/Courses/CSE633/Cosgrove-Spring-2014-CSE633.pdf

# ToDo:
# - hovering mouse that repels like a predator or sets goal
# - sliders for the weight of the 3 rules and max_force
# - add 'keep view clear' rule
# - add predators, obstacles, goals
# - quadtree... spatial binning
# - argparsing
# - optimize calcs if necessary... remove reliance on np.lingalg...

n = 50
width = 800
height = 500
delay = 25


def main():
    flock = Flock(n, width, height)
    game_loop(flock, width, height, delay)


if __name__ == '__main__':
    main()
