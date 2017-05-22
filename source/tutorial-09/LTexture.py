from LFRect import *

class LTexture:
	def __init__(self):
		#Inicializando textura ID
		self.mTextureID = 0
		#Inicializando dimensões da textura
		self.mTextureWidth = 0
		self.mTextureHeight = 0
		#Dimensões da imagem
		self.mImageWidth = 0
		self.mImageHeight = 0
		#Pixels atuais
		self.mPixels = None

	@staticmethod
	def freeTexture(self):
		#Deletando textura
		if(self.mTextureID != 0):
			glDeleteTextures(1,self.mTextureID)
			self.mTextureID = 0
		#Deletando pixels
		if(self.mPixels != None):
			del self.mPixels
			self.mPixels = None
		self.mTextureWidth = 0
		self.mTextureHeight = 0
		self.mImageHeight = 0
		self.mImageWidth = 0

	def __del__(self):
		#Limpa dados da textura se preciso
		self.freeTexture(self)

	def lock(self):
		#Se a textura não está bloqueada e existe
		if(self.mPixels == None and self.mTextureID != 0):
			#Definindo textura atual
			glBindTexture(GL_TEXTURE_2D,self.mTextureID)

			#Obtendo pixels
			glGetTexImage(GL_TEXTURE_2D,0,GL_RGBA,GL_UNSIGNED_BYTE,self.mPixels)

			#Desligando textura
			glBindTexture(GL_TEXTURE_2D,0)

			return True

	def unlock(self):
		#Se a textura está bloqueada e a textura existe
		if(self.mPixels != None and self.mTextureID != 0):
			#Definindo textura atual
			glBindTexture(GL_TEXTURE_2D,self.mTextureID)

			#Atualizando textura
			glTexSubImage2D(GL_TEXTURE_2D,0,0,0,self.mTextureWidth,self.mTextureHeight,GL_RGBA,GL_UNSIGNED_BYTE,self.mPixels)

			#Deletando pixels
			if(self.mPixels != None):
				del self.mPixels
				self.mPixels = None

			#Desligando textura
			glBindTexture(GL_TEXTURE_2D,0)

			return True

	def loadTextureFromPixels32(self,pixels,imgWidth,imgHeight,texWidth,texHeight):
		#Limpa textura se existir
		self.freeTexture(self)

		#Obtém as dimensões da textura
		self.mTextureWidth = texWidth
		self.mTextureHeight = texHeight
		self.mImageHeight = imgHeight
		self.mImageWidth = imgWidth

		#Gera textura ID
		glGenTextures(1,self.mTextureID)

		#Define a ID da textura
		self.mTextureID = 1

		#Cria textura ID
		glBindTexture(GL_TEXTURE_2D,self.mTextureID)

		#Gera textura
		glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,self.mTextureWidth,self.mTextureHeight,0,GL_RGBA,GL_UNSIGNED_BYTE,pixels)

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
			#Inicializando dimensões
			imgWidth = im.width
			imgHeight = im.height

			#Calculando dimensões da textura
			texWidth = self.powerOfTwo(imgWidth)
			texHeigth = self.powerOfTwo(imgHeight)

			#Criando a textura a partir dos pixels do arquivo
			imagem = im.tobytes("raw","RGBA",0,-1)
			textureLoaded = self.loadTextureFromPixels32(imagem,imgWidth,imgHeight,texWidth,texHeigth)

		if(textureLoaded != False):
			#Bloqueando textura para modificação
			self.lock()

			#Tornando parte exterior do circulo transparente
			for i in range(0,im.height):
				for j in range(0,im.width):
					r,g,b,a = im.getpixel((i,j))
					if(r == 0):
						im.putpixel((i,j),(0,0,0,0))

			for i in range(0,im.height):
				for j in range(0,im.width):
					if(j%10 != i%10):
						im.putpixel((i,j),(0,0,0,0))
			self.mPixels = im.tobytes("raw","RGBA",0,-1)
			#Atualizando textura
			self.unlock()
		im.close()

		if(textureLoaded == False):
			print("Não foi possível carregar a imagem!")
		return textureLoaded

	def render(self,x,y,clip = None):
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

	def getTextureID(self):
		return self.mTextureID

	def textureWidth(self):
		return self.mTextureWidth

	def imageWidth(self):
		return self.mImageWidth

	def imageHeight(self):
		return self.mImageHeight

	def textureHeight(self):
		return self.mTextureHeight

	def getImagePixel(self,x,y):
		return im.getpixel((x,y))

	def putImagePixel(self,x,y,pixel):
		return im.putpixel((x,y),pixel)

	def getDataImage(self):
		return im.tobytes("raw","RGBA",0,-1)

	def getMPixel(self):
		return self.mPixels

	def setMPixel(self,pixel):
		self.mPixel = pixel

	def powerOfTwo(self,num):
		if(num != 0):
			num -= 1
			num = num | (num >> 4)
			num = num | (num >> 8)
			num = num | (num >> 16)
			num += 1
		return num