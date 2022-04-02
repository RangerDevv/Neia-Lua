import pygame
import sys
import os
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
        #text
        Text = font.render("Room 1", True, (255, 255, 255))
        screen.blit(Text, [10, 10])
        #player stats
        Health = font.render("Health: " + str(shared.Health), True, (255, 255, 255))
        screen.blit(Health, [10, 30])
        Gold = font.render("Gold: " + str(shared.Gold), True, (255, 255, 255))
        screen.blit(Gold, [10, 50])
        Level = font.render("Level: " + str(shared.Level), True, (255, 255, 255))
        screen.blit(Level, [10, 70])
        Experience = font.render("Experience: " + str(shared.Experience), True, (255, 255, 255))
        screen.blit(Experience, [10, 90])