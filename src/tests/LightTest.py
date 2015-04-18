__author__ = 'cmaran'

import unittest
from OpenGL.GL import *
from utils.Light import Light
from window.Window import Window


class LightTest(unittest.TestCase):


    def testInit(self):
        light = Light([0, 1, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1])
        light2 = Light([0, 1, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1])

        self.assertEqual(light,light2)



if __name__ == '__main__':
    unittest.main()
