"""

"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math as mt

class Pacman:
    """
    Pacman render a PACMAN(without eyes xD) in the screen.
    """
    def __init__(self, size, movSpeed = 1,  color = [255, 255, 0], mouthSpeed = 1):
        """
        Construct a new 'Pacman' object.

        :param size: The radius of the Pacman
        :param movSpeed: The number of pixels that the pacman will 'walk' per render
        :param color: A vector with RGB values. [0:255, 0:255, 0:255]
        :param mouthSpeed: The speed the Pacman close/open the mouth
        """
        self.__size = size
        self.__mouthDirection = 0
        self.__maxAmplitude = 10
        self.__mouthSpeed = mouthSpeed
        self.__movSpeed = movSpeed
        color[:] = [ x / 255 for x in color] # Normalizando os valores entre 0 e 1
        self.__color = color
        self.__rotation = 0.0
        self.__isOpen = True
        self.__currentAmplitude = self.__maxAmplitude
        self.__updateAlpha()        
        self.__renderRange = 80
        self.gCameraX = 50
        self.gCameraY = 50
        self.__dalpha = mt.pi / 40

    def __updateAlpha(self):
        """
        Updates the 'alpha' value when the Pacman rotates.
        """
        self.__alpha = self.__rotation

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

    def __mouthAnimation(self):
        """
        Update the mouth position using the 'mouthSpeed' value.
        """
        #Se a boca estiver aberta, a abertura da boca diminui na velocidade mouthSpeed
        #Se a boca estiver fechada, a abertura da boca aumenta na velocidade mouthSpeed
        if(self.__isOpen):
            self.__currentAmplitude += self.__mouthSpeed
            if(self.__currentAmplitude > 10):
                self.__isOpen = False
                self.__currentAmplitude -= 2
        else:
            self.__currentAmplitude -= self.__mouthSpeed
            if(self.__currentAmplitude < 0):
                self.__isOpen = True
                self.__currentAmplitude += 2
        
        return

    def changeSize(self, newSize):
        """
        Update the 'size'(aka: radius) of the Pacman.

        :param newSize: The new radius of the Pacman
        """
        #Mudando tamanho do pacman
        self.__size = newSize
        return

    def getSize(self):
        """
        Return the current 'size' of the Pacman.

        :return: Pacman radius
        """
        #Tamanho do pacman (raio)
        return self.__size

    def render(self, stop = False):
        """
        Render the Pacman in the screen.

        :param stop: Make the Pacman be render in the previous position
        """
        self.__updateAlpha()
        
        if not stop:
            self.__move()
        
        #Transladando de acordo com as coordenadas x e y dadas
        glTranslatef(self.gCameraX, self.gCameraY, 0)

        #Definindo abertura da boca para iniciar renderização
        glRotatef(self.__mouthDirection, 0, 0, 1)

        #Calculando as coordenadas de inicio da renderização
        x = self.__calculateX()
        y = self.__calculateY()

        glBegin(GL_TRIANGLES)

        #Definindo o início da renderização com base na abertura da boca
        for i in range(self.__currentAmplitude):
            self.__calculateAlpha()
            x = self.__calculateX()
            y = self.__calculateY()

        glColor3f(self.__color[0], self.__color[1], self.__color[2])

        #Renderizando os triângulos para gerar o pacman (de acordo com a abertura atual da boca)
        for i in range(self.__renderRange - (self.__currentAmplitude * 2)):
            glVertex2f(x, y)
            glVertex2f(0.0, 0.0)
            self.__alpha += self.__dalpha
            x = self.__calculateX()
            y = self.__calculateY()
            glVertex2f(x, y)

        glEnd()

        #Aplicando a animação da boca
        self.__mouthAnimation()

        return

    def getPos(self):
        """
        Return the current position of the Pacman.

        :return: An array with the coord (x, y)
        """
        #Posição atual do pacman
        return [self.gCameraX, self.gCameraY]

    def __move(self):
        """
        Update the pacman position using the current direction.
        """
        #Fazendo o pacman se movimentar de acordo com a direção da boca
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
        """
        Change the Pacman direction(where the mouth is pointing).

        :param rotationAngle: Angle in degree
        """
        #Mudando a variável de direção da boca de acordo com um ângulo de rotação dado
        ang = rotationAngle % 361
        self.__mouthDirection = ang
        return

    def rotate(self, angle):
        """
        Change the Pacman direction(where the mouth is pointing).

        :param angle: Angle in radian( a multiple of pi )
        """
        #Mudando a variável de rotação de acordo com um ângulo
        self.__rotation += angle
        return