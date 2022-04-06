from cgitb import text
from pickle import REDUCE
import pygame
import random
import os
import sys
from assets.player import player

# for calling player.py
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

pygame.init()

# hiding the cursor
pygame.mouse.set_visible(False)

# screen 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# font
Stats_font = pygame.font.match_font('freesansbold.ttf')
font1 = pygame.font.Font(Stats_font, 24)

Content_font = pygame.font.match_font('ebrima')
font2 = pygame.font.Font(Content_font, 24)

# variables
Textvar = " "

def test_room1():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()      
        screen.fill(BLACK)

        # player stats
        health = player.health
        max_health = player.max_health
        level = player.level
        experience = player.experience
        gold = player.gold
        # render the stats
        Stats = font1.render("Health: " + str(health) + "/" + str(max_health), True, (RED))
        screen.blit(Stats, (10, 10))
        Stats = font1.render("Level: " + str(level), True, (GREEN))
        screen.blit(Stats, (180, 10))
        Stats = font1.render("Experience: " + str(experience), True, (BLUE))
        screen.blit(Stats, (280, 10))
        Stats = font1.render("Gold: " + str(gold), True, (255, 255, 0))
        screen.blit(Stats, (420, 10))
        Quit = font2.render("[Q] Quit", True, (255, 255, 255))
        screen.blit(Quit, (SCREEN_WIDTH / 2 - Quit.get_width() / 2, SCREEN_HEIGHT - 50))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("space")


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
