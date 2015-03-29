__author__ = 'Berni'

from OpenGL.GL import *
import pyglet.image
from pyglet.gl import *

class Texture:

    suntexture = None
    merkurtexture = None
    venustexture = None
    erdetexture = None
    marstexture = None
    jupitertexture = None
    saturntexture = None
    uranustexture = None
    neptuntexture = None

    def loadTexture(self, filename):
        image = pyglet.image.load(filename)
        return image

    def setupTexture(self):
        glEnable(GL_TEXTURE_2D)

        self.suntexture = self.loadTexture("texture_sun.jpg")
        self.merkurtexture = self.loadTexture("texture_mercury.jpg")
        self.venustexture = self.loadTexture("texture_venus_surface.jpg")
        self.erdetexture = self.loadTexture("texture_earth_clouds.jpg")
        self.marstexture = self.loadTexture("texture_mars.jpg")
        self.jupitertexture = self.loadTexture("texture_jupiter.jpg")
        self.saturntexture = self.loadTexture("texture_saturn.jpg")
        self.uranustexture = self.loadTexture("texture_uranus.jpg")
        self.neptuntexture = self.loadTexture("texture_neptune.jpg")

