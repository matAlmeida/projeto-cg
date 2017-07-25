from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from PIL.Image import open

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
		#Limpa textura se existir
		self.freeTexture(self)

		#Obtém as dimensões da textura
		self.mTextureWidth = width
		self.mTextureHeight = height

		#Gera textura ID
		glGenTextures(1,self.mTextureID)

		#Define a ID da textura
		self.mTextureID = 1

		#Cria textura ID
		glBindTexture(GL_TEXTURE_2D,self.mTextureID)
		glPixelStorei(GL_UNPACK_ALIGNMENT,1)

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

	def loadTextureFromFile(self,imagem, screenColor):
		textureLoaded = False

		#Gerando e Definindo uma imagem atual
		im = open(imagem).convert("RGBA")
		if(im != None):
			im = self.transparentImage(im, screenColor, False)
			#Criando a textura a partir dos pixels do arquivo
			imagem = im.tobytes("raw","RGBA",0,-1)
			textureLoaded = self.loadTextureFromPixels32(imagem,im.size[0],im.size[1])
		im.close()
		if(textureLoaded == False):
			print("Não foi possível carregar a imagem!")
		return textureLoaded

	def render(self,x,y):
		#Se a textura existel
		if(self.mTextureID != 0):
			#Remove quaisquer transformações anteriores
			glLoadIdentity()

			#Movendo para o ponto de renderização
			glTranslatef(x,y,0)

			#Definindo textura ID
			glBindTexture(GL_TEXTURE_2D,self.mTextureID)

			#Renderizando quadrados texturizados
			glBegin(GL_QUADS)
			glTexCoord2f(0,0)
			glVertex2f(0,self.mTextureHeight)
			glTexCoord2f(1,0)
			glVertex2f(self.mTextureWidth,self.mTextureHeight)
			glTexCoord2f(1,1)
			glVertex2f(self.mTextureWidth,0)
			glTexCoord2f(0,1)
			glVertex2f(0,0)
			glEnd()

	def transparentImage(self, im, color, fullRange = True):
		if(fullRange):
			for col in range(0,im.size[0]):
				for lin in range(0,im.size[1]):
					r,g,b,a = im.getpixel((lin, col))
					imColor = [r,g,b,a]
					if(r > 208 and g > 185 and b > 175):
						im.putpixel((lin, col), (color[0], color[1], color[2], color[3]))
		else:	
			#Varrendo lado esquerdo
			for col in range(0,im.size[0]):
				for lin in range(0,im.size[1]):
					r,g,b,a = im.getpixel((lin, col))
					imColor = [r,g,b,a]
					if(r > 208 and g > 185 and b > 175):
						im.putpixel((lin, col), (color[0], color[1], color[2], color[3]))
					else:						
						break
			#Varrendo lado direito
			width = im.size[0] - 1
			height = im.size[1] - 1
			for col in range(-width, 1):
				for lin in range(-height,0):
					r,g,b,a = im.getpixel((-lin, -col))
					imColor = [r,g,b,a]
					if(r > 208 and g > 185 and b > 175):
						im.putpixel((-lin, -col), (color[0], color[1], color[2], color[3]))
					else:
						break
		return im

	def getTextureID(self):
		return self.mTextureID

	def textureWidth(self):
		return self.mTextureWidth

	def textureHeight(self):
		return self.mTextureHeight