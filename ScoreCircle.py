import pygame
import random


class ScCircle():

    def __init__(self, screen):

        self.screen = screen
        self.radius = 30
        self.coordinates = (random.randint(100, 900), random.randint(100, 900))
        self.color = (0, 255, 0)
        self.exist = False

    def output(self):

        pygame.draw.circle(self.screen, self.color, self.coordinates, self.radius)
        self.exist = True

    def new(self):

        self.coordinates = (random.randint(100, 900), random.randint(100, 900))

