from pygame.constants import *

__author__ = 'Berni'

import pygame
import sys

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import pyglet.image
from pyglet.gl import *

def Sphere1(radius, sphere):
    image=pyglet.image.load("sonne.png")
    texture = image.get_texture()
    glEnable(texture.target)
    glBindTexture(texture.target, texture.id)

    '''
    rawimage = image.get_image_data()
    format = 'RGBA'
    pitch = rawimage.width * len(format)
    image = rawimage.get_data(format,pitch)
    '''


    #glColor4f(1,1,0.2,1)
    gluSphere(sphere, radius, 20, 20)
    glDisable(GL_TEXTURE_2D)


def Sphere2(radius, sphere):



    '''
    rawimage = image.get_image_data()
    format = 'RGBA'
    pitch = rawimage.width * len(format)
    image = rawimage.get_data(format,pitch)
    '''

    #glColor4f(1,1,0.2,1)
    gluSphere(sphere, radius, 20, 20)
    glDisable(GL_TEXTURE_2D)

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

    changed = False
    fov = 105
    speed = 1
    modestatus = 1
    yrot = speed
    distanceset = 0

    pygame.init()

    icon = pygame.image.load("SunsystemSplash.jpg")
    icon = pygame.transform.scale(icon, (32, 32))
    pygame.display.set_icon(icon)

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

            #setupLighting()

            gluPerspective(fov, (size[0] / size[1]), 0.1, 100.0)

            glEnable(GL_TEXTURE_2D)

            sphere = gluNewQuadric()
            gluQuadricNormals(sphere,GLU_SMOOTH)
            gluQuadricTexture(sphere,GL_TRUE)

            modestatus = 3




        elif modestatus == 3:

            if distanceset == 0:
                glTranslatef(0.0, 0.0, -7)
                distanceset = 1

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glPushMatrix()

            glRotatef(yrot,0,1,0)

            Sphere1(1,sphere)

            glPopMatrix()

            glPushMatrix()
            glRotatef(4.5*yrot,0,1,0.3)
            glTranslatef(2,0,0)
            Sphere2(0.035,sphere)
            glPopMatrix()

            glPushMatrix()
            glRotatef(1.6*yrot,0,1,0.3)
            glTranslatef(3,0,0)
            Sphere2(0.086,sphere)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot,0,1,0.3)
            glTranslatef(4,0,0)
            Sphere2(0.091,sphere)

            glTranslatef(0.2,0,0)
            glRotatef(12*yrot,0,1,0.3)
            Sphere2(0.025,sphere)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot/2,0,1,0.3)
            glTranslatef(5,0,0)
            Sphere2(0.049,sphere)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot/12,0,1,0.3)
            glTranslatef(7,0,0)
            Sphere2(0.102,sphere)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot/30,0,1,0.3)
            glTranslatef(9,0,0)
            Sphere2(0.086,sphere)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot/84,0,1,0.3)
            glTranslatef(11,0,0)
            Sphere2(0.037,sphere)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot/164,0,1,0.3)
            glTranslatef(12,0,0)
            Sphere2(0.035,sphere)
            glPopMatrix()

            yrot += speed


            pygame.time.wait(10)



            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        modestatus = 4
                    if event.key == pygame.K_RIGHT and speed < 5:
                        speed += 0.5
                    if event.key == pygame.K_LEFT and speed > 0:
                        speed -= 0.5

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 4 and fov > 50:
                        fov -= 5
                        glLoadIdentity()

                        gluPerspective(fov, (size[0] / size[1]), 0.1, 50.0)
                        distanceset = 0

                    elif event.button == 5 and fov < 150:
                        fov += 5
                        glLoadIdentity()
                        gluPerspective(fov, (size[0] / size[1]), 0.1, 50.0)
                        distanceset = 0


        elif modestatus == 4:
            screen = pygame.display.set_mode(size)
            modestatus = 1


        pygame.display.flip()


main()