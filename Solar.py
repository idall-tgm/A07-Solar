from pygame.constants import *

__author__ = 'Berni'

import pygame
import sys
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def Sphere1():
    sphere = gluNewQuadric()
    glColor4f(1,1,0.2,1)
    gluSphere(sphere, 1.0, 100, 100)


def setupLighting():
    """ Initializing Lighting and Light0

	:return:
	"""
    zeros = (0.15, 0.15, 0.15, 0.3)
    ones = (1.0, 1.0, 1.0, 0.3)
    half = (0.5, 0.5, 0.5, 0.5)

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, zeros)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, half)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15)
    glLightfv(GL_LIGHT0, GL_AMBIENT, zeros)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, ones)
    glLightfv(GL_LIGHT0, GL_SPECULAR, half)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)

    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)
    glShadeModel(GL_SMOOTH)

def main():
    speed = 1
    modestatus = 1

    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Solar-System")

    splashscreen = pygame.image.load("SunsystemSplash.jpg")
    splashscreen = pygame.transform.scale(splashscreen, (1280, 720))

    while True:

        if modestatus == 1:

            screen.blit(splashscreen, (0, 0))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        modestatus = 2

            pygame.time.wait(1)

        elif modestatus == 2:
            screen = pygame.display.set_mode(size, DOUBLEBUF | OPENGL)

            gluPerspective(115, (size[0] / size[1]), 0.1, 50.0)

            glTranslatef(0.0, 0.0, -5)

            glRotatef(0, 0, 0, 0)

            modestatus = 3

        elif modestatus == 3:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glRotate(speed, 0, 2, 1)
            Sphere1()
            Cube()
            pygame.time.wait(10)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        modestatus = 4
                    if event.key == pygame.K_RIGHT:
                        speed += 0.5
                    if event.key == pygame.K_LEFT and speed > 0:
                        speed -= 0.5


        elif modestatus == 4:
            screen = pygame.display.set_mode(size)
            modestatus = 1


        pygame.display.flip()


main()