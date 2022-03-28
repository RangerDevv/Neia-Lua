# Imports the necessary modules
import pygame
import sys
import os
import time
import random
import math

# Initializes the pygame module
pygame.init()
# Sets the screen size
screen_size = (800, 600)
# Sets the screen size to the screen_size variable
screen = pygame.display.set_mode(screen_size)

#setting the besic stuff
pygame.display.set_caption("Space Invaders")
background_color = (0, 0, 0)
font = pygame.font.SysFont(None, 25)