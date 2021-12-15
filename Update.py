import pygame

import time
from Wave import Wave
import random
import math


def update(bg_color, screen, player, obstacles, score, sc_circle, shield_circle, phase, fight, waves):
    screen.fill(bg_color)

    if not phase:
        obstacles.update(player)
        if (abs(player.rect.centerx - sc_circle.coordinates[0]) <= sc_circle.radius) and \
                (abs(player.rect.centery - sc_circle.coordinates[1]) <= sc_circle.radius):
            score.score += 10
            sc_circle.new()
        obstacles_draw(sc_circle, phase, obstacles, score)
        obstacles_collision_check(player, obstacles, screen)

    if fight:
        wave_collision_check(screen, player, waves, score)

    if fight:
        waves.update(score)
        for wave in waves:
            wave.output(score)

    if player.invulnerability > 0:
        player.invulnerability -= 1
    player.update_player()
    player.output()

    shield_circle_collision_check(player, shield_circle)
    if not shield_circle.exist and not player.shield:
        shield_circle.new(fight)
    if shield_circle.exist:
        shield_circle.output()

    # emp
    if phase and score.score > 0 and not fight:
        pygame.draw.circle(screen, (128, 0, 255), (500, 500), 500 / (score.score + 1) * 2, 5)
        if score.score < 5:
            player.shield = False
            shield_circle.exist = False

    pygame.display.flip()


def obstacles_collision_check(player, obstacles, screen):
    for obstacle in obstacles.sprites():
        if abs(obstacle.rect.centerx - player.rect.centerx) <= (player.rect.width / 2 + obstacle.rect.width / 2) and \
                abs(obstacle.rect.centery - player.rect.centery) <= (
                player.rect.height / 2 + obstacle.rect.height / 2):
            if player.invulnerability > 0:
                obstacle.kill()
            elif player.shield:
                player.shield = False
                player.invulnerability = 300
                obstacle.kill()
            else:
                screen.fill((0, 0, 0))
                screen.blit(pygame.image.load('lose.png'), (250, 400, 0, 0))
                pygame.display.flip()
                time.sleep(1)
                exit()


def wave_collision_check(screen, player, waves, score):
    check = False
    for wave in waves:
        if 24.5 >= score.score - wave.spawn_score >= 24.49:
            if not wave.horizontal:
                if abs(wave.position - player.centerx) < 151:
                    check = True
                    break
            else:
                if abs(wave.position - player.centery) < 155:
                    check = True
                    break
    if check:
        if player.invulnerability == 0:
            if player.shield:
                player.shield = False
                player.invulnerability = 300
            else:
                screen.fill((0, 0, 0))
                screen.blit(pygame.image.load('lose.png'), (250, 400, 0, 0))
                pygame.display.flip()
                time.sleep(1)
                exit()


def shield_circle_collision_check(player, shield_circle):
    if shield_circle.exist and ((abs(player.rect.centerx - shield_circle.coordinates[0]) <= shield_circle.radius) and
                                (abs(player.rect.centery - shield_circle.coordinates[1]) <= shield_circle.radius)):
        player.shield = True
        shield_circle.exist = False


def obstacles_draw(sc_circle, phase, obstacles, score):
    if not phase:
        sc_circle.output()
        for obstacle in obstacles.sprites():
            obstacle.speed = 0.1 + score.score / 450
            obstacle.draw_obstacle()


def fight_cycle(screen, score, coordinates, waves):
    score.score += 0.005
    if score.score <= 110:
        if score.score - math.floor(score.score) <= 0.005 and math.floor(score.score) % 50 == 0:
            waves.add(
                Wave(screen, score.score, coordinates[random.randint(0, 3)], True, 250),
                Wave(screen, score.score, coordinates[random.randint(0, 3)], False, 250),
                Wave(screen, score.score, coordinates[random.randint(0, 3)], (random.randint(1, 2) == 2), 250),
                Wave(screen, score.score + 7, coordinates[random.randint(0, 3)], True, 250),
                Wave(screen, score.score + 7, coordinates[random.randint(0, 3)], False, 250),
                Wave(screen, score.score + 7, coordinates[random.randint(0, 3)], (random.randint(1, 2) == 2), 250),
                Wave(screen, score.score + 14, coordinates[random.randint(0, 3)], True, 250),
                Wave(screen, score.score + 14, coordinates[random.randint(0, 3)], False, 250),
                Wave(screen, score.score + 14, coordinates[random.randint(0, 3)], (random.randint(1, 2) == 2), 250)
            )
    elif 320 > score.score >= 160:
        if score.score - math.floor(score.score) <= 0.005 and math.floor(score.score) % 40 == 0:
            a = coordinates.copy()
            while a == coordinates or a == coordinates[::-1]:
                random.shuffle(a)
            waves.add(
                Wave(screen, score.score, a[0], (math.floor(score.score) % 80 == 0), 250),
                Wave(screen, score.score + 1.5, a[1], (math.floor(score.score) % 80 == 0), 250),
                Wave(screen, score.score + 3, a[2], (math.floor(score.score) % 80 == 0), 250),
                Wave(screen, score.score + 4.5, a[3], (math.floor(score.score) % 80 == 0), 250)
            )
    elif score.score >= 320:
        screen.fill((255, 255, 255))
        screen.blit(pygame.image.load('win.png'), (250, 400, 0, 0))
        pygame.display.flip()

        time.sleep(10)
        exit()
