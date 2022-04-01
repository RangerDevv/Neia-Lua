from tkinter import font
from pip import main
import pygame
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from assets.everything import shared
pygame.init()
screen = pygame.display.set_mode((shared.screen_width, shared.screen_height))
background_color = (0, 0, 0)
font = pygame.font.SysFont(None, 25)

def room1():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    while True:
        screen.fill(background_color)
        shared.Textvar = "You have spawned in the prison cell. You dont really know how you ended up here, but you know that you have to get out of here. Press [ENTER] to continue."
        text = font.render(shared.Textvar, True, (255, 255, 255))
        screen.blit(text, ( shared.screen_width/2 , shared.screen_height/2 ))
        pygame.display.update()
        if pygame.event == pygame.K_RETURN:
            shared.Textvar = "There are 4 directions you can look in. Press [W] to look up, [A] to look left, [S] to look down, [D] to look right. Press [ENTER] to continue."