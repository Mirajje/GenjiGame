import time
from Attack import *
import random
import math


def update(bg_color, screen, player, obstacles, score, sccircle, shieldcircle, phase, fight, waves):
    screen.fill(bg_color)

    if not phase:
        obstacles.update(player)
        if (abs(player.rect.centerx - sccircle.coordinates[0]) <= sccircle.radius) and \
                (abs(player.rect.centery - sccircle.coordinates[1]) <= sccircle.radius):
            score.score += 10
            sccircle.new()
        obstacles_draw(sccircle, phase, obstacles, score)
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

    shield_circle_collision_check(player, shieldcircle)
    if not shieldcircle.exist and not player.shield:
        shieldcircle.new(fight)
    if shieldcircle.exist:
        shieldcircle.output()

    # emp
    if phase and score.score > 0 and not fight:
        pygame.draw.circle(screen, (128, 0, 255), (500, 500), 500 / (score.score + 1) * 2, 5)
        if score.score < 5:
            player.shield = False
            shieldcircle.exist = False

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
                screen.blit(pygame.image.load('pixil-frame-0 (3).png'), (250, 400, 0, 0))
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
                screen.blit(pygame.image.load('pixil-frame-0 (3).png'), (250, 400, 0, 0))
                pygame.display.flip()
                time.sleep(1)
                exit()


def shield_circle_collision_check(player, shieldcircle):
    if shieldcircle.exist and ((abs(player.rect.centerx - shieldcircle.coordinates[0]) <= shieldcircle.radius) and
                               (abs(player.rect.centery - shieldcircle.coordinates[1]) <= shieldcircle.radius)):
        player.shield = True
        shieldcircle.exist = False


def obstacles_draw(sccircle, phase, obstacles, score):
    if not phase:
        sccircle.output()
        for obstacle in obstacles.sprites():
            obstacle.speed = 0.1 + score.score / 450
            obstacle.draw_obstacle()


def fight_cycle(screen, score, coor, waves):
    score.score += 0.005
    if score.score <= 110:
        if score.score - math.floor(score.score) <= 0.005 and math.floor(score.score) % 50 == 0:
            new_wave1 = Wave(screen, score.score, coor[random.randint(0, 3)], True, 250)
            new_wave2 = Wave(screen, score.score, coor[random.randint(0, 3)], False, 250)
            new_wave3 = Wave(screen, score.score, coor[random.randint(0, 3)], (random.randint(1, 2) == 2), 250)
            new_wave4 = Wave(screen, score.score + 7, coor[random.randint(0, 3)], True, 250)
            new_wave5 = Wave(screen, score.score + 7, coor[random.randint(0, 3)], False, 250)
            new_wave6 = Wave(screen, score.score + 7, coor[random.randint(0, 3)], (random.randint(1, 2) == 2), 250)
            new_wave7 = Wave(screen, score.score + 14, coor[random.randint(0, 3)], True, 250)
            new_wave8 = Wave(screen, score.score + 14, coor[random.randint(0, 3)], False, 250)
            new_wave9 = Wave(screen, score.score + 14, coor[random.randint(0, 3)], (random.randint(1, 2) == 2), 250)
            waves.add(new_wave1)
            waves.add(new_wave2)
            waves.add(new_wave3)
            waves.add(new_wave4)
            waves.add(new_wave5)
            waves.add(new_wave6)
            waves.add(new_wave7)
            waves.add(new_wave8)
            waves.add(new_wave9)
    elif 320 > score.score >= 160:
        if score.score - math.floor(score.score) <= 0.005 and math.floor(score.score) % 40 == 0:
            a = coor.copy()
            while a == coor or a == coor[::-1]:
                random.shuffle(a)
            new_wave0 = Wave(screen, score.score, a[0], (math.floor(score.score) % 80 == 0), 250)
            new_wave1 = Wave(screen, score.score + 1.5, a[1], (math.floor(score.score) % 80 == 0), 250)
            new_wave2 = Wave(screen, score.score + 3, a[2], (math.floor(score.score) % 80 == 0), 250)
            new_wave3 = Wave(screen, score.score + 4.5, a[3], (math.floor(score.score) % 80 == 0), 250)
            waves.add(new_wave0)
            waves.add(new_wave1)
            waves.add(new_wave2)
            waves.add(new_wave3)
    elif score.score >= 320:
        screen.fill((255, 255, 255))
        screen.blit(pygame.image.load('pixil-frame-0 (4).png'), (250, 400, 0, 0))
        pygame.display.flip()

        time.sleep(10)
        exit()

