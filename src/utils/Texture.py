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

    def loadTexture(self, filename):
        """
        Laedt die Textur
        :param filename: Textur-File
        :return:
        """
        image = pyglet.image.load(filename)
        return image

    def setupTexture(self):
        """
        Aktiviert die Textur und speichert diese in ein Attribut
        :return:
        """
        glEnable(GL_TEXTURE_2D)
        self.sunTexture = self.loadTexture("texture_sun.jpg")
        self.venusTexture = self.loadTexture("texture_venus_surface.jpg")
        self.earthTexture = self.loadTexture("texture_earth_clouds.jpg")
        self.moonTexture = self.loadTexture("texture_moon.jpg")

