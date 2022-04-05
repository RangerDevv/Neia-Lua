import pygame
import random
import os
import sys

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

def test_room1():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill((0, 0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()