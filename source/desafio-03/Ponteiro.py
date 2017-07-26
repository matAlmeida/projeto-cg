from LTexture import*

class Ponteiro(LTexture):
	def __init__(self, hms):
		LTexture.__init__(self)
		self.hms = hms
		self.rang = 0

	def render(self,x,y):
		global rang
		#Se a textura existel
		if(self.mTextureID != 0):
			self.rang += 1
			#Remove quaisquer transformações anteriores
			glLoadIdentity()

			#Movendo para o ponto de renderização
			glRotatef(self.rang,0,0,1)
			glTranslatef(0,-18,0)
			

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