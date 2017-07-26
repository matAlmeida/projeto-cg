from LTexture import*

class Ponteiro(LTexture):
	def __init__(self, ticAngle, time):
		LTexture.__init__(self)
		self.ticAngle = ticAngle
		self.angle = time*self.ticAngle
		self.value = time

	def render(self, y):
		#Se a textura existel
		if(self.mTextureID != 0):
			#Movendo para o ponto de renderização
			glRotatef(self.angle,0,0,1)
			glTranslatef(0, y, 0)
			
			#Definindo textura ID
			glBindTexture(GL_TEXTURE_2D,self.mTextureID)
			self.drawPointer()	

	def update(self, time):
		self.value = time
		self.angle = time*self.ticAngle

	def drawPointer(self):
		#Renderizando quadrado texturizado
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