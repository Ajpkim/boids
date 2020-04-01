import pygame
import time
from helper_functions import *


def game_loop(flock, width, height, delay):

    FPS = 60
    clock = pygame.time.Clock()

    pygame.init()

    clock.tick(FPS)

    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Boids Boids Boids")

    run = True

    while run:
        pygame.time.wait(delay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                run = False

        for boid in flock:
            boid.update_position()

        draw_flock(win, flock)
        pygame.display.update()

    pygame.quit()


# draw triangle
def draw_flock(win, flock):
    win.fill((255, 255, 255))
    for boid in flock:
        points = get_pygame_coords(boid.points, 500)
        pygame.draw.polygon(win, (0, 0, 255), points, 3)


# # draw cirlces
# def draw_flock(win, boids):
#     win.fill((255, 255, 255))
#     for boid in boids:
#         pygame.draw.circle(win, (0, 0, 255), [boid.x, boid.y], 4)
