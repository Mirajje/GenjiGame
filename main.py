from player import *
import Controls
import Update
from Obstacle import *
from pygame.sprite import Group
import time
import Circles
import Classes
from Attack import *


def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    score = Classes.Score()
    player = Player(screen, pygame.image.load('pixil-frame-0 (1).png'), 0.6)
    obstacles = Group()
    waves = Group()
    sccircle = Circles.Score_Circle(screen)
    shieldcircle = Circles.Shield_Circle(screen)
    phase = False
    coor = [125, 375, 625, 875]
    fight = False
    bg_color = (0, 0, 0)

    while True:

        pygame.time.Clock().tick(1200)

        if score.score > 250 and not phase:
            phase = True
            score.score = 255

        if not phase:
            frequency = int(50 / (score.score + 1)) + 1
            if time.process_time() % frequency == 0:
                new_obstacle = Obstacle(screen, 0.1 + score.score / 450)
                obstacles.add(new_obstacle)
        else:
            if score.score > 0 and not fight:
                score.score -= 0.5
            else:
                fight = True

        if fight:
            Update.fight_cycle(screen, score, coor, waves)

        Controls.events(player)
        if score.score <= 255:
            bg_color = (score.score, score.score, score.score)
        Update.update(bg_color, screen, player, obstacles, score, sccircle, shieldcircle, phase, fight, waves)


run()
