from player import *
import Controls
import Update
from Obstacle import *
import random
from pygame.sprite import Group
import time
import ScoreCircle


def run():

    random.seed(a=None, version=2)
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    score = 250
    pygame.display.set_caption(str(score))
    bg_color = (0, 0, 0)
    player = Player(screen, pygame.image.load('pixil-frame-0 (1).png'), 0.5)
    obstacles = Group()
    sccircle = ScoreCircle.ScCircle(screen)


    while True:
        frequency = int(50/(score + 1)) + 1
        if time.process_time() % frequency == 0:
            new_obstacle = Obstacle(screen, 0.1 + score/450)
            obstacles.add(new_obstacle)
        Controls.events(player)

        if score > 250:
            screen.fill((255, 255, 255))
            screen.blit(pygame.image.load('pixil-frame-0 (4).png'), (250, 400, 0, 0))
            pygame.display.flip()

            time.sleep(1)
            sys.exit()

        bg_color = (score, score, score)
        score, sccircle = Update.update(bg_color, screen, player, obstacles, score, sccircle)
        pygame.display.set_caption(str(score))


run()
