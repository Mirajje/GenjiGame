import pygame
import random


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, screen, speed):
        super(Obstacle, self).__init__()
        self.speed = speed
        self.screen = screen
        self.color = (0, 0, 0)
        self.rect = pygame.Rect(0, 0, random.random()*20 + 5, random.random() * 20 + 5)
        self.screen_rect = screen.get_rect
        self.rect.centerx = (random.randint(13, 987))
        self.y = float(self.rect.height/2+1)

    def update(self, player):

        self.y += self.speed
        self.rect.centery = self.y
        diff = ((player.rect.centerx - self.rect.centerx)**2 + (player.rect.centery - self.rect.centery)**2)**0.5
        if diff < 1000 and diff != 0:
            if int(50/diff*255) <= 255:
                self.color = (int(50/diff*255), 0, 0)
        if self.rect.centery > 1100:
            self.kill()

    def draw_obstacle(self):

        pygame.draw.rect(self.screen, self.color, self.rect)
