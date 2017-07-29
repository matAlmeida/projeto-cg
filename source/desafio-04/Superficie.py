"""

"""
import math as mt
from LTexture import *
from CoordPosition2D import *
from Sprite import *
import pdb

class Superficie(LTexture):
    """
    Dot render a 'dot' in the screen.
    """
    def __init__(self, image):
        self.image = image
        self.loadMedia()

    def render(self, x, y, clip = None):
        #Se a textura existe
        if(self.mTextureID != 0):
            #Remove quaisquer transformações anteriores
            glLoadIdentity()

            #Coordenadas de textura
            texTop = 0.0
            texBottom = self.mImageHeight/self.mTextureHeight
            texLeft = 0.0
            texRight = self.mImageWidth/self.mTextureWidth

            #Coordenadas de vértice
            quadWidth = self.mImageWidth
            quadHeight = self.mImageHeight

            if(clip != None):
                #Coordenadas de textura
                texLeft = clip.x / self.mTextureWidth
                texRight = (clip.x + clip.w) / self.mTextureWidth
                texTop = clip.y / self.mTextureHeight
                texBottom = (clip.y + clip.h) / self.mTextureHeight

                #Coordenadas de vertice
                quadWidth = clip.w
                quadHeight = clip.h

            #Movendo para o ponto de renderização
            glTranslatef(x,y,0)

            #Definindo textura ID
            glBindTexture(GL_TEXTURE_2D,self.mTextureID)

            #Renderizando quadrados texturizados
            glBegin(GL_QUADS)
            glTexCoord2f(texLeft,texTop)
            glVertex2f(0,quadHeight)
            glTexCoord2f(texRight,texTop)
            glVertex2f(quadWidth,quadHeight)
            glTexCoord2f(texRight,texBottom)
            glVertex2f(quadWidth,0)
            glTexCoord2f(texLeft,texBottom)
            glVertex2f(0,0)
            glEnd()

    def loadMedia(self):
        #Carregando textura
        if(not self.loadTextureFromFile(self.image)):
            print("Não foi possível carregar a textura!")
            return False

        return True