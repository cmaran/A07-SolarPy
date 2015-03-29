__author__ = 'cmaran'

from OpenGL.GL import *
import pyglet.image
from pyglet.gl import *

class Texture:

    sunTexture = None
    mercuryTexture = None
    venusTexture = None
    earthTexture = None
    marstexTure = None
    jupiterTexture = None
    saturnTexture = None
    uranusTexture = None
    neptunTexture = None
    moonTexture = None

    def loadTexture(self, filename):
        image = pyglet.image.load(filename)
        return image

    def setupTexture(self):
        glEnable(GL_TEXTURE_2D)

        self.sunTexture = self.loadTexture("texture_sun.jpg")
        self.mercuryTexture = self.loadTexture("texture_mercury.jpg")
        self.venusTexture = self.loadTexture("texture_venus_surface.jpg")
        self.earthTexture = self.loadTexture("texture_earth_clouds.jpg")
        self.marsTexture = self.loadTexture("texture_mars.jpg")
        self.jupiterTexture = self.loadTexture("texture_jupiter.jpg")
        self.saturnTexture = self.loadTexture("texture_saturn.jpg")
        self.uranusTexture = self.loadTexture("texture_uranus.jpg")
        self.neptunTexture = self.loadTexture("texture_neptune.jpg")
        self.moonTexture = self.loadTexture("texture_moon.jpg")

