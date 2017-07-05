from LSpriteSheet import *

class LFont(LSpriteSheet):
	def __init__(self):
		LSpriteSheet.__init__(self)
		self.mSpace = 0.0
		self.mLineHeight = 0.0
		self.mNewLine = 0.0

	def __del__(self):
		#Deletando fonte
		self.freeFont()

	def loadBitmap(self,imagem):
		#Iniciando flag
		success = True

		#Pixel de fundo
		BLACK_PIXEL = 0xFF000000

		#Liberando a fonte, se ela existe
		self.freeFont()

		#Carregando pixels da imagem
		if(self.loadPixelsFromFile(imagem)):
			#Obtendo dimensões da célula
			cellW = self.imageWidth() // 16
			cellH = self.imageHeight() // 16

			#Obtendo letra do topo e inferior
			top = cellH
			bottom = 0
			aBottom = 0

			#Coordenadas atuais do pixel
			pX = 0
			pY = 0

			#Offsets da base da célula
			bX = 0
			bY = 0

			#Iniciando analise de fonte bitmap
			currentChar = 0
			nextClip = LFRect(0,0,cellW,cellH)

			#Navegando pelas linhas de células
			for rows in range(0,16):
				for cols in range(0,16):
					#Iniciando analise de celula

					#Setando base offsets
					bX = cellW * cols
					bY = cellH * rows

					#Inicializando clip
					nextClip.x = cellW * cols
					nextClip.y = cellH * rows

					nextClip.w = cellW
					nextClip.h = cellH

					#Encontrando lado esquerdo do caractere
					for pCol in range(0,cellW):
						for pRow in range(0,cellH):
							#Setando pixel offset
							pX = bX + pCol
							pY = bY + pRow

							#Nenhum pixel de fundo encontrado
							if(self.getPixel32(pX,pY) != BLACK_PIXEL):
								#Setando x do offset sprite
								nextClip.x = pX

								#Quebrando os loops
								pCol = cellW
								pRow = cellH

					#Lado direito
					for pCol_w in range(cellW-1,0):
						for pRow_w in range(0,cellH):
							#Setando pixel offset
							pX = bX + pCol_w
							pY = bY + pRow_w

							#Nenhum pixel de fundo encontrado
							if(getPixel32(pX,pY) != BLACK_PIXEL):
								#Setando largura do offset sprite
								nextClip.w = (pX - nextClip.x) + 1

								#Quebrando os loops
								pCol = -1
								pRow = cellH

					#Encontrando topo
					for pRow in range(0,cellH):
						for pCol in range(0,cellW):
							#Setando pixel offset
							pX = bX + pCol
							pY = bY + pRow

							#Nenhum pixel de fundo encontrado
							if(self.getPixel32(pX,pY) != BLACK_PIXEL):
								#Novo topo encontrado
								if(pRow < top):
									top = pRow

								#Quebrando os loops
								pCol = cellW
								pRow = cellH

					#Encontrando parte inferior
					for pRow_b in range(cellH-1,0):
						for pCol_b in range(0,cellW):
							#Setando pixel offset
							pX = bX + pCol_b
							pY = bY + pRow_b

							#Nenhum pixel de fundo encontrado
							if(getPixel32(pX,pY) != BLACK_PIXEL):
								#Setando BaseLine
								if(currentChar == 'A'):
									aBottom = pRow_b

								#Quebrando os loops
								pCol = cellW
								pRow = -1
					#Indo para o proximo caractere
					self.mClips.append(nextClip)
					currentChar += 1
			#Setando topo
			for t in range(0,256):
				self.mClips[t].y += top
				self.mClips[t].h -= top

			#Mistura
			RED_BYTE = 1
			GREEN_BYTE = 1
			BLUE_BYTE = 2
			ALPHA_BYTE = 3

			#Andando através os pixels
			PIXEL_COUNT = self.textureWidth() * self.textureHeight()
			pixels = self.getPixelData32()
			'''
			for i in range(0,PIXEL_COUNT):
				#Obtendo cores individuais de componentes
				colors = pixels[i]

				#Pixel branco como transparente
				colors[ALPHA_BYTE] = colors[RED_BYTE]
				colors[RED_BYTE] = 0xFF
				colors[GREEN_BYTE] = 0xFF
				colors[BLUE_BYTE] = 0xFF
			'''
			#Criando textura a partir de pixels manipulados
			if(self.loadTextureFromPixels32()):
				#Construindo buffer de vértice a partir dos dados de sprite sheet
				if(not self.generateDataBuffer(LSPRITE_ORIGIN_TOP_LEFT)):
					print("Não foi possível criar buffer de vértice para font bitmap!\n")
					success = False
			else:
				print("Não foi possível criar textura a partir de pixels de fonte bitmap!\n")
				success = False

			#Setando textura wrap
			glBindTexture( GL_TEXTURE_2D, self.getTextureID() )
			glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER )
			glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER )

			#Setando variáveis de espaço
			self.mSpace = cellW / 2
			self.mNewLine = aBottom - top
			mLineHeight = bottom - top
		else:
			print("Não foi possível carregar imagem de fonte bitmap: %s!\n",imagem)
		return success

	def freeFont(self):
		#Liberando sprite sheet
		#self.freeTexture()

		#Reinicializando constantes de espaço
		self.mSpace = 0
		mLineHeight = 0
		self.mNewLine = 0

	def renderText(self,x,y,text):
		#Se existe uma textura
		if(self.getTextureID() != 0):
			#Posições de desenho
			dX = x
			dY = y

			#Movendo para a posição de desenho
			glTranslatef(x,y,0)

			#Setando textura
			glBindTexture(GL_TEXTURE_2D, self.getTextureID())

			#Habilitando vértice e coordenada dos arrays de textura
			glEnableClientState( GL_VERTEX_ARRAY )
			glEnableClientState( GL_TEXTURE_COORD_ARRAY )

			#Ativando dados do vértice
			glBindBuffer( GL_ARRAY_BUFFER, self.mVertexDataBuffer )

			#Setando dados da coordenada da textura
			glTexCoordPointer( 2, GL_DOUBLE, sizeof(LVertexData2D), c_void_p(LVertexData2D.texCoord.offset) )
			
			#Setando dados do vértice
			glVertexPointer( 2, GL_DOUBLE, sizeof(LVertexData2D), c_void_p(LVertexData2D.position.offset) )

			#Navegando através da string
			for i in range(0,len(text)):
				#Espaço
				if(text[i] == ' '):
					glTranslatef(self.mSpace,0,0)
					dX += self.mSpace
				#Nova Linha
				elif(text[i] == '\n'):
					glTranslatef( x - dX, self.mNewLine, 0 )
					dY += self.mNewLine
					dX += x - dX
				#Caractere
				else:
					#Obtendo caractere ASCII
					asc = ord(text[i])
					print(chr(self.mIndexBuffers[ 15 ]))
					#Desenhando quadrado usando dados do vertice e dados do índice
					glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, GLuint(self.mIndexBuffers[asc]) )
					glDrawElements( GL_QUADS, 4, GL_UNSIGNED_INT, None )

					#Movendo
					glTranslatef( self.mClips[ asc ].w, 0, 0 )
					dX += self.mClips[ asc ].w
					
		#Desabilitando arrays de coordenadas de vértide e de textura
		glDisableClientState( GL_TEXTURE_COORD_ARRAY )
		glDisableClientState( GL_VERTEX_ARRAY )
