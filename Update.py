import pygame
import time
import random


def update(bg_color, screen, player, obstacles, score, sccircle, shieldcircle):

    screen.fill(bg_color)
    obstacles.update(player)

    if player.invulnerability > 0:
        player.invulnerability -= 1

    pygame.display.set_caption(str(score.score))

    player.update_player()

    if (abs(player.rect.centerx - sccircle.coordinates[0]) <= sccircle.radius) and \
            (abs(player.rect.centery - sccircle.coordinates[1]) <= sccircle.radius):
        sccircle.new()
        score.score += 10

    if shieldcircle.exist and ((abs(player.rect.centerx - shieldcircle.coordinates[0]) <= shieldcircle.radius) and
                               (abs(player.rect.centery - shieldcircle.coordinates[1]) <= shieldcircle.radius)):
        player.shield = True
        shieldcircle.exist = False

    if not player.shield and not shieldcircle.exist:
        if random.randint(1, 15000) == 6969:
            shieldcircle.new()

    sccircle.output()
    if shieldcircle.exist:
        shieldcircle.output()

    for obstacle in obstacles.sprites():
        obstacle.speed = 0.1 + score.score/450
        obstacle.draw_obstacle()
    player.output()
    player.speed = 0.5 + score.score/500

    collision_check(player, obstacles, screen)

    pygame.display.flip()



def collision_check(player, obstacles, screen):

    for obstacle in obstacles.sprites():
        if abs(obstacle.rect.centerx - player.rect.centerx) <= (player.rect.width/2 + obstacle.rect.width/2) and \
                abs(obstacle.rect.centery - player.rect.centery) <= (player.rect.height/2 + obstacle.rect.height/2):
            if player.invulnerability > 0:
                obstacle.kill()
            elif player.shield:
                player.shield = False
                player.invulnerability = 300
                obstacle.kill()
            else:
                screen.fill((0, 0, 0))
                screen.blit(pygame.image.load('pixil-frame-0 (3).png'), (250, 400, 0, 0))
                pygame.display.flip()

                time.sleep(1)
                exit()

