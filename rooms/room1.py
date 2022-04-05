import pygame
import random
import os
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

def test_room1():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))