from LTexture import *
from Ponteiro import *
from MatrizBoladona import *
from time import *
import pygame

class Relogio(LTexture):
	Textura = None
	def __init__(self):
		Textura = LTexture.__init__(self)
		self.Horas = Ponteiro(360/12, localtime(time())[3])
		self.Minutos = Ponteiro(360/60, localtime(time())[4])
		self.Segundos = Ponteiro(360/60, localtime(time())[5])
		pygame.init()
		pygame.mixer.init()
		pygame.mixer.music.load(b'despertador.wav')
		pygame.mixer.music.play(-1)
		#self.despertador = pygame.mixer.Sound(b'despertador.mp3')
		#self.despertador.play()

	def initTexture(self):
		#Carregando textura
		flag = self.loadTextureFromFile("relogioSafadao.png")
		if(flag):
			flag = self.Horas.loadTextureFromFile("pontHoras2.png")
		if(flag):
			flag = self.Minutos.loadTextureFromFile("pontMinutos2.png")
		if(flag):
			flag = self.Segundos.loadTextureFromFile("pontSegundos2.png")
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
				self.Horas.render(-18)
			with MatrizBoladona():
				self.Minutos.render(-32)
			with MatrizBoladona():
				self.Segundos.render(-37)
	def update(self):
		self.Segundos.update(localtime()[5])
		self.Minutos.update(localtime()[4]+(localtime()[5]/60))
		self.Horas.update(localtime()[3]+(localtime()[4]/60))