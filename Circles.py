import pygame
import random


class ScoreCircle:

    def __init__(self, screen):

        self.screen = screen
        self.radius = 30
        self.coordinates = (random.randint(100, 900), random.randint(100, 900))
        self.color = (0, 190, 0)

    def output(self):

        pygame.draw.circle(self.screen, self.color, self.coordinates, self.radius)

    def new(self):

        self.coordinates = (random.randint(100, 900), random.randint(100, 900))


class ShieldCircle:

    def __init__(self, screen):

        self.screen = screen
        self.radius = 45
        self.coordinates = (random.randint(100, 900), random.randint(100, 900))
        self.color = (255, 255, 0)
        self.exist = True

    def output(self):

        pygame.draw.circle(self.screen, self.color, self.coordinates, self.radius)

    def new(self, fight):

        k = 15000
        if fight:
            k = 30000
        if random.randint(1, k) == 6969:
            self.coordinates = (random.randint(100, 900), random.randint(100, 900))
            self.exist = True
