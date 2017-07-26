from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from PIL.Image import open

DEFAULT_TEXTURE_WRAP = GL_REPEAT

class LTexture:
	mTextureID = 0
	mTextureWidth = 0
	mTextureHeight = 0
	def __init__(self):
		#Inicializando ID da textura
		self.mTextureID = 0
		#Inicializando dimensões da textura
		self.mTextureWidth = 0
		self.mTextureHeight = 0

	@staticmethod
	def freeTexture(self):
		#Deletando textura
		if(self.mTextureID != 0):
			glDeleteTextures(1,self.mTextureID)
			self.mTextureID = 0
		mTextureWidth = 0
		mTextureHeight = 0

	def __del__(self):
		#Limpa dados da textura se preciso
		self.freeTexture(self)

	def loadTextureFromPixels32(self,pixels,width,height):
		#Obtém as dimensões da textura
		self.mTextureWidth = width
		self.mTextureHeight = height

		#Gera textura ID
		self.mTextureID = glGenTextures(1)

		#Cria textura ID
		glBindTexture(GL_TEXTURE_2D,self.mTextureID)
		glPixelStorei(GL_UNPACK_ALIGNMENT,1)

		#Gera textura
		glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,width,height,0,GL_RGBA,GL_UNSIGNED_BYTE,pixels)

		#Definindo parâmetros da textura
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, DEFAULT_TEXTURE_WRAP)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, DEFAULT_TEXTURE_WRAP)

		#Liberando textura
		glBindTexture(GL_TEXTURE_2D,0)

		#Procurando erros
		erro = glGetError()
		if(erro != GL_NO_ERROR):
			print("Erro ao carregar textura de %p pixels! %s\n",pixels,gluErrorString(erro))
			return False
		return True

	def loadTextureFromFile(self,imagem):
		textureLoaded = False

		#Gerando e Definindo uma imagem atual
		im = open(imagem).convert("RGBA")
		if(im != None):
			#Criando a textura a partir dos pixels do arquivo
			imagem = im.tobytes("raw","RGBA",0,-1)
			textureLoaded = self.loadTextureFromPixels32(imagem,im.size[0],im.size[1])
		im.close()
		if(textureLoaded == False):
			print("Não foi possível carregar a imagem!")
		return textureLoaded

	def getTextureID(self):
		return self.mTextureID

	def textureWidth(self):
		return self.mTextureWidth

	def textureHeight(self):
		return self.mTextureHeight