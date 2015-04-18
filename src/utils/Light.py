__author__ = 'cmaran'

from OpenGL.GL import *

class Light:
    """
    Licht Klasse
    """
    light_position = None
    light_ambient = None
    light_specular = None
    light_diffuse = None



    def __init__(self, light_position, light_ambient, light_specular, light_diffuse):
        """
        Erstellt das Licht
        :param light_position: (x, y, z, w) position of light
        :param light_ambient: ambient RGBA intensity of light
        :param light_specular: specular RGBA intensity of light
        :param light_diffuse: diffuse RGBA intensity of light
        :return:
        """
        self.light_ambient = light_ambient
        self.light_diffuse = light_diffuse
        self.light_position = light_position
        self.light_specular = light_specular

        glEnable(GL_LIGHTING)
        glEnable(GL_NORMALIZE)
        glEnable(GL_LIGHT0)
        glLight(GL_LIGHT0, GL_POSITION, self.light_position)
        glLight(GL_LIGHT0, GL_AMBIENT, self.light_ambient)
        glLight(GL_LIGHT0, GL_SPECULAR, self.light_specular)
        glLight(GL_LIGHT0, GL_DIFFUSE, self.light_diffuse)