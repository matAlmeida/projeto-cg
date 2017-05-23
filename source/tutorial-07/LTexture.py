from LFRect import *

class LTexture:
	mTextureID = 0
	mTextureWidth = 0
	mTextureHeight = 0
	def __init__(self):
		#Inicializando textura ID
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
		self.mTextureWidth = 0
		self.mTextureHeight = 0

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

	def render(self,x,y,clip):
		#Se a textura existe
		if(self.mTextureID != 0):
			#Remove quaisquer transformações anteriores
			glLoadIdentity()

			#Coordenadas de textura
			texTop = 0.0
			texBottom = 1.0
			texLeft = 0.0
			texRight = 1.0

			#Coordenadas de vértice
			quadWidth = self.mTextureWidth
			quadHeight = self.mTextureHeight

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
			glVertex2f(0,0)
			glTexCoord2f(texRight,texTop)
			glVertex2f(quadWidth,0)
			glTexCoord2f(texRight,texBottom)
			glVertex2f(quadWidth,quadHeight)
			glTexCoord2f(texLeft,texBottom)
			glVertex2f(0,quadHeight)
			glEnd()

	def getTextureID(self):
		return self.mTextureID

	def textureWidth(self):
		return self.mTextureWidth

	def textureHeight(self):
		return self.mTextureHeight