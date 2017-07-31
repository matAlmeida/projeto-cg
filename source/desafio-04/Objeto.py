"""

"""
import math as mt
from LTexture import *
from CoordPosition2D import *
from Sprite import *
import pdb

class Objeto(LTexture):
    """
    Dot render a 'dot' in the screen.
    """
    def __init__(self, objType, coordX, coordY):
        obj = self.__returnObj(objType)
        self.image = obj[0]
        self.vertexDataBuffer = None
        self.vertexIndexBuffer = None
        self.textureDataBuffer = None
        self.__size = obj[2]
        self.__renderRange = 80
        self.coordX = coordX
        self.coordY = coordY
        self.__resetAlpha()
        self.__dalpha = mt.pi / 40
        self.numSprites = obj[1]
        self.spriteCoordXSize = 1/self.numSprites
        self.actualSprite = 0
        self.spriteSpeed = 10
        self.renderCount = 1
        self.stopRender = True
        self.rotacionar = False
        LTexture.__init__(self)
        self.initVBO()

    def nextSprite(self):
        self.actualSprite += 1
        if(self.actualSprite >= self.numSprites):
            self.actualSprite = 0
        if(self.renderCount > 60):
            self.renderCount = 1
    def __resetAlpha(self):
        """
        Reset the 'alpha' value when the Dot is re-render.
        """
        self.__alpha = 0.0

        return

    def __calculateAlpha(self):
        """
        Calculate a new value to 'alpha' using the 'delta alpha' value.
        """
        self.__alpha += self.__dalpha
        return

    def initVBO(self):
        self.loadTextureFromFile(self.image)
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
        del indexBuffers
        return

    def initTextureData(self):
        self.textureDataBuffer = glGenBuffers(1)
        
        vData = (Sprite*self.numSprites)()
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
        self.__resetAlpha()

        self.renderCount += 1
        if(self.renderCount % self.spriteSpeed == 0):
            self.nextSprite()
        glTranslatef(self.coordX, self.coordY, 0)
        if(self.rotacionar):
            glRotatef(180,0,1,0)

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

    def changeObj(self, objType, x, y):
        self.__init__(objType, x, y)

    def __returnObj(self, num):
        if(num == 0):
            return ["Objetos/shot.png", 1, 25]
        elif(num == 1):
            return ["Objetos/abobora.png", 6, 15]
        elif(num == 2):
            return ["Objetos/coin.png", 10, 15]
        elif(num == 3):
            return ["Objetos/cogumelo.png", 1, 15]
        elif(num == 4):
            return ["Objetos/tomato.png", 4, 15]
        elif(num == 5):
            return ["Objetos/strawberry.png", 6, 15]

    def getStopRender(self):
        return self.stopRender
    def setStopRender(self, flag):
        self.stopRender = flag
    def getCoordX(self):
        return self.coordX
    def getCoordY(self):
        return self.coordY
    def setCoordX(self, newCoord):
        self.coordX = newCoord
    def setCoordY(self, newCoord):
        self.coordY = newCoord
    def getRotacionar(self):
        return self.rotacionar
    def setRotacionar(self, flag):
        self.rotacionar = flag
    def getImage(self):
        return self.image
