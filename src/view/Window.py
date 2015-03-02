__author__ = 'cmaran'

import pygame
import sys
from pygame.locals import *

pygame.init()

setDisplay = pygame.display.set_mode((1930, 1080))
pygame.display.set_caption("SolarPy")
while True:
    for event in pygame.event.get():
        print event
        if event.tyoe == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
