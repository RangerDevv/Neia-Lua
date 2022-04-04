# Imports the necessary modules
from cgitb import text
from codecs import backslashreplace_errors
from distutils.command.build_scripts import first_line_re
from multiprocessing.connection import wait
from threading import Timer
import pygame
import sys
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
isplaying = False


while True: # the main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            text = font.render("Welcome to Neia!" , True, (255, 255, 255))
            screen.blit(text, [200, 200])
            pygame.display.update()
            time.sleep(2)
            background_color = (0, 0, 0)
            text = font.render("Loading the game" , True, (255, 255, 255))
            screen.blit(text, [200, 200])
            pygame.display.update()
            room1.prison()
