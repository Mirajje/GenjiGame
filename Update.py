import pygame
import time
import random
import ScoreCircle


def update(bg_color, screen, player, obstacles, score, sccircle):

    screen.fill(bg_color)
    obstacles.update(player)

    pygame.display.set_caption(str(score))

    player.update_player()

    if (abs(player.rect.centerx - sccircle.coordinates[0]) <= sccircle.radius) and (abs(player.rect.centery - sccircle.coordinates[1]) <= sccircle.radius):
        sccircle.new()
        score += 10

    sccircle.output()

    for obstacle in obstacles.sprites():
        obstacle.speed = 0.1 + score/450
        obstacle.draw_obstacle()
    player.output()
    player.speed = 0.5 + score/500

    collisioncheck(player, obstacles, screen)

    pygame.display.flip()

    return score, sccircle


def collisioncheck(player, obstacles, screen):

    for obstacle in obstacles.sprites():
        if abs(obstacle.rect.centerx - player.rect.centerx) <= (player.rect.width/2 + obstacle.rect.width/2) and abs(obstacle.rect.centery - player.rect.centery) <= (player.rect.height/2 + obstacle.rect.height/2):
            screen.fill((0, 0, 0))
            screen.blit(pygame.image.load('pixil-frame-0 (3).png'), (250, 400, 0, 0))
            pygame.display.flip()

            time.sleep(1)
            exit()

