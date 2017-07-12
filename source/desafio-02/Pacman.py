from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math as mt

class Pacman:

    def __init__(self, size, maxAmplitude, speed = 40, color = [1, 1, 0]):
        self.__size = size
        self.__angle = 0
        self.__maxAmplitude = maxAmplitude
        self.__speed = speed
        self.__color = color
        
        # Starting the variables
        self.__starting()

    def __starting(self):
        self.__isOpen = True
        self.__actualAmplitude = self.__maxAmplitude
        self.__alpha = 0.0
        self.__dalpha = mt.pi / self.__speed
        self.__renderRange = (self.__speed * 2)

    def __calculateX(self):

        return self.__size * mt.cos(self.__alpha)
    
    def __calculateY(self):

        return self.__size * mt.sin(self.__alpha)

    def __calculateAlpha(self):

        return self.__alpha += self.__dalpha

    def __ôpenTheTcheka(self):
        if(self.__isOpen):
            self.__actualAmplitude += 1
            if(self.__actualAmplitude > 10):
                self.__isOpen = False
                self.__actualAmplitude -= 2
        else:
            self.__actualAmplitude -= 1
            if(self.__actualAmplitude < 0):
                self.__isOpen = True
                self.__actualAmplitude += 2
        
        return

    def changeSize(self, newSize):
        self.__size = newSize

        return

    def render(self):

        # glTranslatef(gCameraX, gCameraY, 0)

        x = self.__calculateX()
        y = self.__calculateY()

        glBegin(GL_TRIANGLES)

        for i in range(self.__maxAmplitude):
            __calculateAlpha()
            x = self.__calculateX()
            y = self.__calculateY()

        glColor3f(self.__color[0], self.__color[1], self.__color[2])

        for i in range(self.__renderRange - (self.__actualAmplitude * 2)):
            glVertex2f(x, y)
            glVertex2f(0.0, 0.0)
            __calculateAlpha()
            x = self.__calculateX()
            y = self.__calculateY()
            glVertex2f(x, y)

        glEnd()

        self.__ôpenTheTcheka()

        return