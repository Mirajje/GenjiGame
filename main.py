from Player import *
import Controls
import Update
from Obstacle import *
from pygame.sprite import Group
import time
import Circles
import Classes
import Menu


def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    score = Classes.Score()
    player = Player(screen, pygame.image.load('genji.png'), 0.6)
    obstacles = Group()
    waves = Group()
    sc_circle = Circles.ScoreCircle(screen)
    shield_circle = Circles.ShieldCircle(screen)
    phase = False
    coordinates = [125, 375, 625, 875]
    fight = False
    bg_color = (0, 0, 0)
    pygame.display.set_caption('GenjiGame')

    difficulty = Menu.menu(screen)

    frequency_list = [150, 100, 50]
    obstacle_speed_list = [750, 600, 450]

    while True:

        pygame.time.Clock().tick(1200)

        if score.score > 250 and not phase:
            phase = True
            score.score = 255

        if not phase:
            frequency = int(frequency_list[difficulty] / (score.score + 1)) + 1
            if time.process_time() % frequency == 0:
                new_obstacle = Obstacle(screen, 0.1 + score.score / obstacle_speed_list[difficulty])
                obstacles.add(new_obstacle)
        else:
            if score.score > 0 and not fight:
                score.score -= 0.5
            else:
                fight = True

        if fight:
            Update.fight_cycle(screen, score, coordinates, waves)

        Controls.events(player)
        if score.score <= 255:
            bg_color = (score.score, score.score, score.score)
        Update.update(bg_color, screen, player, obstacles, score, sc_circle, shield_circle, phase, fight, waves,
                      obstacle_speed_list, difficulty)


run()
