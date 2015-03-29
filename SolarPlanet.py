__author__ = 'Berni'

from OpenGL.GL import *
from OpenGL.GLU import *

class solarplanet:

    def planet(self, radius, sphere, image):

        texture = image.get_texture()
        glBindTexture(texture.target, texture.id)

        gluSphere(sphere, radius, 20, 20)

    def sun(self, radius, sphere, image):
        texture = image.get_texture()
        glBindTexture(texture.target, texture.id)

        gluSphere(sphere, radius, 50, 50)

    def moon(self, radius, sphere, image):
        texture = image.get_texture()
        glBindTexture(texture.target, texture.id)

        gluSphere(sphere, radius, 15, 15)