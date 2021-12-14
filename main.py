from player import *
import Controls
import Update
from Obstacle import *
from pygame.sprite import Group
import time
import Circles
import Classes


def run():

    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    score = Classes.Score()
    pygame.display.set_caption(str(score.score))
    player = Player(screen, pygame.image.load('pixil-frame-0 (1).png'), 0.5)
    obstacles = Group()
    sccircle = Circles.Score_Circle(screen)
    shieldcircle = Circles.Shield_Circle(screen)

    while True:

        pygame.time.Clock().tick(1200)
        frequency = int(50/(score.score + 1)) + 1
        if time.process_time() % frequency == 0:
            new_obstacle = Obstacle(screen, 0.1 + score.score/450)
            obstacles.add(new_obstacle)
        Controls.events(player)

        if score.score > 250:
            screen.fill((255, 255, 255))
            screen.blit(pygame.image.load('pixil-frame-0 (4).png'), (250, 400, 0, 0))
            pygame.display.flip()

            time.sleep(10)
            exit()

        bg_color = (score.score, score.score, score.score)
        Update.update(bg_color, screen, player, obstacles, score, sccircle, shieldcircle)


run()
