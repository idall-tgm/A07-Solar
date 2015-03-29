__author__ = 'Berni'

from OpenGL.GL import *
import pyglet.image
from pyglet.gl import *

class solarTexture:

    suntexture = None
    merkurtexture = None
    venustexture = None
    erdetexture = None
    marstexture = None
    jupitertexture = None
    saturntexture = None
    uranustexture = None
    neptuntexture = None

    def loadTexture(self, filename):
        image = pyglet.image.load(filename)
        return image

    def setupTexture(self):
        glEnable(GL_TEXTURE_2D)

        self.suntexture = self.loadTexture("sonne.png")
        self.merkurtexture = self.loadTexture("merkur.jpg")
        self.venustexture = self.loadTexture("venus.jpg")
        self.erdetexture = self.loadTexture("erde.jpg")
        self.marstexture = self.loadTexture("mars.jpg")
        self.jupitertexture = self.loadTexture("jupiter.jpg")
        self.saturntexture = self.loadTexture("saturn.jpg")
        self.uranustexture = self.loadTexture("uranus.jpg")
        self.neptuntexture = self.loadTexture("neptun.jpg")

