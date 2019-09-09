import pygame
from pygame.locals import *

pygame.init()

# Game Resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Show Text')
titlefont = pygame.font.Font('freesansbold.ttf', 60)
menufont = pygame.font.Font('freesansbold.ttf', 50)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (112, 129, 140)
lgray = (141, 154, 163)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (59, 175, 247)
yellow = (255, 255, 0)

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

for i in range(20):
    print("")


def main_menu():

    main = True
    menu = True
    start = False

    while main:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and x >= 345 and y >= 360 and x <= 455 and y <= 410:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and x >= 340 and y >= 300 and x <= 460 and y <= 350:
                start = True
                menu = False

        if menu == True:
            # Main Menu UI
            if x >= 340 and y >= 300 and x <= 460 and y <= 350:
                selected = "start"
            if x >= 345 and y >= 360 and x <= 455 and y <= 410:
                selected = "quit"
            if x < 340 or y < 300 or x > 455 or y > 410:
                selected = ""
            screen.fill(gray)
            title = titlefont.render('Welcome', True, blue, gray)
            if selected == "start":
                text_start = menufont.render('Start', True, white, lgray)
            else:
                text_start = menufont.render('Start', True, black, gray)
            if selected == "quit":
                text_quit = menufont.render('Quit', True, white, lgray)
            else:
                text_quit = menufont.render('Quit', True, black, gray)

            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()

            # Main Menu Text
            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
            screen.blit(text_start,
                        (screen_width / 2 - (start_rect[2] / 2), 300))
            screen.blit(text_quit,
                        (screen_width / 2 - (quit_rect[2] / 2), 360))

        elif start == True:
            # Start Menu UI
            screen.fill(gray)
            title = titlefont.render('Welcome', True, blue, gray)
            title_rect = title.get_rect()
            # Text
            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption(
            "Python - Pygame Simple Main Menu Selection")


main_menu()
pygame.quit()
quit()
