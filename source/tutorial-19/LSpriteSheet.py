from LVertexData2D import *
from LTexture import *

class LSpriteSheet(LTexture):
	def __init__(self):
		LTexture.__init__(self)
		#Inicializando dados do buffer do vértice
		self.mVertexDataBuffer = None
		self.mIndexBuffers = None
		self.mClips = []

	def __del__(self):
		#Limpando dados do sprite sheet
		self.freeSheet()

	def addClipSprite(self,newClip):
		#Adicionando clip e retornando indice
		self.mClips.append(newClip)
		return len(self.mClips) - 1

	def getClip(self,index):
		return self.mClips[index]

	def generateDataBuffer(self):
		#Se existe uma textura carregada e clips
		if(self.getTextureID != 0 and len(self.mClips) > 0):
			#Alocando dados do vértice de buffers
			totalSprites = len(self.mClips)
			totalVertexData = 4*totalSprites
			#(position(x,y), s, t)
			vertexData = (LVertexData2D * totalVertexData)(LVertexData2D())
			self.mIndexBuffers = (GLuint * 4)(GLuint(0))

			#Alocando dados do vértice de nomes de buffers
			self.mVertexDataBuffer = glGenBuffers(1)

			#Alocando nomes dos indices de buffers
			self.mIndexBuffers = glGenBuffers(totalSprites)

			#Andando através dos clips
			tw = self.textureWidth()
			th = self.textureHeight()
			

			for i in range(0,totalSprites):
				#Inicializando indices
				spriteIndices = (GLuint * 4)(GLuint(0))
				spriteIndices[0] = GLuint(i * 4 + 0)
				spriteIndices[1] = GLuint(i * 4 + 1)
				spriteIndices[2] = GLuint(i * 4 + 2)
				spriteIndices[3] = GLuint(i * 4 + 3)


				#Superior esquerda
				vertexData[spriteIndices[0]].position.x = GLdouble(-(self.mClips[i].w / 2))
				vertexData[spriteIndices[0]].position.y = GLdouble(-(self.mClips[i].h / 2))

				vertexData[spriteIndices[0]].texCoord.s = GLdouble((self.mClips[i].x) / tw)
				vertexData[spriteIndices[0]].texCoord.t = GLdouble((self.mClips[i].y) / th)

				#Superior direita
				vertexData[spriteIndices[1]].position.x = GLdouble(self.mClips[i].w / 2)
				vertexData[spriteIndices[1]].position.y = GLdouble(-self.mClips[i].h / 2)

				vertexData[spriteIndices[1]].texCoord.s = GLdouble((self.mClips[ i ].x + self.mClips[ i ].w) / tw)
				vertexData[spriteIndices[1]].texCoord.t = GLdouble((self.mClips[i].y) / th)

				#Inferior direita
				vertexData[spriteIndices[2]].position.x = GLdouble(self.mClips[i].w / 2)
				vertexData[spriteIndices[2]].position.y = GLdouble(self.mClips[i].h / 2)

				vertexData[spriteIndices[2]].texCoord.s = GLdouble((self.mClips[i].x + self.mClips[i].w) / tw)
				vertexData[spriteIndices[2]].texCoord.t = GLdouble((self.mClips[i].y + self.mClips[i].h) / th)

				#Inferior esquerda
				vertexData[spriteIndices[3]].position.x = GLdouble(-self.mClips[i].w / 2)
				vertexData[spriteIndices[3]].position.y = GLdouble(self.mClips[i].h / 2)

				vertexData[spriteIndices[3]].texCoord.s = GLdouble((self.mClips[i].x) / tw)
				vertexData[spriteIndices[3]].texCoord.t = GLdouble((self.mClips[i].y + self.mClips[i].h) / th)

				#Ativando dados dos índices do buffer
				glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.mIndexBuffers[i])
				glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(spriteIndices) , spriteIndices, GL_STATIC_DRAW)
			#Ativando dados do vértice
			glBindBuffer( GL_ARRAY_BUFFER, self.mVertexDataBuffer );
			glBufferData( GL_ARRAY_BUFFER, sizeof(vertexData), vertexData, GL_STATIC_DRAW );
			del vertexData

		else:
			if(getTextureID() == 0):
				print("Nenhuma textura para renderizar!\n")
			if(len(self.mClips) <= 0):
				print("Nenhum clip para gerar dados de vértice!\n")
			return False
		return True

	def freeSheet(self):
		#Limpando vértice de buffer
		if(self.mVertexDataBuffer != None):
			glDeleteBuffers(1,self.mVertexDataBuffer)
			self.mVertexDataBuffer = None
		#Limpando índices dos buffers
		if(self.mIndexBuffers != None):
			glDeleteBuffers(len(self.mClips), self.mIndexBuffers)
			del self.mIndexBuffers
			self.mIndexBuffers = None

		self.mClips.clear()

	def freeTexture(self):
		#Liberando dados de sprite sheet
		freeSheet()
		#Liberando textura
		freeTexture()

	def renderSprite(self,index):
		#Se dados de sprite sheet existe
		if(self.mVertexDataBuffer != None):
			#Setando textura
			glBindTexture(GL_TEXTURE_2D, self.getTextureID())

			#Habilitando coordenada de arrays de vértice e textura
			glEnableClientState(GL_VERTEX_ARRAY)
			glEnableClientState(GL_TEXTURE_COORD_ARRAY)

			#Ativando dados de vértice
			glBindBuffer(GL_ARRAY_BUFFER, self.mVertexDataBuffer)

			#Setando dados de coordenada de textura
			glTexCoordPointer( 2, GL_DOUBLE, sizeof(LVertexData2D), c_void_p(LVertexData2D.texCoord.offset));

			#Setando dados do vértice
			glVertexPointer( 2, GL_DOUBLE, sizeof(LVertexData2D), c_void_p(LVertexData2D.position.offset));

			#Desenhando quadrado usando dados do vértice e dados do índice
			glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, self.mIndexBuffers[ index ] );
			glDrawElements(GL_QUADS, 4, GL_UNSIGNED_INT, None);
		#Desabilitando coordenada de arrays de vértice e textura
		glDisableClientState( GL_TEXTURE_COORD_ARRAY );
		glDisableClientState( GL_VERTEX_ARRAY );
