__author__ = 'cmaran'

from OpenGL.GL import *

class Light:

    def setupLight(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_NORMALIZE)
        glEnable(GL_LIGHT0)
        light_position = [0, 5, 0, 0]
        light_color = [1, 1, 1, 1]
        glLight(GL_LIGHT0, GL_POSITION, light_position)
        glLight(GL_LIGHT0, GL_AMBIENT, light_color)