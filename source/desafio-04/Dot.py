"""

"""
import math as mt
from LTexture import *
from CoordPosition2D import *
from Sprite import *
import pdb

class Dot(LTexture):
    """
    Dot render a 'dot' in the screen.
    """
    def __init__(self, coordX, coordY, spriteStop, size = 15):
        """
        Construct a new 'Pacman' object.

        :param size: The radius of the Dot
        """
        self.vertexDataBuffer = None
        self.vertexIndexBuffer = None
        self.textureDataBuffer = None
        self.__size = size
        self.numSprites = 6
        self.spriteCoordXSize = 1/self.numSprites
        self.actualSprite = 0
        self.spriteSpeed = 10
        self.renderCount = 1
        self.__coordX = coordX
        self.__currentCoordY = coordY
        self.__coordY = coordY
        self.puloMax = coordY - 50
        self.pular = False
        self.puloSpeed = 3
        self.andando = False
        self.direita = True
        self.rotacionar = False
        self.spriteStop = spriteStop
        LTexture.__init__(self)
        self.initVBO()

    def nextSprite(self):
        if(self.andando):
            self.actualSprite += 1
        else:
            self.actualSprite = self.spriteStop
        if(self.actualSprite >= self.numSprites):
            self.actualSprite = 0
        if(self.renderCount > 60):
            self.renderCount = 1

    def initVBO(self):
        self.loadTextureFromFile("walk.png")
        self.initVertexData()
        self.initTextureData()
        return

    def initVertexData(self):
        self.vertexDataBuffer = glGenBuffers(1)
        vData = (CoordPosition2D*4)(CoordPosition2D())

        #Lado superior esquerdo
        vData[0].x = GLfloat(-self.__size)
        vData[0].y = GLfloat(self.__size)

        #Lado superior direito
        vData[1].x = GLfloat(self.__size)
        vData[1].y = GLfloat(self.__size)

        #Lado inferior direito
        vData[2].x = GLfloat(self.__size)
        vData[2].y = GLfloat(-self.__size)

        #Lado inferior esquerdo
        vData[3].x = GLfloat(-self.__size)
        vData[3].y = GLfloat(-self.__size)

        self.vertexIndexBuffer = glGenBuffers(1)

        indexBuffers = (GLuint*4)(GLuint(0))
        indexBuffers[0] = GLuint(0)
        indexBuffers[1] = GLuint(1)
        indexBuffers[2] = GLuint(2)
        indexBuffers[3] = GLuint(3)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.vertexIndexBuffer)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indexBuffers), indexBuffers, GL_STATIC_DRAW)

        glBindBuffer(GL_ARRAY_BUFFER, self.vertexDataBuffer)
        glBufferData(GL_ARRAY_BUFFER, sizeof(vData), vData, GL_STATIC_DRAW)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,0)
        glBindBuffer(GL_ARRAY_BUFFER,0)

        del vData
        return

    def initTextureData(self):
        self.textureDataBuffer = glGenBuffers(1)
        
        vData = (Sprite*6)()
        for i in range(0,self.numSprites):
            #Lado superior esquerdo
            vData[i].coord[0].x = GLfloat(i*self.spriteCoordXSize)
            vData[i].coord[0].y = GLfloat(0)

            #Lado superior direito
            vData[i].coord[1].x = GLfloat((i+1)*self.spriteCoordXSize)
            vData[i].coord[1].y = GLfloat(0)

            #Lado inferior direito
            vData[i].coord[2].x = GLfloat((i+1)*self.spriteCoordXSize)
            vData[i].coord[2].y = GLfloat(1)

            #Lado inferior esquerdo
            vData[i].coord[3].x = GLfloat(i*self.spriteCoordXSize)
            vData[i].coord[3].y = GLfloat(1)

        glBindBuffer(GL_ARRAY_BUFFER, self.textureDataBuffer)
        glBufferData(GL_ARRAY_BUFFER, sizeof(vData), vData, GL_STATIC_DRAW)

        glBindBuffer(GL_ARRAY_BUFFER,0)
        
        del vData
        return

    def render(self):
        """
        Render the Dot in the screen.

        :param coordX: The 'x' coordinate where the Dot will be rendered
        :param coordY: The 'y' coordinate where the Dot will be rendered
        """

        self.renderCount += 1
        if(self.renderCount % self.spriteSpeed == 0):
            self.nextSprite()
        glTranslatef(self.__coordX, self.__currentCoordY, 0)
        if(self.rotacionar):
            glRotatef(180,0,1,0)

        if(self.pular):
            self.__currentCoordY -= self.puloSpeed
            if(self.__currentCoordY < self.puloMax):
                self.pular = False
        else:
            self.updateCoordY()


        glBindTexture(GL_TEXTURE_2D, self.mTextureID)

        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)

        glBindBuffer(GL_ARRAY_BUFFER, self.vertexDataBuffer)
        glVertexPointer(2, GL_FLOAT, sizeof(CoordPosition2D), c_void_p(CoordPosition2D.x.offset))

        glBindBuffer(GL_ARRAY_BUFFER, self.textureDataBuffer)
        glTexCoordPointer(2, GL_FLOAT, sizeof(CoordPosition2D), c_void_p(self.actualSprite*sizeof(CoordPosition2D*4)))

        
        #glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.textureIndexBuffer[1])
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.vertexIndexBuffer)
        glDrawElements(GL_QUADS, 4, GL_UNSIGNED_INT, None)
        
        glBindTexture(GL_TEXTURE_2D,0)
        glBindBuffer(GL_ARRAY_BUFFER,0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,0)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)

    def handlekeys(self, key):
        velocidade = 6
        key = ord(key)
        #se o usuario pressiona a
        if(key == 97):
            self.andando = True
            if(self.getDireita()):
                self.setRotacionar(True)
            self.setDireita(False)
            self.setCoordX(self.getCoordX() - velocidade)
        #se o usuario pressiona d
        elif(key == 100):
            self.andando = True
            if(not self.getDireita()):
                self.setRotacionar(False)
            self.setDireita(True)
            self.setCoordX(self.getCoordX() + velocidade)
        #se o usuario pressiona w
        elif(key == 119):
            self.pular = True
        #se o usuario pressiona s
        #elif(key == 115):
            #self.__dot.setCoordY(self.__dot.getCoordY + 16)

    def updateCoordY(self):
        if(self.__currentCoordY < self.__coordY):
            self.__currentCoordY += self.puloSpeed

    def setCoordX(self, newCoord):
        self.__coordX = newCoord
    def getCoordX(self):
        return self.__coordX
    def setCoordY(self, newCoord):
        self.__coordY = newCoord
    def getCoordY(self):
        return self.__currentCoordY
    def setAndando(self, flag):
        self.andando = flag
    def setDireita(self, flag):
        self.direita = flag
    def getDireita(self):
        return self.direita
    def getPuloMax(self):
        return self.puloMax
    def setRotacionar(self, flag):
        self.rotacionar = flag
