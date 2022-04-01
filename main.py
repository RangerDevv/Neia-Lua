# Imports the necessary modules
from textwrap import fill
from turtle import clear
import pygame
import sys
import os
import time
import random
import math
from assets.everything import shared
from rooms import room1

# Initializes the pygame module
pygame.init()
# Sets the screen size
# Sets the screen size to the screen_size variable
screen = pygame.display.set_mode((shared.screen_width, shared.screen_height))

#setting the besic stuff
pygame.display.set_caption("Neia")
background_color = (0, 0, 0)
font = pygame.font.SysFont(None, 25)


while True: # the main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    text = font.render(shared.Textvar, True, (255, 255, 255))
    screen.blit(text, ( shared.screen_width/2 , shared.screen_height/2 ))
    pygame.display.update()
    time.sleep(1)
    # Clears the screen
    screen.fill(background_color)
    shared.Textvar = "Starting the game"
    text = font.render(shared.Textvar, True, (255, 255, 255))
    screen.blit(text, ( shared.screen_width/2 , shared.screen_height/2 ))
    pygame.display.update()
    time.sleep(5)
    room1.room1()
    break