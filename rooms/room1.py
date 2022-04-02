import pygame
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from assets.everything import shared
pygame.init()
screen = pygame.display.set_mode((shared.screen_width, shared.screen_height))
background_color = (0, 0, 0)
font = pygame.font.SysFont(None, 25)

def room1():
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    