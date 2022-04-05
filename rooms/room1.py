from cgitb import text
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

# screen 
screen = pygame.display.set_mode((800, 600))

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# font
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

        screen.fill(BLACK)

        # player stats
        health = player.health
        max_health = player.max_health
        level = player.level
        experience = player.experience
        gold = player.gold
        # render the stats
        text = font2.render("Health: " + str(health) + "/" + str(max_health), True, (255, 255, 255))
        screen.blit(text, (10, 10))
        text = font2.render("Level: " + str(level), True, (255, 255, 255))
        screen.blit(text, (10, 40))
        text = font2.render("Experience: " + str(experience), True, (255, 255, 255))
        screen.blit(text, (10, 70))
        text = font2.render("Gold: " + str(gold), True, (255, 255, 255))
        screen.blit(text, (10, 100))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.health = player.health -1
                    Textvar = "You pressed W!"
                    text = font2.render(Textvar, True, (255, 255, 255))
                    screen.blit(text, (100, 100))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()