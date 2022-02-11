import pygame


def menu(screen):
    difficulty = -1
    screen.fill((255, 255, 255))
    button_intense = [255, 255, 255]
    button_difficulty = pygame.transform.scale(pygame.image.load('difficulty.png'), (400, 80))
    button_low = pygame.image.load('difficulty_low.png')
    button_medium = pygame.image.load('difficulty_medium.png')
    button_hard = pygame.image.load('difficulty_hard.png')
    while True:
        screen.fill((255, 255, 255))
        pygame.time.Clock().tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if 440 <= pos[0] <= 560:
                        if 480 <= pos[1] <= 520:
                            difficulty = 1
                        elif 380 <= pos[1] <= 420:
                            difficulty = 0
                        elif 580 <= pos[1] <= 620:
                            difficulty = 2

        if difficulty != -1:
            break
        button_intense = button_colors(screen, button_intense)
        screen.blit(button_difficulty, (300, 100, 0, 0))
        screen.blit(button_low, (440, 380, 0, 0))
        screen.blit(button_medium, (440, 480, 0, 0))
        screen.blit(button_hard, (440, 580, 0, 0))
        pygame.display.flip()

    return difficulty


def button_colors(screen, button_intense):
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        if 440 <= pos[0] <= 560:
            if 480 <= pos[1] <= 520:
                if button_intense[1] >= 125/144:
                    button_intense[1] -= 125/144
                pygame.draw.rect(screen, (255, 255, button_intense[1]),
                                 (440, 480, 120, 40))
                button_intense[0] = 255
                button_intense[2] = 255

            elif 380 <= pos[1] <= 420:
                if button_intense[0] >= 125/144:
                    button_intense[0] -= 125/144
                pygame.draw.rect(screen, (255, 255, button_intense[0]),
                                 (440, 380, 120, 40))
                button_intense[1] = 255
                button_intense[2] = 255

            elif 580 <= pos[1] <= 620:
                if button_intense[2] >= 125/144:
                    button_intense[2] -= 125/144
                pygame.draw.rect(screen, (255, 255, button_intense[2]),
                                 (440, 580, 120, 40))
                button_intense[0] = 255
                button_intense[1] = 255

            else:
                button_intense[0] = 255
                button_intense[1] = 255
                button_intense[2] = 255
        else:
            button_intense[0] = 255
            button_intense[1] = 255
            button_intense[2] = 255

    return button_intense
