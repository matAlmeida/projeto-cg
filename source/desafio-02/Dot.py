from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math as mt

class Dot:

    def __init__(self, color = [1, 0, 0], size = 5):
        self.__size = size
        self.__color = color
        self.__starting()

    def __starting(self):
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

    def render(self, coordX, coordY):
        self.__initAlpha()

        # self.__move()

        glTranslatef(coordX, coordY, 0)

        # Renderizando um circulo com cor sólida, a partir da cor inicial ciano, utilizando tringulos
        x = self.__calculateX()
        y = self.__calculateY()

        glBegin(GL_TRIANGLES)

        glColor3f(self.__color[0], self.__color[1], self.__color[2])
        for i in range(self.__renderRange):
            glVertex2f(x, y)
            glVertex2f(0.0, 0.0)
            self.__calculateAlpha()
            x = self.__calculateX()
            y = self.__calculateY()
            glVertex2f(x, y)

        glEnd()