import pygame
import sys
from Obstacle import *


def events(player):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.mright = True
            if event.key == pygame.K_w:
                player.mupward = True
            if event.key == pygame.K_a:
                player.mleft = True
            if event.key == pygame.K_s:
                player.mdown = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.mright = False
            if event.key == pygame.K_w:
                player.mupward = False
            if event.key == pygame.K_a:
                player.mleft = False
            if event.key == pygame.K_s:
                player.mdown = False


