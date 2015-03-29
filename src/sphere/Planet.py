__author__ = 'cmaran'

from OpenGL.GL import *
from OpenGL.GLU import *
from sphere.Sphere import Sphere

class Planet(Sphere):

    def setUp(self, radius, sphere, image):
        texture = image.get_texture()
        glBindTexture(texture.target, texture.id)
        gluSphere(sphere, radius, 50, 50)
