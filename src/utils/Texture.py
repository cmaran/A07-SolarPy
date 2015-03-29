__author__ = 'cmaran'

from OpenGL.GL import *
import pyglet.image
from pyglet.gl import *

class Texture:
    """
    Um mehrfaches Laden der Textur zu vermeiden wird diese davor in einem Textur-Objekt geladen und dort in ein Attribut abglegt
    """

    sunTexture = None
    venusTexture = None
    earthTexture = None
    moonTexture = None

    def load(self, file):
        """
        Laedt die Textur
        :param file: Textur-File
        :return:
        """
        image = pyglet.image.load(file)
        return image

    def setup(self):
        """
        Aktiviert die Textur und speichert diese in ein Attribut
        :return:
        """
        glEnable(GL_TEXTURE_2D)
        self.sunTexture = self.load("texture_sun.jpg")
        self.venusTexture = self.load("texture_venus_surface.jpg")
        self.earthTexture = self.load("texture_earth_clouds.jpg")
        self.moonTexture = self.load("texture_moon.jpg")

