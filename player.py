import pygame


class Player():

    def __init__(self, screen, image, speed):

        self.screen = screen
        self.speed = speed
        self.image = image

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.mright = self.mleft = self.mupward = self.mdown = False
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def output(self):

        self.screen.blit(self.image, self.rect)

    def update_player(self):

        if self.mright and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed
        if self.mupward and self.rect.top > 0:
            self.centery -= self.speed
        if self.mleft and self.rect.left > 0:
            self.centerx -= self.speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

