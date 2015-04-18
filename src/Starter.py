__author__ = 'cmaran'

import sys

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from window.Window import Window
from utils.Texture import Texture
from utils.Light import Light
from utils.CamView import CamView
from sphere.Sun import Sun
from sphere.Planet import Planet
from sphere.Moon import Moon


mode = 1  # Modus um zwischen den Anzeigen(Splashscreen->OpenGl) zu, welchsen
speed = 0.2  # Standardgeschwindigkeit
rotation = speed  # Rotationsgeschwindigkeit
distance = 0
lightOn = True  # Flag fürs Lighting
animation = True  # Flag um die Animation zu starten/stoppen
view = 1  # Kameraview (default: 1)

pygame.init()
window = Window(1650, 1050, 100, 'splashscreen_v1.jpg')

sunTexture = Texture("texture_sun.jpg")
mercuryTexture = Texture("texture_mercury.jpg")
venusTexture = Texture("texture_venus_surface.jpg")
earthTexture = Texture("texture_earth_clouds.jpg")
moonTexture = Texture("texture_moon.jpg")
marsTexture = Texture("texture_mars.jpg")
jupiterTexture = Texture("texture_jupiter.jpg")
saturnTexture = Texture("texture_saturn.jpg")
uranusTexture = Texture("texture_uranus.jpg")
neptuneTexture = Texture("texture_neptune.jpg")

sun = None
mercury = None
venus = None
earth = None
moon = None
mars = None
jupiter = None
saturn = None
uranus = None
neptune = None

light = None
perspective1 = None
perspective2 = None

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
                    window.setupGL()
                    glEnable(GL_TEXTURE_2D)

                    mode = 2
        pygame.time.wait(1)

    elif mode == 2:
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
        sphere = gluNewQuadric()
        gluQuadricNormals(sphere, GL_FLAT)
        gluQuadricTexture(sphere, GL_TRUE)
        light = Light([0, 1, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1])
        rotation += speed

        # setzen der Kameraview 1
        if distance == 0 and view == 1:
            perspective1 = CamView(1, 5, 1, 0, 0, 0, 0, 1, 0)
            distance = 1
        #setzen der Kameraview 2
        elif distance == 0 and view == 2:
            perspective2 = CamView(0, 0, 10, 0, 0, 0, 0, 1, 0)
            distance = 1
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()  #Setzen der Sonne
        glRotatef(rotation, 0, 1, 0)

        if lightOn:
            glDisable(GL_LIGHTING)  #Licht aus damit die Sonne keinen Schatten wirft :)
        sun = Sun(1, sphere, sunTexture.texture, 50, 50)
        if lightOn:
            glEnable(GL_LIGHTING)
        glPopMatrix()

        #Setzen des Merkurs
        glPushMatrix()
        glRotatef(1.7 * rotation, 0, 1, 0)
        glTranslatef(2, 0, 0)
        mercury = Planet(0.04, sphere, mercuryTexture.texture, 50, 50)
        glPopMatrix()

        #Setzen der Venus
        glPushMatrix()
        glRotatef(1.6 * rotation, 0, 1, 0)
        glTranslatef(3, 0, 0)
        venus = Planet(0.085, sphere, venusTexture.texture, 50, 50)
        glPopMatrix()

        #Setzen der Erde
        glPushMatrix()
        glRotatef(1.5 * rotation, 0, 1, 0)
        glTranslatef(4, 0, 0)
        earth = Planet(0.09, sphere, earthTexture.texture, 50, 50)

        #Setzen des Monds
        glRotatef(5 * rotation, 0, 1, 0)
        glTranslatef(0.2, 0, 0)
        moon = Moon(0.03, sphere, moonTexture.texture, 50, 50)
        glPopMatrix()

        #Setzen des Mars
        glPushMatrix()
        glRotatef(1.4 * rotation, 0, 1, 0)
        glTranslatef(5, 0, 0)
        mars = Planet(0.05, sphere, marsTexture.texture, 50, 50)
        glPopMatrix()

        #Setzen des Jupiters
        glPushMatrix()
        glRotatef(1.3 * rotation, 0, 1, 0)
        glTranslatef(6, 0, 0)
        jupiter = Planet(0.25, sphere, jupiterTexture.texture, 50, 50)
        glPopMatrix()

        #Setzen des Saturns
        glPushMatrix()
        glRotatef(1.2 * rotation, 0, 1, 0)
        glTranslatef(7, 0, 0)
        saturn = Planet(0.2, sphere, saturnTexture.texture, 50, 50)
        glPopMatrix()

        #Setzen des Uranus
        glPushMatrix()
        glRotatef(1.1 * rotation, 0, 1, 0)
        glTranslatef(8, 0, 0)
        uranus = Planet(0.12, sphere, uranusTexture.texture, 50, 50)
        glPopMatrix()

        #Setzen des Neptuns
        glPushMatrix()
        glRotatef(1 * rotation, 0, 1, 0)
        glTranslatef(9, 0, 0)
        neptune = Planet(0.1, sphere, neptuneTexture.texture, 50, 50)
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

    pygame.display.flip()  #Aktualisiert die Anzeige auf die Bildschirmoberfläche


