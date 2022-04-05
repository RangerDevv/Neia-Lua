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

Content_font = pygame.font.match_font('ebrima')
font2 = pygame.font.Font(Content_font, 24)

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

    # Content
    Content = font2.render("Welcome to Neia, a text-based adventure game.", True, (255, 255, 255))
    screen.blit(Content, (SCREEN_WIDTH / 2 - Content.get_width() / 2, 200))
    pygame.display.update()

    # Content
    Content = font2.render("[W] Play", True, (255, 255, 255))
    screen.blit(Content, (SCREEN_WIDTH / 2 - Content.get_width() / 2, 300))
    pygame.display.update()
    Content = font2.render("[Q] Quit", True, (255, 255, 255))
    screen.blit(Content, (SCREEN_WIDTH / 2 - Content.get_width() / 2, 350))
    pygame.display.update()
    Content = font2.render("[A] Credits", True, (255, 255, 255))
    screen.blit(Content, (SCREEN_WIDTH / 2 - Content.get_width() / 2, 400))
    pygame.display.update()
