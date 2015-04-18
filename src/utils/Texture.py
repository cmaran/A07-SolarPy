__author__ = 'cmaran'

from OpenGL.GL import *
import pyglet.image
from pyglet.gl import *

class Texture:
    """
    Um mehrfaches Laden der Textur zu vermeiden wird diese davor in einem Textur-Objekt geladen und dort in ein Attribut abglegt
    """

    texture = None

    def __init__(self, texture):
        """
        Aktiviert die Textur und speichert diese in ein Attribut
        :return:
        """
        glEnable(GL_TEXTURE_2D)
        self.texture = self.load(texture)


    def load(self, file):
        """
        Laedt die Textur
        :param file: Textur-File
        :return:
        """
        image = pyglet.image.load(file)
        return image

