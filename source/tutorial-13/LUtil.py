from LTexture import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Textura de sprite
gRotatingTexture = LTexture();

#Ângulo de rotação
gAngle = 360.0

#Estado de transformação
gTransformationCombo = 0

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
	if(not gRotatingTexture.loadTextureFromFileWithColorKey("texture.png")):
		print("Não foi possível carregar textura arrow!")
		return False
	return True

def update():
	global gAngle
	#Rotacionando
	gAngle -= 360.0 / SCREEN_FPS

	#Angulação
	if(gAngle < 0.0):
		gAngle += 360.0

def render():
	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT);

	#Resetando transformação
	glLoadIdentity()

	#Renderizando cena de transformação atual
	switch(gTransformationCombo)

	#Renderizando o seta
	gRotatingTexture.render(0,0)

	#Atualizando tela
	glutSwapBuffers()

def handlekeys(key, x, y):
	global gAngle, gTransformationCombo
	key = ord(key)
	
	#Se q é pressionado
	if(key == 113):
		#Resetando rotação
		gAngle = 0

		#Ciclo através de combinações
		gTransformationCombo += 1
		if(gTransformationCombo > 4):
			gTransformationCombo = 0

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)

#SWITCH

def caso_0():
	glTranslatef(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0)
	glRotatef(gAngle,0,0,1)
	glScalef(2,2,0)
	glTranslatef(gRotatingTexture.imageWidth() / -2	, gRotatingTexture.imageHeight() / -2, 0)


def caso_1():
	glTranslatef(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0)
	glRotatef(gAngle,0,0,1)
	glTranslatef(gRotatingTexture.imageWidth() / -2, gRotatingTexture.imageHeight() / -2, 0)
	glScalef(2,2,0)

def caso_2():
	glScalef(2,2,0)
	glTranslatef(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0)
	glRotatef(gAngle,0,0,1)
	glTranslatef(gRotatingTexture.imageWidth() / -2, gRotatingTexture.imageHeight() / -2, 0)


def caso_3():
	glTranslatef(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0)
	glRotatef(gAngle,0,0,1)
	glScalef(2,2,0)
	
def caso_4():
	glRotatef(gAngle,0,0,1)
	glTranslatef(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0)
	glScalef(2,2,0)
	glTranslatef(gRotatingTexture.imageWidth() / -2, gRotatingTexture.imageHeight() / -2, 0)

def switch(op):
	dic = {0: caso_0, 1: caso_1, 2: caso_2, 3: caso_3, 4: caso_4}

	dic[op]()