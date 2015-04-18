__author__ = 'cmaran'

from OpenGL.GL import *
from OpenGL.GLU import *
from sphere.Sphere import Sphere

class Moon(Sphere):

    def __init__(self, radius, sphere, image, slicesSubDiv, stacksSubDiv):
        """
        Erstellt den Mond

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

