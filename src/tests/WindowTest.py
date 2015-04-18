__author__ = 'cmaran'

import unittest
import pygame
from pygame.locals import *
from window.Window import Window


class WindowTest(unittest.TestCase):
    def testSetupGL(self):
        window = Window()
        window.setupsplash(100,100)
        window.setupGL()
        screen = pygame.display.set_mode((100,100), DOUBLEBUF | OPENGL)
        self.assertEqual(window.screen,screen)

if __name__ == '__main__':
    unittest.main()
