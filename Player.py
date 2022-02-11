import pygame


class Player:

    def __init__(self, screen, image, speed):

        self.normal_speed = self.speed = speed
        self.screen = screen
        self.image = image

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.move_right = self.move_left = self.move_upward = self.move_down = False
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.shield = False
        self.invulnerability = 0

    def output(self):

        if self.shield or self.invulnerability > 0:
            pygame.draw.circle(self.screen, (255, 255, 0), (self.centerx, self.centery), 40, 5)
        self.screen.blit(self.image, self.rect)

    def update_player(self):
        if (self.move_right and self.move_upward) or (self.move_right and self.move_down) or \
                (self.move_left and self.move_upward) or (self.move_left and self.move_down):
            self.speed = self.speed / (2 ** 0.5)
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed
        if self.move_upward and self.rect.top > 0:
            self.centery -= self.speed
        if self.move_left and self.rect.left > 0:
            self.centerx -= self.speed

        self.speed = self.normal_speed
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
