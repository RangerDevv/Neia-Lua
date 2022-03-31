from pip import main
import pygame
from vars import shared

pygame.init()

def room1():
    shared.Textvar = "This is room 1"
    pygame.display.update()