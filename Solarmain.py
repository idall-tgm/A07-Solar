__author__ = 'Berni'

import sys
from Solarwindow import solarwindow
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from SolarTexture import solarTexture
from Solarsun import solarsun
from SolarPlanet import solarplanet
from SolarLight import solarLight


class Solarmain:

    def main():
        modestatus = 1
        lighting = False
        speed = 1
        yrot = speed
        distanceset = 0
        textureon = True
        lightingon = True
        cammode = 1

        pygame.init()

        window = solarwindow()
        window.setupsplash(1280,720)

        textures = solarTexture()

        planets = solarplanet()

        light = solarLight()

        while True:
            if modestatus == 1:
                window.screen.blit(window.splashscreen, (0, 0))

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    elif event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            modestatus = 2

                pygame.time.wait(1)

            elif modestatus == 2:
                window.setupgl()

                glEnable(GL_TEXTURE_2D)

                sphere = gluNewQuadric()
                gluQuadricNormals(sphere, GL_FLAT)
                gluQuadricTexture(sphere, GL_TRUE)

                textures.setupTexture()
                light.setupLight()

                modestatus = 3

            elif modestatus == 3:

                if distanceset == 0 and cammode == 1:
                    gluLookAt(0,0,7,0,0,0,0,1,0)
                    distanceset = 1
                elif distanceset == 0 and cammode == 2:
                    gluLookAt(0,5,7,0,0,0,0,1,0)
                    distanceset = 1

                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

                glPushMatrix()
                glRotatef(yrot, 0, 1, 0)
                if lightingon:
                    glDisable(GL_LIGHTING)
                planets.sun(1, sphere, textures.suntexture)
                if lightingon:
                    glEnable(GL_LIGHTING)
                glPopMatrix()

                glPushMatrix()
                glRotatef(4.5 * yrot, 0, 1, 0.3)
                glTranslatef(2, 0, 0)
                planets.planet(0.035, sphere, textures.merkurtexture)
                glPopMatrix()

                glPushMatrix()
                glRotatef(1.6 * yrot, 0, 1, 0.3)
                glTranslatef(3, 0, 0)
                planets.planet(0.086, sphere, textures.venustexture)
                glPopMatrix()

                glPushMatrix()
                glRotatef(yrot, 0, 1, 0.3)
                glTranslatef(4, 0, 0)
                glRotatef(yrot*3, 0, 1, 0)
                planets.planet(0.091, sphere, textures.erdetexture)

                glRotatef(-yrot*5, 0, 1, 0)
                glRotatef(12 * yrot, 0, 1, 0)
                glTranslatef(0.2, 0, 0.1)
                planets.moon(0.025, sphere, textures.merkurtexture)
                glPopMatrix()

                glPushMatrix()
                glRotatef(yrot / 2, 0, 1, 0.3)
                glTranslatef(5, 0, 0)
                planets.planet(0.049, sphere, textures.marstexture)
                glPopMatrix()

                glPushMatrix()
                glRotatef(yrot / 12, 0, 1, 0.3)
                glTranslatef(7, 0, 0)
                planets.planet(0.102, sphere, textures.jupitertexture)
                glPopMatrix()

                glPushMatrix()
                glRotatef(yrot / 30, 0, 1, 0.3)
                glTranslatef(9, 0, 0)
                planets.planet(0.086, sphere, textures.saturntexture)
                glPopMatrix()

                glPushMatrix()
                glRotatef(yrot / 84, 0, 1, 0.3)
                glTranslatef(11, 0, 0)
                planets.planet(0.037, sphere, textures.uranustexture)
                glPopMatrix()

                glPushMatrix()
                glRotatef(yrot / 164, 0, 1, 0.3)
                glTranslatef(12, 0, 0)
                planets.planet(0.035, sphere, textures.neptuntexture)
                glPopMatrix()

                yrot += speed


                pygame.time.wait(10)

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    elif event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            modestatus = 4
                            distanceset = 0
                        if event.key == pygame.K_RIGHT and speed < 5:
                            speed += 0.5
                        if event.key == pygame.K_LEFT and speed > 0:
                            speed -= 0.5

                        if event.key == pygame.K_UP and cammode == 1:
                            cammode = 2
                            glLoadIdentity()

                            gluPerspective(window.fov, (window.size[0] / window.size[1]), 0.1, 100)
                            distanceset = 0

                        if event.key == pygame.K_DOWN and cammode == 2:
                            cammode = 1
                            glLoadIdentity()

                            gluPerspective(window.fov, (window.size[0] / window.size[1]), 0.1, 100)
                            distanceset = 0


                    elif event.type == MOUSEBUTTONDOWN:
                        if event.button == 4 and window.fov > 50:
                            window.fov -= 5
                            glLoadIdentity()

                            gluPerspective(window.fov, (window.size[0] / window.size[1]), 1.0, 100)
                            distanceset = 0

                        elif event.button == 5 and window.fov < 150:
                            window.fov += 5
                            glLoadIdentity()
                            gluPerspective(window.fov, (window.size[0] / window.size[1]), 1.0, 100)
                            distanceset = 0

                        elif event.button == 1 and textureon == True:
                            glDisable(GL_TEXTURE_2D)
                            textureon = False
                        elif event.button == 1 and textureon == False:
                            glEnable(GL_TEXTURE_2D)
                            textureon = True

                        elif event.button == 3 and lightingon == True:
                            glDisable(GL_LIGHTING)
                            lightingon = False
                        elif event.button == 3 and lightingon == False:
                            glEnable(GL_LIGHTING)
                            lightingon = True

                glFlush()


            elif modestatus == 4:
                window.resetup()
                modestatus = 1



            pygame.display.flip()



Solarmain.main()