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

def Cube():
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

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def Sphere1(radius):
    glEnable(GL_TEXTURE_2D)
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

    sphere = gluNewQuadric()
    #glColor4f(1,1,0.2,1)
    gluSphere(sphere, radius, 100, 100)
    glDisable(GL_TEXTURE_2D)





def load_Texture():

    #global texture
    glEnable(GL_TEXTURE_2D)
    image = pyglet.image.load('sonne.png')


   # ix = image.width
   # iy = image.height
    rawimage = image.get_image_data()
    format = 'RGBA'
    pitch = rawimage.width * len(format)
    image = rawimage.get_data(format,pitch)

    texture = image.get_texture()
    glEnable(texture.target)
    glBindTexture(texture.target, texture.id)

    '''
    #Create Texture
    textures = glGenTextures(3)
    glBindTexture(GL_TEXTURE_2D, int(textures[0]))   # 2d texture (x and y size)


    # Create Linear Filtered Texture
    glBindTexture(GL_TEXTURE_2D, int(textures[1]))
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)


    # Create MipMapped Texture
    glBindTexture(GL_TEXTURE_2D, int(textures[2]))
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_NEAREST)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 3,ix,iy, GL_RGBA, GL_UNSIGNED_BYTE, image)
'''
    sphere = gluNewQuadric()
    gluQuadricNormals(sphere,GLU_SMOOTH)
    gluQuadricTexture(sphere,GL_TRUE)

    '''
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
    '''

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

            gluPerspective(fov, (size[0] / size[1]), 0.1, 50.0)

            glTranslatef(0.0, 0.0, -5)


            modestatus = 3




        elif modestatus == 3:

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glPushMatrix()

            glRotatef(yrot,0,1,0)

            Sphere1(1)
            #Cube()
            glPopMatrix()

            glPushMatrix()
            glRotatef(4.5*yrot,0,1,0.2)
            glTranslatef(2,0,0)
            Sphere1(0.035)
            glPopMatrix()

            glPushMatrix()
            glRotatef(1.6*yrot,0,1,0.2)
            glTranslatef(3,0,0)
            Sphere1(0.086)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot,0,1,0.2)
            glTranslatef(4,0,0)
            Sphere1(0.091)

            glTranslatef(0.1,0,0)
            glRotatef(12*yrot,0,1,0.2)
            Sphere1(0.025)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot/2,0,1,0.2)
            glTranslatef(5,0,0)
            Sphere1(0.049)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot/12,0,1,0.2)
            glTranslatef(7,0,0)
            Sphere1(0.102)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot/30,0,1,0.2)
            glTranslatef(9,0,0)
            Sphere1(0.086)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot/84,0,1,0.2)
            glTranslatef(11,0,0)
            Sphere1(0.037)
            glPopMatrix()

            glPushMatrix()
            glRotatef(yrot/164,0,1,0)
            glTranslatef(12,0,0)
            Sphere1(0.035)
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

                    elif event.button == 5 and fov < 150:
                        fov += 5


        elif modestatus == 4:
            screen = pygame.display.set_mode(size)
            modestatus = 1


        pygame.display.flip()


main()