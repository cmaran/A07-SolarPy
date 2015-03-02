__author__ = 'cmaran'

import pygame
import sys
from pygame.locals import *

pygame.init()


img = pygame.image.load("res/galaxy.jpg")
x = 1920
y = 1080
setDisplay = pygame.display.set_mode((x, y))
pygame.display.set_caption("SolarPy")

while True:
    setDisplay.blit(x,y)
    for event in pygame.event.get():
        print event
        if event.tyoe == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
