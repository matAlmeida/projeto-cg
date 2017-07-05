from LTexture import *

LSPRITE_ORIGIN_CENTER = 0
LSPRITE_ORIGIN_TOP_LEFT = 1
LSPRITE_ORIGIN_BOTTOM_LEFT = 2
LSPRITE_ORIGIN_TOP_RIGHT = 3
LSPRITE_ORIGIN_BOTTOM_RIGHT = 4

class LSpriteSheet(LTexture):
	def __init__(self):
		LTexture.__init__(self)
		#Inicializando dados do buffer do vértice
		self.mVertexDataBuffer = 0
		self.mIndexBuffers = None
		self.mClips = []

	def __del__(self):
		#Limpando dados do sprite sheet
		self.freeSheet()

	def addClipSprite(self,newClip):
		#Adicionando clip e retornando indice
		
		self.mClips.append(newClip)
		return (len(self.mClips) - 1)

	def getClip(self,index):
		return self.mClips[index]

	def generateDataBuffer(self, origin = LSPRITE_ORIGIN_CENTER):
		#Se existe uma textura carregada e clips
		if(self.getTextureID != 0 and len(self.mClips) > 0):
			#Alocando dados do vértice de buffers
			totalSprites = len(self.mClips)
			#(position(x,y), s, t)
			vertexData = (totalSprites * 4 * LVertexData2D)(LVertexData2D())
			self.mIndexBuffers = (totalSprites * GLuint)(GLuint(0))

			self.mIndexBuffers = (GLuint * 4)(GLuint(0))
			#Alocando dados do vértice de nomes de buffers
			self.mVertexDataBuffer = glGenBuffers(1)

			#Alocando nomes dos indices de buffers
			self.mIndexBuffers = glGenBuffers(totalSprites)

			#Andando através dos clips
			tw = self.textureWidth()
			th = self.textureHeight()

			spriteIndices = (4 * GLuint)(GLuint(0))

			#Variáveis de origem
			vTop = 0.0
			vBottom = 0.0
			vLeft = 0.0
			vRight = 0.0

			for i in range(0,totalSprites):
				#Inicializando indices
				spriteIndices[0] = i * 4 + 0
				spriteIndices[1] = i * 4 + 1
				spriteIndices[2] = i * 4 + 2
				spriteIndices[3] = i * 4 + 3

				#Setando origem
				if(origin == LSPRITE_ORIGIN_TOP_LEFT):
					vTop = 0.0
					vBottom = self.mClips[i].h
					vLeft = 0.0
					vRight = self.mClips[i].w
				elif(origin == LSPRITE_ORIGIN_TOP_RIGHT):
					vTop = 0.0
					vBottom = self.mClips[i].h
					vLeft = -self.mClips[i].w
					vRight = 0.0
				elif(origin == LSPRITE_ORIGIN_BOTTOM_LEFT):
					vTop = -self.mClips[i].h
					vBottom = 0.0
					vLeft = 0.0
					vRight = self.mClips[i].w
				elif(origin == LSPRITE_ORIGIN_BOTTOM_RIGHT):
					vTop = -self.mClips[i].h
					vBottom = 0.0
					vLeft = -self.mClips[i].w
					vRight = 0.0
				else:
					vTop = -self.mClips[i].h / 2
					vBottom = self.mClips[i].h / 2
					vLeft = -self.mClips[i].w / 2
					vRight = self.mClips[i].w / 2

				#Superior esquerda
				vertexData[spriteIndices[0]].position.x = vLeft
				vertexData[spriteIndices[0]].position.y = vTop

				vertexData[spriteIndices[0]].texCoord.s = (self.mClips[i].x) / tw
				vertexData[spriteIndices[0]].texCoord.t = (self.mClips[i].y) / th

				#Superior direita
				vertexData[spriteIndices[1]].position.x = vRight
				vertexData[spriteIndices[1]].position.y = vTop

				vertexData[spriteIndices[1]].texCoord.s = (self.mClips[i].x + self.mClips[i].w) / tw
				vertexData[spriteIndices[1]].texCoord.t = (self.mClips[i].y) / th

				#Inferior direita
				vertexData[spriteIndices[2]].position.x = vRight
				vertexData[spriteIndices[2]].position.y = vBottom

				vertexData[spriteIndices[2]].texCoord.s = (self.mClips[i].x + self.mClips[i].w) / tw
				vertexData[spriteIndices[2]].texCoord.t = (self.mClips[i].y + self.mClips[i].h) / th;

				#Inferior esquerda

				vertexData[spriteIndices[3]].position.x = vLeft
				vertexData[spriteIndices[3]].position.y = vBottom

				vertexData[spriteIndices[3]].texCoord.s = (self.mClips[i].x) / tw
				vertexData[spriteIndices[3]].texCoord.t = (self.mClips[i].y + self.mClips[i].h) / th;

				#Ativando dados dos índices do buffer
				glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.mIndexBuffers[i])

				glBufferData(GL_ELEMENT_ARRAY_BUFFER, 4 * sizeof(GLuint()), spriteIndices, GL_STATIC_DRAW)
			#Ativando dados do vértice
			glBindBuffer( GL_ARRAY_BUFFER, self.mVertexDataBuffer );
			glBufferData( GL_ARRAY_BUFFER, totalSprites * 4 * sizeof(LVertexData2D()), vertexData, GL_STATIC_DRAW );

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
		if(self.mVertexDataBuffer != 0):
			glDeleteBuffers(1,self.mVertexDataBuffer)
			self.mVertexDataBuffer = 0
		#Limpando índices dos buffers
		if(self.mIndexBuffers != None):
			glDeleteBuffers(len(self.mClips), self.mIndexBuffers)
			del self.mIndexBuffers
			self.mIndexBuffers = None

		self.mClips.clear()

	def freeTexture(self):
		pass
		#Liberando dados de sprite sheet
		#self.freeSheet()
		#Liberando textura
		#self.freeTexture()

	def renderSprite(self,index):
		#Se dados de sprite sheet existe
		if(self.mVertexDataBuffer != 0):
			#Setando textura
			#pdb.set_trace()
			glBindTexture(GL_TEXTURE_2D, self.getTextureID())

			#Habilitando coordenada de arrays de vértice e textura
			glEnableClientState(GL_VERTEX_ARRAY)
			glEnableClientState(GL_TEXTURE_COORD_ARRAY)

			#Ativando dados de vértice
			glBindBuffer(GL_ARRAY_BUFFER, self.mVertexDataBuffer)

			#Setando dados de coordenada de textura

			glTexCoordPointer( 2, GL_DOUBLE, sizeof(LVertexData2D()), c_void_p(LVertexData2D.texCoord.offset));

			#Setando dados do vértice
			glVertexPointer( 2, GL_DOUBLE, sizeof(LVertexData2D()), c_void_p(LVertexData2D.position.offset));

			#Desenhando quadrado usando dados do vértice e dados do índice
			glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, self.mIndexBuffers[ index ] );
			glDrawElements(GL_QUADS, 4, GL_UNSIGNED_INT, None);
			import pdb
			pdb.set_trace()
		#Desabilitando coordenada de arrays de vértice e textura
		glDisableClientState( GL_TEXTURE_COORD_ARRAY );
		glDisableClientState( GL_VERTEX_ARRAY );
