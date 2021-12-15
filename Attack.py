import pygame


class Wave(pygame.sprite.Sprite):

    def __init__(self, screen, spawn_score, position, horizontal, size):

        super(Wave, self).__init__()
        self.spawn_score = spawn_score
        self.size = size
        self.screen = screen
        self.position = position
        self.horizontal = horizontal
        self.color = (0, 0, 0)
        self.size = size

    def update(self, score):

        if 0 <= (score.score - self.spawn_score) <= 1.5:
            self.color = (100, 100, 0)
        elif 24.5 >= score.score - self.spawn_score >= 24:
            self.color = (255, 0, 0)
        elif score.score - self.spawn_score > 28:
            self.kill()

    def output(self, score):

        if (24.5 >= score.score - self.spawn_score >= 24) or (0 <= score.score - self.spawn_score <= 1.5):
            if self.horizontal:
                pygame.draw.rect(self.screen, self.color, (0, self.position - self.size/2, 1000, self.size))
            else:
                pygame.draw.rect(self.screen, self.color, (self.position - self.size/2, 0, self.size, 1000))




