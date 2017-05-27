from LTexture import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Textura de sprite
gRepeatingTexture = LTexture();

#Coordenada de deslocamento de textura
gTexX = 0.0
gTexY = 0.0

#Tipo de envolvimento de textura
gTextureWrapType = 0

def initGL():
	#Definindo a janela de exibição (Viewport)
	glViewport(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

	#Inicializando Matriz de Projeção
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(0.0, SCREEN_WIDTH, SCREEN_HEIGHT, 0.0, 1.0, -1.0);

	#Inicializando Matriz de modelo de exibição (Modelview)
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	#Inicializando a tela com a cor preta
	glClearColor(0,0,0,1);

	#Habilitando textura
	glEnable(GL_TEXTURE_2D)

	#Misturando
	glEnable(GL_BLEND)
	glDisable(GL_DEPTH_TEST)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

	#Verificando se há erros
	erro = glGetError()
	if(erro != GL_NO_ERROR):
		print("Erro ao iniciar OpenGL! %s\n", gluErrorString(erro))
		return False
	return True

def loadMedia():
	#Carregando textura com cor ciano
	if(not gRepeatingTexture.loadTextureFromFile("texture.png")):
		print("Não foi possível carregar textura arrow!")
		return False
	return True

def update():
	global gTexY,gTexX,gRepeatingTexture

	gTexX += 1
	gTexY += 1

	#Rolagem
	if(gTexX >= gRepeatingTexture.textureWidth()):
		gTexX = 0.0
	if(gTexY >= gRepeatingTexture.textureHeight()):
		gTexY = 0.0

def render():
	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)

	#Calculando textura máxima
	textureRight = SCREEN_WIDTH / gRepeatingTexture.textureWidth()
	textureBottom = SCREEN_HEIGHT / gRepeatingTexture.textureHeight()

	#Usando textura repetida
	glBindTexture(GL_TEXTURE_2D, gRepeatingTexture.getTextureID())

	#Alterando para a matriz de textura
	glMatrixMode(GL_TEXTURE)

	#Resetando transformação
	glLoadIdentity()

	#Textura de rolagem
	glTranslatef(gTexX / gRepeatingTexture.textureWidth(), gTexY / gRepeatingTexture.textureHeight(), 0)

	#Renderizando
	glBegin(GL_QUADS)
	glTexCoord2f(0,0)
	glVertex2f(0,0)
	glTexCoord2f(textureRight,0)
	glVertex2f(SCREEN_WIDTH,0)
	glTexCoord2f(textureRight,textureBottom)
	glVertex2f(SCREEN_WIDTH,SCREEN_HEIGHT)
	glTexCoord2f(0,textureBottom)
	glVertex2f(0,SCREEN_HEIGHT)
	glEnd()

	#Atualizando tela
	glutSwapBuffers()

def handlekeys(key, x, y):
	global gTextureWrapType
	key = ord(key)
	
	#Se q é pressionado
	if(key == 113):
		#Ciclo através de repetições de texturas
		gTextureWrapType += 1
		if(gTextureWrapType > 4):
			gTextureWrapType = 0
		#Definindo repetição de textura
		glBindTexture(GL_TEXTURE_2D,gRepeatingTexture.getTextureID())
		switch(gTextureWrapType)

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)

#SWITCH

def caso_0():
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	print(gTextureWrapType,": GL_REPEAT")

def caso_1():
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	print(gTextureWrapType,": GL_CLAMP")

def caso_2():
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)
	print(gTextureWrapType,": GL_CLAMP_TO_BORDER")

def caso_3():
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
	print(gTextureWrapType,": GL_CLAMP_TO_EDGE")

def caso_4():
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT)
	print(gTextureWrapType,": GL_MIRRORED_REPEAT")

def switch(op):
	dic = {0: caso_0, 1: caso_1, 2: caso_2, 3: caso_3, 4: caso_4}

	dic[op]()