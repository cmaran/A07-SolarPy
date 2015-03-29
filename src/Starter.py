__author__ = 'Berni'

import sys

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from window.Window import Window
from utils.Texture import Texture
from sphere.Sun import Sun
from sphere.Planet import Planet
from utils.Light import Light
from sphere.Moon import Moon



mode = 1
speed = 1
rotation = speed
distance = 0
lightOn = True
animation = True
view = 1
i = 1

pygame.init()

window = Window()

window.setup(1650,1050)

textures = Texture()

sun = Sun()
planets = Planet()
moon = Moon()

light = Light()


while True:
    if mode == 1:
        window.screen.blit(window.splashscreen, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    mode = 2

        pygame.time.wait(1)

    elif mode == 2:
        window.setupGL()

        glEnable(GL_TEXTURE_2D)
        sphere = gluNewQuadric()
        gluQuadricNormals(sphere, GL_FLAT)
        gluQuadricTexture(sphere, GL_TRUE)
        textures.setupTexture()
        light.setupLight()

        mode = 3

    elif mode == 3:

        rotation += speed

        if distance == 0 and view == 1:
            gluLookAt(1,5,1,0,0,0,0,1,0)
            distance = 1
        elif distance == 0 and view == 2:
            gluLookAt(0,0,10,0,0,0,0,1,0)
            distance = 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glRotatef(rotation, 0, 1, 0)
        if lightOn:
            glDisable(GL_LIGHTING)
        sun.setUp(1, sphere, textures.sunTexture)
        if lightOn:
            glEnable(GL_LIGHTING)
        glPopMatrix()

        glPushMatrix()
        glRotatef(0.5 * rotation, 0, 1, 0.3)
        glTranslatef(2, 0, 0)
        planets.setUp(0.035, sphere, textures.mercuryTexture)
        glPopMatrix()

        glPushMatrix()
        glRotatef(1.6 * rotation, 0, 1, 0.3)
        glTranslatef(3, 0, 0)
        planets.setUp(0.085, sphere, textures.venusTexture)
        glPopMatrix()

        glPushMatrix()
        glRotatef(rotation, 0, 1, 0.3)
        glTranslatef(4, 0, 0)
        glRotatef(rotation*3, 0, 1, 0)
        planets.setUp(0.09, sphere, textures.earthTexture)

        glRotatef(-rotation*5, 0, 1, 0)
        glRotatef(12 * rotation, 0, 1, 0)
        glTranslatef(0.2, 0, 0.1)
        moon.setUp(0.025, sphere, textures.moonTexture)
        glPopMatrix()

        glPushMatrix()
        glRotatef(rotation / 2, 0, 1, 0.3)
        glTranslatef(5, 0, 0)
        planets.setUp(0.049, sphere, textures.marsTexture)
        glPopMatrix()

        glPushMatrix()
        glRotatef(rotation / 12, 0, 1, 0.3)
        glTranslatef(7, 0, 0)
        planets.setUp(0.302, sphere, textures.jupiterTexture)
        glPopMatrix()

        glPushMatrix()
        glRotatef(rotation / 30, 0, 1, 0.3)
        glTranslatef(9, 0, 0)
        planets.setUp(0.256, sphere, textures.saturnTexture)
        glPopMatrix()

        glPushMatrix()
        glRotatef(rotation / 84, 0, 1, 0.3)
        glTranslatef(11, 0, 0)
        planets.setUp(0.127, sphere, textures.uranusTexture)
        glPopMatrix()

        glPushMatrix()
        glRotatef(rotation / 164, 0, 1, 0.3)
        glTranslatef(12, 0, 0)
        planets.setUp(0.127, sphere, textures.neptunTexture)
        glPopMatrix()


        pygame.time.wait(1)



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    mode = 4
                    distance = 0
                if event.key == pygame.K_RIGHT and speed < 5:
                    speed += 0.1
                if event.key == pygame.K_LEFT and speed >= 0:
                    speed -= 0.1

                if event.key == pygame.K_s :
                    if animation == False:
                        animation = True
                        speed = 1
                    elif animation == True:
                        animation = False
                        speed = 0

                if event.key == pygame.K_l:
                    if lightOn == False:
                        glEnable(GL_LIGHTING)
                        lightOn = True
                    elif lightOn == True:
                        glDisable(GL_LIGHTING)
                        lightOn = False

                if event.key == pygame.K_1 and view == 1:
                    view = 2
                    glLoadIdentity()
                    gluPerspective(window.fov, (window.size[0] / window.size[1]), 0.1, 100)
                    distance = 0

                if event.key == pygame.K_2 and view == 2:
                    view = 1
                    glLoadIdentity()
                    gluPerspective(window.fov, (window.size[0] / window.size[1]), 0.1, 100)
                    distance = 0



            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 4 and window.fov > 0:
                    window.fov -= 5
                    glLoadIdentity()

                    gluPerspective(window.fov, (window.size[0] / window.size[1]), 1.0, 100)
                    distance = 0

                elif event.button == 5 and window.fov < 500:
                    window.fov += 5
                    glLoadIdentity()
                    gluPerspective(window.fov, (window.size[0] / window.size[1]), 1.0, 100)
                    distance = 0

        glFlush()


    elif mode == 4:
        window.reset()
        mode = 1

    pygame.display.flip()


