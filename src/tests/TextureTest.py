__author__ = 'cmaran'

import unittest
from OpenGL.GL import *
from OpenGL.GLU import *
from utils.Light import Light
from window.Window import Window
from utils.Texture import Texture
from sphere.Sun import Sun

import pyglet.image
from pyglet.gl import *

class TextureTest(unittest.TestCase):
    def test_texture(self):
        window = Window()
        window.setupsplash(1000,1000)
        window.setupgl()
        sunTexture = Texture("texture_sun.jpg")
        sphere = gluNewQuadric()
        gluQuadricNormals(sphere, GL_FLAT)
        gluQuadricTexture(sphere, GL_TRUE)
        sun = Sun(1, sphere, sunTexture.texture, 50, 50)
        if glIsEnabled(GL_TEXTURE_2D) == GL_TRUE:
            self.assertEqual(1, 1)
            self.assertEqual(sunTexture, sun.texture)

if __name__ == '__main__':
    unittest.main()
