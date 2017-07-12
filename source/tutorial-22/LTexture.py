from LVertexData2D import *
from LFRect import *
from PIL import Image
from PIL.Image import open


DEFAULT_TEXTURE_WRAP = GL_REPEAT

class LTexture:
	def __init__(self):
		#Inicializando textura ID e pixels
		self.mTextureID = 0
		self.mPixels32 = None
		self.mPixels8 = None
		self.mPixelsFormat = None

		#Inicializando dimensões da textura
		self.mTextureWidth = 0
		self.mTextureHeight = 0
		
		#Dimensões da imagem
		self.mImageWidth = 0
		self.mImageHeight = 0

		#Inicializando VBO(Vertex Buffer Object)
		self.mVBOID = 0
		self.mIBOID = 0
	'''
	def __del__(self):
		#Limpa dados da textura se preciso
		self.freeTexture(self)

		#Liberar o VBO e IBO se preciso 
		self.freeVBO()'''
	
	def initVBO(self):
		#Se atextura for carregada e VBO não existe 
		if (self.mTextureID != 0 and self.mVBOID == 0):
			#Dados do vertice
			#vData array(position(x,y), s, t)
			verData = (LVertexData2D * 4)(LVertexData2D())
			iData = (GLuint * 4)(GLuint(0))

			#Definindo indices de renderização
			iData[0] = 0
			iData[1] = 1
			iData[2] = 2
			iData[3] = 3

			#Criando VBO
			self.mVBOID = glGenBuffers(1)
			glBindBuffer(GL_ARRAY_BUFFER, self.mVBOID)
			glBufferData(GL_ARRAY_BUFFER,sizeof(verData),verData,GL_DYNAMIC_DRAW)
			

			#Criando IBO 
			self.mIBOID = glGenBuffers(1)
			glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.mIBOID)
			glBufferData(GL_ELEMENT_ARRAY_BUFFER,sizeof(iData),iData,GL_DYNAMIC_DRAW)


			#Desativando buffer
			glBindBuffer(GL_ARRAY_BUFFER, 0)
			glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)


	@staticmethod
	def freeTexture(self):
		#Deletando textura
		if(self.mTextureID != 0):
			#glDeleteTextures(1,self.mTextureID)
			self.mTextureID = 0
		#Deletando pixels
		if(self.mPixels32 != None):
			del self.mPixels32
			self.mPixels32 = None
		if(self.mPixels8 != None):
			del self.mPixels8
			self.mPixels8 = None
		self.mTextureWidth = 0
		self.mTextureHeight = 0
		self.mImageHeight = 0
		self.mImageWidth = 0

		#Setando formato de pixel
		mPixelsFormat = None

	def loadTextureFromPixels32(self,pixels,imgWidth,imgHeight,texWidth,texHeigth):
		#Obtendo dimensoes de imagem
		self.mImageWidth = imgWidth
		self.mImageHeight = imgHeight
		self.mTextureWidth = texWidth
		self.mTextureHeight = texHeigth

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
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, DEFAULT_TEXTURE_WRAP)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, DEFAULT_TEXTURE_WRAP)

		#Liberando textura
		glBindTexture(GL_TEXTURE_2D,0)

		#Procurando erros
		erro = glGetError()
		if(erro != GL_NO_ERROR):
			print("Erro ao carregar textura de %p pixels! %s\n",pixels,gluErrorString(erro))
			return False
		#Gerando VBO
		self.initVBO()
		return True

	def loadTextureFromFile32(self,imagem):
		textureLoaded = False

		im = Image.open(imagem).convert("RGBA")
		if(im != None):
			#Inicializando dimensões
			imgWidth = im.width
			imgHeight = im.height

			#Calculando dimensões da textura
			texWidth = self.powerOfTwo(imgWidth)
			texHeigth = self.powerOfTwo(imgHeight)

			imagem = im.tobytes("raw","RGBA",0,-1)
			textureLoaded = self.loadTextureFromPixels32(imagem,imgWidth,imgHeight,texWidth,texHeigth)
		im.close()
		if(textureLoaded == False):
			print("Não foi possível carregar a imagem!")
		return textureLoaded

	def render(self,x,y,clip = None):
		#Se a textura existe
		if(self.mTextureID != 0):
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

			#Definindo dados do vertice 
			vData = (LVertexData2D * 4)(LVertexData2D())

			#Coordenadas da textura e dos vértices
			vData[0].texCoord.s = GLdouble(texLeft);	vData[0].position.x = GLdouble(0.0)
			vData[0].texCoord.t = GLdouble(texBottom);	vData[0].position.y = GLdouble(0.0)
			vData[1].texCoord.s = GLdouble(texRight);	vData[1].position.x = GLdouble(quadWidth)
			vData[1].texCoord.t = GLdouble(texBottom);	vData[1].position.y = GLdouble(0.0)
			vData[2].texCoord.s = GLdouble(texRight);	vData[2].position.x = GLdouble(quadWidth)
			vData[2].texCoord.t = GLdouble(texTop);		vData[2].position.y = GLdouble(quadHeight)
			vData[3].texCoord.s = GLdouble(texLeft);	vData[3].position.x = GLdouble(0.0)
			vData[3].texCoord.t = GLdouble(texTop);		vData[3].position.y = GLdouble(quadHeight)

			#Definindo textura ID
			glBindTexture(GL_TEXTURE_2D,self.mTextureID)
			
			#Habilitando vertice e coordenada de array de textura 
			glEnableClientState (GL_VERTEX_ARRAY)
			glEnableClientState (GL_TEXTURE_COORD_ARRAY)

			#Ativando buffer do vertice 
			glBindBuffer(GL_ARRAY_BUFFER,self.mVBOID)

			#Atualizando dados do buffer do vertice 
			glBufferSubData(GL_ARRAY_BUFFER,0,sizeof(vData),vData)

			#Set texture coordinate data
			glTexCoordPointer(2, GL_DOUBLE, sizeof(LVertexData2D), c_void_p(LVertexData2D.texCoord.offset))

		        #Set vertex data
			glVertexPointer(2, GL_DOUBLE, sizeof(LVertexData2D), c_void_p(LVertexData2D.position.offset))

			#Desenhando quadrado usando os dados do vertice e os dados do indice
			glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,self.mIBOID)
			glDrawElements(GL_QUADS,4,GL_UNSIGNED_INT,None)

			#Desabilitando vertices e coordenadas de arrays de vertice
			glDisableClientState(GL_TEXTURE_COORD_ARRAY)
			glDisableClientState(GL_VERTEX_ARRAY)

	def createPixels32(self,imgWidth, imgHeight):
		#Dimensões válidas
		if(imgWidth > 0 and imgHeight > 0):
			#Deletando qualquer dado de textura atual
			self.freeTexture(self)

			#Criando Pixels
			size = imgWidth * imgHeight
			self.mPixels32 = (GLuint * size)(GLuint())

			#Copiando dados do pixel
			self.mImageWidth = imgWidth
			self.mImageHeight = imgHeight
			self.mTextureWidth = self.mImageWidth
			self.mTextureHeight = self.mImageWidth

			#Setando formato de pixel
			self.mPixelsFormat = GL_RGBA

	def copyPixels32(self,pixels,imgWidth,imgHeight):
		#Pixel possui dimensões válidas
		if(imgWidth > 0 and imgHeight > 0):
			#Deletando qualquer dado de textura atual
			freeTexture()

			#Copiando Pixels
			size = imgWidth * imgHeight
			self.mPixels32 = (GLuint * size)(GLuint())

			#Copiando dados do pixel
			self.mImageWidth = imgWidth
			self.mImageHeight = imgHeight
			self.mTextureWidth = self.mImageWidth
			self.mTextureHeight = self.mImageWidth

			#Setando formato de pixel
			self.mPixelsFormat = GL_RGBA

	def blitPixels32(self,x,y,destination):
		#Se não existem pixels a serem exibidos
		if( self.mPixels32 != None and destination.mPixels32 != None ):
			#Copiando linhas de pixels
			dPixels = destination.mPixels32
			sPixels = self.mPixels32
			#Função memcpy

	def padPixels32(self):
		#Se existem pixels
		if(self.mPixels32 != None):
			#Atributos de textura antigos
			oTextureWidth = self.mTextureWidth
			oTextureHeight = self.mTextureHeight

			#Calculando dimensões de potencia de dois
			self.mTextureWidth = powerOfTwo( self.mImageWidth )
			self.mTextureHeight = powerOfTwo( self.mImageHeight )

			#O bitmap precisa mudar
			if( self.mTextureWidth != self.mImageWidth or self.mTextureHeight != self.mImageHeight ):
				#Alocando pixels
				size = self.mTextureWidth * self.mTextureHeight
				pixels = (GLuint * size)(GLuint())

				#Função memcpy

				#Mudando pixels
				del self.mPixels32
				self.mPixels32 = pixels

	def freeVBO(self):
		#Liberando VBO e IBO
		if (self.mVBOID != 0):
			glDeleteBuffers(1,self.mVBOID)		
			glDeleteBuffers(1,self.mIBOID)

	def createPixels8(self,imgWidth, imageHeight):
		#Dimensões válidas
		if(imgWidth > 0 and imgHeight > 0):
			#Deletando qualquer dado de textura atual
			freeTexture()

			#Criando Pixels
			size = imgWidth * imgHeight
			self.mPixels8 = (GLuint * size)(GLuint())

			#Copiando dados do pixel
			self.mImageWidth = imgWidth
			self.mImageHeight = imgHeight
			self.mTextureWidth = self.mImageWidth
			self.mTextureHeight = self.mImageWidth

			#Setando formato de pixel
			self.mPixelsFormat = GL_ALPHA

	def copyPixels8(self,pixels,imgWidth,imgHeight):
		#Dimensões válidas
		if(imgWidth > 0 and imgHeight > 0):
			#Deletando qualquer dado de textura atual
			self.freeTexture()

			#Criando Pixels
			size = imgWidth * imgHeight
			self.mPixels8 = (GLuint * size)(GLuint())

			#Copiando dados do pixel
			self.mImageWidth = imgWidth
			self.mImageHeight = imgHeight
			self.mTextureWidth = self.mImageWidth
			self.mTextureHeight = self.mImageWidth

			#Setando formato de pixel
			self.mPixelsFormat = GL_ALPHA

	def padPixels8(self):
		#Se existem pixels
		if(self.mPixels8 != None):
			#Atributos de textura antigos
			oTextureWidth = self.mTextureWidth
			oTextureHeight = self.mTextureHeight

			#Calculando dimensões de potencia de dois
			self.mTextureWidth = powerOfTwo( self.mImageWidth )
			self.mTextureHeight = powerOfTwo( self.mImageHeight )

			#O bitmap precisa mudar
			if( self.mTextureWidth != self.mImageWidth or self.mTextureHeight != self.mImageHeight ):
				#Alocando pixels
				size = self.mTextureWidth * self.mTextureHeight
				pixels = (GLuint * size)(GLuint())

				#Função memcpy

				#Mudando pixels
				del self.mPixels8
				self.mPixels8 = pixels

	def blitPixels8(self,x,y,destination):
		#Se não existem pixels a serem exibidos
		if( self.mPixels8 != None and destination.mPixels8 != None ):
			#Copiando linhas de pixels
			dPixels = destination.mPixels8
			sPixels = self.mPixels8
			#Função memcpy

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
			num = num | (num >> 8)
			num = num | (num >> 16)
			num += 1
		return num
