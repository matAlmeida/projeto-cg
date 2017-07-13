from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math as mt

class Pacman:

    def __init__(self, size, movSpeed = 4, mouthSpeed = 1,  color = [1, 1, 0]):
        self.__size = size
        self.__mouthDirection = 0
        self.__maxAmplitude = 10
        self.__mouthSpeed = mouthSpeed
        self.__movSpeed = movSpeed
        self.__color = color
        
        # Starting the variables
        self.__starting()

    def __starting(self):
        self.__isOpen = True
        self.__actualAmplitude = self.__maxAmplitude
        self.__initAlpha()        
        self.__renderRange = 80
        self.gCameraX = 0
        self.gCameraY = 0

    def __initAlpha(self):
        self.__alpha = 0.0
        self.__dalpha = mt.pi / 40

    def __calculateX(self):

        return self.__size * mt.cos(self.__alpha)
    
    def __calculateY(self):

        return self.__size * mt.sin(self.__alpha)

    def __calculateAlpha(self):
        self.__alpha += self.__dalpha
        
        return

    def __ôpenTheTcheka(self):
        if(self.__isOpen):
            self.__actualAmplitude += self.__mouthSpeed
            if(self.__actualAmplitude > 10):
                self.__isOpen = False
                self.__actualAmplitude -= 2
        else:
            self.__actualAmplitude -= self.__mouthSpeed
            if(self.__actualAmplitude < 0):
                self.__isOpen = True
                self.__actualAmplitude += 2
        
        return

    def changeSize(self, newSize):
        self.__size = newSize

        return

    def getSize(self):

        return self.__size

    def render(self):
        self.__initAlpha()

        self.__move()

        glTranslatef(self.gCameraX, self.gCameraY, 0)
        glRotatef(self.__mouthDirection, 0, 0, 1)

        x = self.__calculateX()
        y = self.__calculateY()

        glBegin(GL_TRIANGLES)

        for i in range(self.__actualAmplitude):
            self.__calculateAlpha()
            x = self.__calculateX()
            y = self.__calculateY()

        glColor3f(self.__color[0], self.__color[1], self.__color[2])

        for i in range(self.__renderRange - (self.__actualAmplitude * 2)):
            glVertex2f(x, y)
            glVertex2f(0.0, 0.0)
            self.__alpha += self.__dalpha
            x = self.__calculateX()
            y = self.__calculateY()
            glVertex2f(x, y)

        glEnd()

        self.__ôpenTheTcheka()

        return

    def __move(self):

        if (self.__mouthDirection == 0):
            self.gCameraX += self.__movSpeed
        elif (self.__mouthDirection == 90):
            self.gCameraY += self.__movSpeed
        elif (self.__mouthDirection == 180):
            self.gCameraX -= self.__movSpeed
        else:
            self.gCameraY -= self.__movSpeed

        return

    def changeDirection(self, rotationAngle):

        self.__mouthDirection = rotationAngle

        return