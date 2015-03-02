__author__ = 'cmaran'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from logging import warning
sphere_locations = [(0, 0)]

def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 100.0, 0.0, 100.0)
    glEnable(GL_DEPTH_TEST)                              


def on_click(button, state, x, y):
    global sphere_locations
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        warning("CLICK")
        sphere_locations.append((x, y))


def display():
    global sphere_locations
    warning(sphere_locations)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for x, y in sphere_locations:
        glPushMatrix()
        glTranslatef(x, y, 1.0)
        glColor3f(0.0, 1.0, 0.0)
        glutSolidSphere(0.3, 250, 250)
        glPopMatrix()
    glFlush()
    glutSwapBuffers()
    glutPostRedisplay()



glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH )
glutInitWindowSize(550, 550)
glutInitWindowPosition(50, 50)
glutCreateWindow("Bubble Pop")
glutDisplayFunc(display)
glutMouseFunc(on_click)
init()
glutMainLoop()