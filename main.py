# Imports the necessary modules
from textwrap import fill
from turtle import clear
import pygame
import sys
import os
import time
import random
import math
from rooms import prison

# Initializes the pygame module
pygame.init()
# Sets the screen size
screen_size = (800, 600)
# Sets the screen size to the screen_size variable
screen = pygame.display.set_mode(screen_size)

#setting the besic stuff
pygame.display.set_caption("Neia")
background_color = (0, 0, 0)
font = pygame.font.SysFont('arial', 25)

# variables 
textvar = "Neia"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    text = font.render(textvar, True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.update()
    time.sleep(1)
    # Clears the screen
    screen.fill(background_color)
    textvar = "Press F to start"
    text = font.render(textvar, True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.update()
    time.sleep(1)
    prison.prisonroom()