"""

"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math as mt

class Dot:
    """
    Dot render a 'dot' in the screen.
    """
    def __init__(self, size = 5, color = [255, 0, 0]):
        """
        Construct a new 'Pacman' object.

        :param size: The radius of the Dot
        :param color: A vector with RGB values. [0:255, 0:255, 0:255]
        """
        self.__size = size
        color[:] = [ x / 255 for x in color] # Normalizando os valores entre 0 e 1
        self.__color = color
        self.__renderRange = 80
        self.gCameraX = 0
        self.gCameraY = 0
        self.__resetAlpha()
        self.__dalpha = mt.pi / 40

    def __resetAlpha(self):
        """
        Reset the 'alpha' value when the Dot is re-render.
        """
        self.__alpha = 0.0

        return

    def __calculateX(self):
        """
        Calculate a new coord 'x' of the Pacman using the current 'alpha' value.
        """
        return self.__size * mt.cos(self.__alpha)
    
    def __calculateY(self):
        """
        Calculate a new coord 'y' of the Pacman using the current 'alpha' value.
        """
        return self.__size * mt.sin(self.__alpha)

    def __calculateAlpha(self):
        """
        Calculate a new value to 'alpha' using the 'delta alpha' value.
        """
        self.__alpha += self.__dalpha
        
        return

    def render(self, coordX, coordY):
        """
        Render the Dot in the screen.

        :param coordX: The 'x' coordinate where the Dot will be rendered
        :param coordY: The 'y' coordinate where the Dot will be rendered
        """
        self.__resetAlpha()

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