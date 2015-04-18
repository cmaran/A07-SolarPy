__author__ = 'cmaran'

from OpenGL.GL import *
from OpenGL.GLU import *
from sphere.Sphere import Sphere

class Planet(Sphere):


    def __init__(self, radius, sphere, image, slicesSubDiv, stacksSubDiv):
        """
        Erstellt den Planeten

        :param radius: Radius der Sphere
        :param sphere: Spherentyp
        :param image:  Das Image wird als Textur geladen
        :param slicesSubDiv: Gibt die Anzahl der Subdivisions um die z-Achse an (L&auml;ngengrad)
        :param stacksSubDiv: Gibt die Anzahl der Subdivisions um die z-Achse an (Breitengrad)
        :return:
        """
        texture = image.get_texture()   #bekommt die uebergebene Textur
        glBindTexture(texture.target, texture.id)   #Bindet diese auf das Objekt
        gluSphere(sphere, radius, slicesSubDiv, stacksSubDiv)


    def setRotation(self, angle, x, y, z):
        glRotatef(angle, x, y, z)

    def setPosition(self,  x, y, z):
        glTranslatef(x, y, z)