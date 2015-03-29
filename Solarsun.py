__author__ = 'Berni'

from OpenGL.GL import *
from OpenGL.GLU import *

class solarsun:

    def sun(self, radius, sphere, image):
        texture = image.get_texture()
        glBindTexture(texture.target, texture.id)

        gluSphere(sphere, radius, 50, 50)