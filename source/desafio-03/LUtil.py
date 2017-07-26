from LTexture import *
from Ponteiro import *
from Relogio import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Textura do tabuleiro de damas
gRelogio = None
gPonteiroH = None
gPonteiroM = None
gPonteiroS = None
screenColor = [0,0,0,1]

def initGL():
	#Definindo a janela de exibição (Viewport)
	glViewport(-SCREEN_WIDTH//2,-SCREEN_HEIGHT//2,SCREEN_WIDTH//2,SCREEN_HEIGHT//2)

	#Inicializando Matriz de Projeção
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-SCREEN_WIDTH//2, SCREEN_WIDTH//2, SCREEN_HEIGHT//2, -SCREEN_HEIGHT//2, 1.0, -1.0);

	#Inicializando Matriz de modelo de exibição (Modelview)
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	#Salvando a matriz padrão
	glPushMatrix()

	#Inicializando a tela com a cor preta
	glClearColor(screenColor[0], screenColor[1], screenColor[2], screenColor[3]);

	#Habilitando textura
	glEnable(GL_TEXTURE_2D)
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
	global gRelogio, gPonteiroH, gPonteiroM, gPonteiroS
	gRelogio = Relogio()
	gPonteiroH = Ponteiro('h')
	gPonteiroM = Ponteiro('m')
	gPonteiroS = Ponteiro('s')
	#Carregando textura
	flag = gRelogio.loadTextureFromFile("relogioCoca.png", screenColor)
	if(flag):
		flag = gPonteiroH.loadTextureFromFile("pontHoras.png")
	if(flag):
		flag = gPonteiroM.loadTextureFromFile("pontMinutos.png")
	if(flag):
		flag = gPonteiroS.loadTextureFromFile("pontSegundos.png")
	if(not flag):
		print("Não foi possível carregar a textura!")
	return flag

def update():
	global gPonteiroH
	gPonteiroH.rang += 1

def render():
	global gRelogio, gPonteiro
	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)

	#Obtendo coordenadas centrais
	x = (SCREEN_WIDTH - gRelogio.textureWidth()) / 2
	y = (SCREEN_HEIGHT - gRelogio.textureHeight()) / 2

	#Atualizando Matriz
	updateMatrix()

	#Renderizando relogio
	gRelogio.render(x,y)

	x = (SCREEN_WIDTH - gPonteiroH.textureWidth()) / 2
	y = (SCREEN_HEIGHT - gPonteiroH.textureHeight()) / 2 - 10
	
	#Atualizando Matriz
	updateMatrix()

	#Renderizando ponteiro
	gPonteiroH.render(x,y)
	
	x = (SCREEN_WIDTH - gPonteiroM.textureWidth()) / 2
	y = (SCREEN_HEIGHT - gPonteiroM.textureHeight()) / 2

	#Atualizando Matriz
	updateMatrix()

	#Renderizando ponteiro
	gPonteiroM.render(x,y)

	x = (SCREEN_WIDTH - gPonteiroS.textureWidth()) / 2
	y = (SCREEN_HEIGHT - gPonteiroS.textureHeight()) / 2

	#Atualizando Matriz
	updateMatrix()

	#Renderizando ponteiro
	gPonteiroS.render(x,y)
	
	#Atualizando tela
	glutSwapBuffers()

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)

def updateMatrix():
	#Retirando a matriz padrão para a matriz atual
	glMatrixMode(GL_MODELVIEW)
	glPopMatrix()
	glLoadIdentity()

	#Salvando matriz padrão
	glPushMatrix()