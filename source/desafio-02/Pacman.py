from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math as mt

class Pacman:

    def __init__(self, size, movSpeed = 1, mouthSpeed = 1,  color = [1, 1, 0]):
        #Iniciando algumas variáveis
        self.__size = size
        self.__mouthDirection = 0
        self.__maxAmplitude = 10
        self.__mouthSpeed = mouthSpeed
        self.__movSpeed = movSpeed
        self.__color = color
        self.__rotation = 0.0
        
        self.__starting()

    def __starting(self):
        # Iniciando as variáveis para renderização
        self.__isOpen = True
        self.__actualAmplitude = self.__maxAmplitude
        self.__updateAlpha()        
        self.__renderRange = 80
        self.gCameraX = 50
        self.gCameraY = 50
        self.__dalpha = mt.pi / 40

    def __updateAlpha(self):
        #Atualizando o ângulo atual de rotação
        self.__alpha = self.__rotation

    def __calculateX(self):
        #Calculando a coordenada X
        return self.__size * mt.cos(self.__alpha)
    
    def __calculateY(self):
        #Calculando a coordenada Y
        return self.__size * mt.sin(self.__alpha)

    def __calculateAlpha(self):
        #Incrementando o valor do ângulo
        self.__alpha += self.__dalpha
        return

    def __mouthAnimation(self):
        #Se a boca estiver aberta, a abertura da boca diminui na velocidade mouthSpeed
        #Se a boca estiver fechada, a abertura da boca aumenta na velocidade mouthSpeed
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
        #Mudando tamanho do pacman
        self.__size = newSize
        return

    def getSize(self):
        #Tamanho do pacman (raio)
        return self.__size

    def render(self, stop = False):
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
        for i in range(self.__actualAmplitude):
            self.__calculateAlpha()
            x = self.__calculateX()
            y = self.__calculateY()

        glColor3f(self.__color[0], self.__color[1], self.__color[2])

        #Renderizando os triângulos para gerar o pacman (de acordo com a abertura atual da boca)
        for i in range(self.__renderRange - (self.__actualAmplitude * 2)):
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
        #Posição atual do pacman
        return [self.gCameraX, self.gCameraY]

    def __move(self):
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
        #Mudando a variável de direção da boca de acordo com um ângulo de rotação dado
        self.__mouthDirection = rotationAngle
        return

    def rotate(self, angle):
        #Mudando a variável de rotação de acordo com um ângulo
        self.__rotation += angle
        return