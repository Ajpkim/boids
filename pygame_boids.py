import pygame
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

        win.fill((100, 255, 255))

        flock.update_positions()
        flock.draw_flock(win)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    pass
