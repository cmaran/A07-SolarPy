__author__ = 'cmaran'

from abc import ABCMeta, abstractmethod

class Sphere:
    """
    Abstrakte Klasse Sphere
    """

    @abstractmethod
    def setUp(self, radius, sphere, image, slicesSubDiv, stacksSubDiv):
        """
        setUp muss von den Subclasses implementiert werden, sonst wird eine Exception geworfen
        :param radius: Radius der Sphere
        :param sphere: Spherentyp
        :param image:  Das Image wird als Textur geladen
        :param slicesSubDiv: Gibt die Anzahl der Subdivisions um die z-Achse an (L&auml;ngengrad)
        :param stacksSubDiv: Gibt die Anzahl der Subdivisions um die z-Achse an (Breitengrad)
        :return:
        """
        raise NotImplementedError()

