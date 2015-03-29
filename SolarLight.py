__author__ = 'Berni'

from OpenGL.GL import *

class solarLight:

    def setupLight(self):
        glEnable(GL_LIGHTING)

        glEnable(GL_NORMALIZE)

        glEnable(GL_LIGHT0)

        light_position1 = [0, 1, 0, 0]
        glLight(GL_LIGHT0, GL_POSITION, light_position1)

        light_color = [1, 1, 1, 0.5]
        glLight(GL_LIGHT0, GL_AMBIENT, light_color)