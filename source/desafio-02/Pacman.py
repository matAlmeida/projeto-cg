from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math as mt

class Pacman:
    def __init__(self, size):
        self._aberturaBoca = 0
        self._bocaAbrindo = True
        self._bocaDir = 0
        self._size = size;
        self._alpha = 0.0
        self._dalpha = mt.pi / 40

    def render(self, gCameraX, gCameraY):
        #Movendo a câmera para uma posição
        glTranslatef(gCameraX,gCameraY,0)

        x = self.__calculateX()
        y = self.__calculateY()
        glBegin(GL_TRIANGLES)
        for i in range(self._aberturaBoca):
            self._alpha += self._dalpha
            x = self.__calculateX()
            y = self.__calculateY()
        glColor3f(1,1,0)
        for i in range(80 - (self._aberturaBoca * 2)):
            glVertex2f(x, y)
            glVertex2f(0.0, 0.0)
            self._alpha += self._dalpha
            x = self.__calculateX()
            y = self.__calculateY()
            glVertex2f(x, y)
        glEnd()

        #Verificando e alterando abertura da boca
        if(self._bocaAbrindo):
            self._aberturaBoca += 1
            if(self._aberturaBoca > 10):
                self._bocaAbrindo = False
                self._aberturaBoca -= 2
        else:
            self._aberturaBoca -= 1
            if(self._aberturaBoca < 0):
                self._bocaAbrindo = True
                self._aberturaBoca += 2

    def changeSize(self, newSize):
        self._size = newSize

        return True

    def rotate(self, alpha):
        for i in range(mt.fabs(alpha)):
            self._bocaDir += i
            glRotatef(self._bocaDir, 0, 0, 1)

    def __calculateX(self):

        return self._size * mt.cos(self._alpha)
    
    def __calculateY(self):

        return self._size * mt.sin(self._alpha)

    #def __calculateAlpha(self):

        #return self._alpha += self._dalpha