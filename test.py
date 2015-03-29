__author__ = 'Berni'

import sys
import pygame


pygame.init()

splashscreen = pygame.image.load('SunsystemSplash.jpg')
splashscreen = pygame.transform.scale(splashscreen, (1280, 720))

icon = pygame.image.load('SunsystemSplash.jpg')
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)

size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Solar-System")


while True:
    screen.blit(splashscreen, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.time.wait(1)

    pygame.display.flip()
