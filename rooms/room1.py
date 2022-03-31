from pip import main
import pygame
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

pygame.init()

def room1():
    shared.Textvar = "This is room 1"
    pygame.display.update()