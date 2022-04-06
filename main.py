from cgitb import text
import pygame
import random
import os
import sys
import time

from rooms import room1

# variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Neia"

# screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# hide the cursor
pygame.mouse.set_visible(False)

# fonts
Title_font = pygame.font.match_font('Times New Roman')
font1 = pygame.font.Font(Title_font, 32)

Content_font = pygame.font.match_font('ebrima')
font2 = pygame.font.Font(Content_font, 24)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# main loop

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(BLACK)

    # Title
    Title = font1.render("Neia", True, (255, 255, 255))
    screen.blit(Title, (SCREEN_WIDTH / 2 - Title.get_width() / 2, 100))

    # Content
    Content = font2.render("Welcome to Neia, a text-based adventure game.", True, (255, 255, 255))
    screen.blit(Content, (SCREEN_WIDTH / 2 - Content.get_width() / 2, 200))

    # Content
    Content = font2.render("[W] Play", True, (255, 255, 255))
    screen.blit(Content, (SCREEN_WIDTH / 2 - Content.get_width() / 2, 300))
    Content = font2.render("[Q] Quit", True, (255, 255, 255))
    screen.blit(Content, (SCREEN_WIDTH / 2 - Content.get_width() / 2, 350))
    Content = font2.render("[A] Credits", True, (255, 255, 255))
    screen.blit(Content, (SCREEN_WIDTH / 2 - Content.get_width() / 2, 400))

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                screen.fill(BLACK)
                room1.test_room1()
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_a:
                screen.fill(BLACK)
                Content = font2.render("Credits:", True, (255, 255, 255))
                screen.blit(Content, (SCREEN_WIDTH / 2 - Content.get_width() / 2, 100))
                Develpoer = font2.render("Develpoer: Ranger", True, (255, 255, 255))
                screen.blit(Develpoer, (SCREEN_WIDTH / 2 - Develpoer.get_width() / 2, 200))
                Helper = font2.render("Helper: Avidcoder123", True, (255, 255, 255))
    
    pygame.display.update()
    