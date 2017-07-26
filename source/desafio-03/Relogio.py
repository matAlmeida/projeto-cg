from LTexture import *
from Ponteiro import *
from MatrizBoladona import *
from time import *

class Relogio(LTexture):
	Textura = None
	def __init__(self):
		Textura = LTexture.__init__(self)
		self.Horas = Ponteiro(360/12, localtime(time())[3])
		self.Minutos = Ponteiro(360/60, localtime(time())[4])
		self.Segundos = Ponteiro(360/60, localtime(time())[5])

	def initTexture(self):
		#Carregando textura
		flag = self.loadTextureFromFile("relogioCoca.png")
		if(flag):
			flag = self.Horas.loadTextureFromFile("pontHoras.png")
		if(flag):
			flag = self.Minutos.loadTextureFromFile("pontMinutos.png")
		if(flag):
			flag = self.Segundos.loadTextureFromFile("pontSegundos.png")
		return flag

	def drawClock(self):
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

	def render(self):
		#Se a textura existel
		if(self.mTextureID != 0):
			#Definindo textura ID
			glBindTexture(GL_TEXTURE_2D,self.mTextureID)
			with MatrizBoladona():
				self.drawClock()
			with MatrizBoladona():
				self.Horas.render()
			with MatrizBoladona():
				self.Minutos.render()
			with MatrizBoladona():
				self.Segundos.render()
		
	def update(self):
		self.Segundos.update(localtime(time())[5])
		print(localtime(time())[5])
		pass