from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class LTexture:
	#Inicializando textura ID
	mTextureID = 0
	mTextureWidth = 0
	mTextureHeight = 0
	def __int__(self):
		#Inicializando dimensões da textura
		self.mTextureID = 0
		self.mTextureWidth = 0
		self.mTextureHeight = 0

	@staticmethod
	def freeTexture(self):
		#Deletando textura
		if(self.mTextureID != 0):
			glDeleteTextures(1,mTextureID)
			self.mTextureID = 0
		mTextureWidth = 0
		mTextureHeight = 0

	def __del__(self):
		#Limpa dados da textura se preciso
		self.freeTexture(self)

	def loadTextureFromPixels32(self,pixels,width,height):
		#Limpa textura se existir
		self.freeTexture(self)

		#Obtém as dimensões da textura
		mTextureWidth = width
		mTextureHeight = height

		#Gera textura ID
		texture = glGenTextures(1,self.mTextureID)

		#Cria textura ID
		glBindTexture(GL_TEXTURE_2D,self.mTextureID)

		#Gera textura
		glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,width,height,0,GL_RGBA,GL_UNSIGNED_BYTE,pixels)

		#Definindo parâmetros da textura
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

		#Liberando textura
		glBindTexture(GL_TEXTURE_2D,0)

		#Procurando erros
		erro = glGetError()
		if(erro != GL_NO_ERROR):
			print("Erro ao carregar textura de %p pixels! %s\n",pixels,gluErrorString(erro))
			return False
		return True

	def render(self,x,y):
		#Se a textura existel
		if(self.mTextureID != 0):
			#Remove quaisquer transformações anteriores
			glLOadIdentity()

			#Movendo para o ponto de renderização
			glTranslatef(x,y,0)

			#Definindo textura ID
			glBindTexture(GL_TEXTURE_2D,mTextureID)

			#Renderizando quadrados texturizados
			glBegin(GL_QUADS)
			glTexCoord2f(0,0)
			glVertex2f(1,0)
			glTexCoord2f(1,0)
			glVertex2f(mTextureWidth,0)
			glTexCoord2f(1,1)
			glVertex2f(mTextureWidth,mTextureHeight)
			glTexCoord2f(0,1)
			glVertex2f(0,mTextureHeight)

	def getTextureID(self):
		return self.mTextureID

	def textureWidth(self):
		return self.mTextureWidth

	def textureHeight(self):
		return self.mTextureHeight