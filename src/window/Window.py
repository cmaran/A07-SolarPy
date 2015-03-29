__author__ = 'Berni'

import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Window:

    screen = None
    splashscreen = None
    size = None
    fieldOfView = 100

    def setup(self, sizex, sizey):

        self.size = width, height = sizex, sizey

        self.splashscreen = pygame.image.load('splashscreen_v1.jpg')
        self.splashscreen = pygame.transform.scale(self.splashscreen, self.size)

        icon = pygame.image.load('splashscreen_v1.jpg')
        icon = pygame.transform.scale(icon, (32, 32))
        pygame.display.set_icon(icon)

        self.screen = pygame.display.set_mode(self.size, RESIZABLE)
        pygame.display.set_caption("Solar-System")

    def setupGL(self):
        self.screen = pygame.display.set_mode(self.size, DOUBLEBUF | OPENGL)

        gluPerspective(self.fieldOfView, (self.size[0] / self.size[1]), 1.0, 100.0)

    def reset(self):
        self.screen = pygame.display.set_mode(self.size)
