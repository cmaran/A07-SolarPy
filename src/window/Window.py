__author__ = 'cmaran'

import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Window:
    """
    Fenster - Grundfläche
    """
    screen = None
    splash = None
    size = None
    fieldOfView = None

    def __init__(self, x, y, fieldOfView, splashImage):
        """
        Erzeugt das Fenster
        Laedt den Splashscreen und setzt den Titel
        :param x: Auflösung - x
        :param y: Auflösung - y
        :return:
        """
        self.size = width, height = x, y
        self.fieldOfView = fieldOfView
        self.splash = pygame.image.load(splashImage)
        self.splash = pygame.transform.scale(self.splash, self.size)
        self.screen = pygame.display.set_mode(self.size, RESIZABLE)
        pygame.display.set_caption("SolarPy")


    def setupGL(self):
        """
        Lädt OpenGl in PyGame
        :return:
        """
        self.screen = pygame.display.set_mode(self.size, DOUBLEBUF | OPENGL)
        gluPerspective(self.fieldOfView, (self.size[0] / self.size[1]), 1.0, 100.0)



