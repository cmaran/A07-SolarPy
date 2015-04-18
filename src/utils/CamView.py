__author__ = 'cmaran'


import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class CamView:
    """
    Kameraperspektive
    """
    eyeX = None
    eyeY = None
    eyeZ = None
    centerX = None
    centerY = None
    centerZ = None
    upX = None
    upY = None
    upZ = None


    def __init__(self, eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ):
        """
        :param eyeX: Specifies the position of the eye point.
        :param eyeY: Specifies the position of the eye point.
        :param eyeZ: Specifies the position of the eye point.
        :param centerX: Specifies the position of the reference point.
        :param centerY: Specifies the position of the reference point.
        :param centerZ: Specifies the position of the reference point.
        :param upX: Specifies the direction of the up vector.
        :param upY: Specifies the direction of the up vector.
        :param upZ: Specifies the direction of the up vector.
        :return:
        """
        self.eyeX = eyeX
        self.eyeY = eyeY
        self.eyeZ = eyeZ
        self.centerX = centerX
        self.centerY = centerY
        self.centerZ = centerZ
        self.upX = upX
        self.upY = upY
        self.upZ = upZ

        gluLookAt(self.eyeX, self.eyeY, self.eyeZ, self.centerX, self.centerY, self.centerZ, self.upX, self.upY, self.upZ)