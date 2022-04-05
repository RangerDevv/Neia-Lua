from cgitb import text
import pygame
import random
import os
import sys
import time

# variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Neia"

# screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# fonts
Title_font = pygame.font.match_font('Times New Roman')
font1 = pygame.font.Font(Title_font, 32)

# main loop

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Title
    Title = font1.render("Neia", True, (255, 255, 255))
    screen.blit(Title, (SCREEN_WIDTH / 2 - Title.get_width() / 2, 100))
    pygame.display.update()

