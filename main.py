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
pygame.display.set_caption("Neia")
background_color = (0, 0, 0)
font = pygame.font.SysFont(None, 25)

# variables 
textworld = ""

while True:
    textworld = "Welcome to Neia. Press F to start the game."
    pygame.event.get()
    # Sets the screen to the background color
    screen.fill(background_color)
    # Sets the text to the font variable
    text = font.render( textworld , True, (255, 255, 255))
    # Sets the text position to the middle of the screen
    text_rect = text.get_rect()
    text_rect.center = (screen_size[0] // 2, screen_size[1] // 2)
    # Draws the text to the screen
    screen.blit(text, text_rect)
    # Updates the screen
    pygame.display.update()

    # Checks if the user presses the F key
    if pygame.key.get_pressed()[pygame.K_f]:
        main()

    def main():
        textworld = "totally hello world!"
        text = font.render( textworld, True, (255, 255, 255))
        screen.blit(text, text_rect)
        # Updates the screen
        pygame.display.update()