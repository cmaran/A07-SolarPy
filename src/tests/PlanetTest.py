__author__ = 'cmaran'

import unittest
from OpenGL.GLU import *
from OpenGL.GLU import *
from utils.Light import Light
from window.Window import Window
from utils.Texture import Texture
from sphere.Planet import Planet

class PlanetTest(unittest.TestCase):
    def test_something(self):
        window = Window()
        window.setupsplash(1000,1000)
        window.setupgl()
        earthTexture = Texture("texture_sun.jpg")
        sphere = gluNewQuadric()
        gluQuadricNormals(sphere, GL_FLAT)
        gluQuadricTexture(sphere, GL_TRUE)
        earth = Planet(1, sphere, earthTexture.texture, 50, 50)
        earth2 = Planet(1, sphere, earthTexture.texture, 50, 50)
        self.assertEqual(earth, earth2)


if __name__ == '__main__':
    unittest.main()
