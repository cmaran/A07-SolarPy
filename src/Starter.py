__author__ = 'cmaran'

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


mode = 1    #Modus um zwischen den Anzeigen(Splashscreen->OpenGl) zu, welchsen
speed = 1   #Standardgeschwindigkeit
rotation = speed #Rotationsgeschwindigkeit
distance = 0
lightOn = True  #Flag fürs Lighting
animation = True    #Flag um die Animation zu starten/stoppen
view = 1        #Kameraview (default: 1)

pygame.init()
window = Window()
window.setup(1650, 1050)    #Setzt die Fenstergröße fest
textures = Texture()
sun = Sun()
planets = Planet()
moon = Moon()
light = Light()

while True:
    if mode == 1:
        """
        Modus 1:
        Splashscreen
        Keybindings:
        ESC-> Um das Fenster zu schließen
        ENTER->Um zur OpenGl View zu wechseln
        """
        window.screen.blit(window.splash
                           , (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    mode = 2
        pygame.time.wait(1)

    elif mode == 2:
        """
        Modus 2:
        Lädt die Texturen
        Erzeugt die Spheren-Matrix
        Und lädt das Licht
        """
        window.setupGL()
        glEnable(GL_TEXTURE_2D)
        textures.setup()
        light.setup()
        sphere = gluNewQuadric()
        gluQuadricNormals(sphere, GL_FLAT)
        gluQuadricTexture(sphere, GL_TRUE)
        mode = 3

    elif mode == 3:
        """
        Modus 3:
        Planetenmodell
        Keybindings:
        ESC-> Um das Fenster zu schließen
        PFEIL RECHTS-> Rotationsgeschwindigkeit erhöhen
        PFEIL LINKS -> Rotationsgeschwindigkeit verringern
        S -> Animation stoppen/starten
        L -> Lighting an/aus
        1 -> Kameraview Seite
        2 -> Kameraview Oben
        """
        textures.setup()
        light.setup()
        rotation += speed

        #setzen der Kameraview 1
        if distance == 0 and view == 1:
            gluLookAt(1, 5, 1, 0, 0, 0, 0, 1, 0)
            distance = 1
        #setzen der Kameraview 2
        elif distance == 0 and view == 2:
            gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
            distance = 1
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix() #Setzen der Sonne
        glRotatef(rotation, 0, 1, 0)
        if lightOn:
            glDisable(GL_LIGHTING)
        sun.setUp(1, sphere, textures.sunTexture, 50, 50)
        if lightOn:
            glEnable(GL_LIGHTING)
        glPopMatrix()

        #Setzen des Planet 1
        glPushMatrix()
        glRotatef(1.6 * rotation, 0, 1, 0.3)
        glTranslatef(3, 0, 0)
        planets.setUp(0.085, sphere, textures.venusTexture, 50, 50)
        glPopMatrix()

        #Setzen der Planet 2
        glPushMatrix()
        glRotatef(rotation, 0, 1, 0.3)
        glTranslatef(4, 0, 0)
        glRotatef(rotation * 3, 0, 1, 0)
        planets.setUp(0.09, sphere, textures.earthTexture, 50, 50)

        #Setzen der Mond
        glRotatef(rotation * 2, 0, 1, 0)
        glRotatef(7 * rotation, 0, 1, 0)
        glTranslatef(0.2, 0, 0.1)
        moon.setUp(0.025, sphere, textures.moonTexture, 50, 50)
        glPopMatrix()


        pygame.time.wait(1)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    mode = 4
                    distance = 0
                if event.key == pygame.K_RIGHT and speed < 5:
                    speed += 0.1
                if event.key == pygame.K_LEFT and speed >= 0:
                    speed -= 0.1

                if event.key == pygame.K_s:
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
                    gluPerspective(window.fieldOfView, (window.size[0] / window.size[1]), 0.1, 100)
                    distance = 0

                if event.key == pygame.K_2 and view == 2:
                    view = 1
                    glLoadIdentity()
                    gluPerspective(window.fieldOfView, (window.size[0] / window.size[1]), 0.1, 100)
                    distance = 0

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 4 and window.fieldOfView > 0:
                    window.fieldOfView -= 5
                    glLoadIdentity()
                    gluPerspective(window.fieldOfView, (window.size[0] / window.size[1]), 1.0, 100)
                    distance = 0

                elif event.button == 5 and window.fieldOfView < 500:
                    window.fieldOfView += 5
                    glLoadIdentity()
                    gluPerspective(window.fieldOfView, (window.size[0] / window.size[1]), 1.0, 100)
                    distance = 0
        glFlush()


    pygame.display.flip() #Aktualisiert die Anzeige auf die Bildschirmoberfläche


