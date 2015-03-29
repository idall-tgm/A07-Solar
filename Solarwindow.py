__author__ = 'Berni'

import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class solarwindow:

    screen = None
    splashscreen = None
    size = None
    fov = 105

    def setupsplash(self, sizex, sizey):

        self.size = width, height = sizex, sizey

        self.splashscreen = pygame.image.load('SunsystemSplash.jpg')
        self.splashscreen = pygame.transform.scale(self.splashscreen, self.size)

        icon = pygame.image.load('SunsystemSplash.jpg')
        icon = pygame.transform.scale(icon, (32, 32))
        pygame.display.set_icon(icon)

        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Solar-System")

    def setupgl(self):
        self.screen = pygame.display.set_mode(self.size, DOUBLEBUF | OPENGL)

        gluPerspective(self.fov, (self.size[0] / self.size[1]), 1.0, 100.0)

    def resetup(self):
        self.screen = pygame.display.set_mode(self.size)

