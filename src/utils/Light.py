__author__ = 'cmaran'

from OpenGL.GL import *

class Light:
    """
    Licht Klasse
    """

    def setup(self):
        """
        Erstellt das Licht
        :return:
        """
        glEnable(GL_LIGHTING)
        glEnable(GL_NORMALIZE)
        glEnable(GL_LIGHT0)
        position = [0, 5, 0, 0]
        color = [1, 1, 1, 1]
        glLight(GL_LIGHT0, GL_POSITION, position)
        glLight(GL_LIGHT0, GL_AMBIENT, color)