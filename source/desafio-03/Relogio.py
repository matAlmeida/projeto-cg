from LTexture import *

class Relogio(LTexture):
	Textura = None
	def __init__(self):
		Textura = LTexture.__init__(self)

	def render(self,x,y):
		#Se a textura existel
		if(self.mTextureID != 0):
			#Remove quaisquer transformações anteriores
			glLoadIdentity()

			#Movendo para o ponto de renderização
			#glTranslatef(x,y,0)

			#Definindo textura ID
			glBindTexture(GL_TEXTURE_2D,self.mTextureID)

			#Renderizando quadrados texturizados
			glBegin(GL_QUADS)
			glTexCoord2f(0,0)
			glVertex2f(-self.mTextureWidth/2, self.mTextureHeight/2)
			glTexCoord2f(1,0)
			glVertex2f(self.mTextureWidth/2,self.mTextureHeight/2)
			glTexCoord2f(1,1)
			glVertex2f(self.mTextureWidth/2,-self.mTextureHeight/2)
			glTexCoord2f(0,1)			
			glVertex2f(-self.mTextureWidth/2,-self.mTextureHeight/2)
			glEnd()