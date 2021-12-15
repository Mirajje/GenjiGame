import sys
from Obstacle import *


def events(player):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move_right = True
            if event.key == pygame.K_w:
                player.move_upward = True
            if event.key == pygame.K_a:
                player.move_left = True
            if event.key == pygame.K_s:
                player.move_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.move_right = False
            if event.key == pygame.K_w:
                player.move_upward = False
            if event.key == pygame.K_a:
                player.move_left = False
            if event.key == pygame.K_s:
                player.move_down = False
