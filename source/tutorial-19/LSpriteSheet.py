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
			#(position(x,y), s, t)
			vertexData = array(totalSprites*4*[[0,0,0,0]], dtype = 'float32')
			self.mIndexBuffers = array(totalSprites*[0], dtype = 'int32')

			#Alocando dados do vértice de nomes de buffers
			self.mVertexDataBuffer = glGenBuffers(1)

			#Alocando nomes dos indices de buffers
			self.mIndexBuffers = glGenBuffers(totalSprites)

			#Andando através dos clips
			tw = self.textureWidth()
			th = self.textureHeight()
			spriteIndices = array([0,0,0,0], dtype = 'int32')

			for i in range(0,totalSprites):
				#Inicializando indices
				spriteIndices[0] = i * 4 + 0
				spriteIndices[1] = i * 4 + 1
				spriteIndices[2] = i * 4 + 2
				spriteIndices[3] = i * 4 + 3

				#Superior esquerda
				vertexData[spriteIndices[0]][0] = -(self.mClips[i].w / 2)
				vertexData[spriteIndices[0]][1] = -(self.mClips[i].h / 2)

				vertexData[spriteIndices[0]][2] = (self.mClips[i].x) / tw
				vertexData[spriteIndices[0]][3] = (self.mClips[i].y) / th

				#Superior direita
				vertexData[spriteIndices[1]][0] = -self.mClips[i].w / 2
				vertexData[spriteIndices[1]][1] = -self.mClips[i].h / 2

				vertexData[spriteIndices[1]][2] = (self.mClips[ i ].x + self.mClips[ i ].w) / tw
				vertexData[spriteIndices[1]][3] = (self.mClips[i].y) / th

				#Inferior direita
				vertexData[spriteIndices[1]][0] = -self.mClips[i].w / 2
				vertexData[spriteIndices[1]][1] = -self.mClips[i].h / 2

				vertexData[spriteIndices[1]][2] = (self.mClips[i].x + self.mClips[i].w) / tw
				vertexData[spriteIndices[1]][3] = (self.mClips[i].y + self.mClips[i].h) / th;

				#Inferior esquerda
				vertexData[spriteIndices[1]][0] = -self.mClips[i].w / 2
				vertexData[spriteIndices[1]][1] = -self.mClips[i].h / 2

				vertexData[spriteIndices[1]][2] = (self.mClips[i].x) / tw
				vertexData[spriteIndices[1]][3] = (self.mClips[i].y + self.mClips[i].h) / th;

				#Ativando dados dos índices do buffer
				glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.mIndexBuffers[i])
				glBufferData(GL_ELEMENT_ARRAY_BUFFER, 4 * GLuint().__sizeof__(), spriteIndices, GL_STATIC_DRAW)
			#Ativando dados do vértice
			glBindBuffer( GL_ARRAY_BUFFER, self.mVertexDataBuffer );
			glBufferData( GL_ARRAY_BUFFER, totalSprites * 4 * LVertexData2D().__sizeof__(), vertexData, GL_STATIC_DRAW );

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
			#glTexCoordPointer( 2, GL_FLOAT, LVertexData2D().__sizeof__(), offsetof( LVertexData2D, texCoord ));

			#Setando dados do vértice
			#glVertexPointer( 2, GL_FLOAT, LVertexData2D().__sizeof__(), offsetof( LVertexData2D, position) );

			#Desenhando quadrado usando dados do vértice e dados do índice
			glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, self.mIndexBuffers[ index ] );
			glDrawElements(GL_QUADS, 4, GL_UNSIGNED_INT, None);
		#Desabilitando coordenada de arrays de vértice e textura
		glDisableClientState( GL_TEXTURE_COORD_ARRAY );
		glDisableClientState( GL_VERTEX_ARRAY );