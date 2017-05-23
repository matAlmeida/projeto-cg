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

	def loadTextureFromPixels32(self):
		#Flag de carregamento
		success = True

		if(self.mTextureID == 0 and self.mPixels != None):
			#Gera textura ID
			glGenTextures(1,self.mTextureID)

			#Define a ID da textura
			self.mTextureID = 1

			#Cria textura ID
			glBindTexture(GL_TEXTURE_2D,self.mTextureID)

			#Gera textura
			glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,self.mTextureWidth,self.mTextureHeight,0,GL_RGBA,GL_UNSIGNED_BYTE,self.mPixels)

			#Definindo parâmetros da textura
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

			#Liberando textura
			glBindTexture(GL_TEXTURE_2D,0)

			#Procurando erros
			erro = glGetError()
			if(erro != GL_NO_ERROR):
				print("Erro ao carregar textura de %p pixels! %s\n",self.mPixels,gluErrorString(erro))
				success = False
			else:
				#Liberando pixels
				del self.mPixels
				self.mPixels = None
		else:
			print("Não foi possível carregar textura através dos pixels atuais!")

			#Se a textura existe
			if(self.mTextureID != 0):
				print("A textura já foi carregada!")
			#Se nenhum pixel foi carregado
			elif(self.mPixels == None):
				print("Sem pixels para gerar uma textura!")
			success = False
		return success

	def loadPixelsFromFile(self,im):
		#Desalocando dados da textura
		self.freeTexture(self)

		pixelsLoaded = False

		if(im != None):
			#Inicializando dimensões
			imgWidth = im.width
			imgHeight = im.height

			#Calculando dimensões da textura
			texWidth = self.powerOfTwo(imgWidth)
			texHeigth = self.powerOfTwo(imgHeight)

			#Obtendo dimensoes de imagem
			self.mImageWidth = imgWidth
			self.mImageHeight = imgHeight
			self.mTextureWidth = texWidth
			self.mTextureHeight = texHeigth

			self.mPixels = im.tobytes("raw","RGBA",0,-1)

			pixelsLoaded = True
		if(pixelsLoaded == False):
			print("Não foi possível carregar a imagem!")
		return pixelsLoaded

	def loadTextureFromFileWithColorKey(self,imagem):
		#Gerando e Definindo uma imagem atual
		im = Image.open(imagem).convert("RGBA")

		#Carregando pixels
		if(not self.loadPixelsFromFile(im)):
			return False

		#Retirando imagem da memória
		im.close()
		#Criando textura
		return self.loadTextureFromPixels32()

	def render(self,x,y,clip = None, stretch = None,degrees = None):
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
			#Alongando imagem
			if(stretch != None):
				quadWidth = stretch.w
				quadHeight = stretch.h

			#Movendo para o ponto de renderização
			glTranslatef(x + quadWidth/2,y + quadHeight/2,0)

			#Rotacionando ao redor do ponto de renderização
			glRotatef(degrees,0,0,1)

			#Definindo textura ID
			glBindTexture(GL_TEXTURE_2D,self.mTextureID)

			#Renderizando quadrados texturizados
			glBegin(GL_QUADS)
			glTexCoord2f(texLeft,texTop)
			glVertex2f(-quadWidth / 2, -quadHeight / 2)
			glTexCoord2f(texRight,texTop)
			glVertex2f(quadWidth / 2, -quadHeight / 2)
			glTexCoord2f(texRight,texBottom)
			glVertex2f(quadWidth / 2, quadHeight / 2)
			glTexCoord2f(texLeft,texBottom)
			glVertex2f(-quadWidth / 2, quadHeight / 2)
			glEnd()

	def getPixelData32(self):
		return self.mPixels

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

	def powerOfTwo(self,num):
		if(num != 0):
			num -= 1
			num = num | (num >> 4)
			num = num | (num >> 8)
			num = num | (num >> 16)
			num += 1
		return num