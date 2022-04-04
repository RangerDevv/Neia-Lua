from cgitb import text
import pygame
import sys
import os
import time
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from assets.everything import shared
from assets.player import player

pygame.init()
screen = pygame.display.set_mode((shared.screen_width, shared.screen_height))
background_color = (0, 0, 0)
font = pygame.font.SysFont(None, 25)

#player stats
shared.Health = player.health
shared.Gold = player.gold
shared.Level = player.level
shared.Experience = player.experience

def prison():
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(background_color)
        text = font.render("this is the prison!" , True, (255, 255, 255))
        screen.blit(text, [200, 200])
        pygame.display.update()   