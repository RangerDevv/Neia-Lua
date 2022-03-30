# Imports the necessary modules
from textwrap import fill
from turtle import clear
import pygame
import sys
import os
import time
import random
import math
from rooms import room1 as room1

# Initializes the pygame module
pygame.init()
# Sets the screen size
screen_width = 800
screen_height = 600
# Sets the screen size to the screen_size variable
screen = pygame.display.set_mode((screen_width, screen_height))

#setting the besic stuff
pygame.display.set_caption("Neia")
background_color = (0, 0, 0)
font = pygame.font.SysFont(None, 25)

# variables 
textvar = "Neia"

while True: # the main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    text = font.render(textvar, True, (255, 255, 255))
    screen.blit(text, ( screen_width/2 , screen_height/2 ))
    pygame.display.update()
    time.sleep(1)
    # Clears the screen
    screen.fill(background_color)
    textvar = "Starting the game..."
    time.sleep(1)
    room1.prisonroom()