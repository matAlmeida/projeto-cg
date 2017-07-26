from LTexture import *
from Relogio import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Textura do tabuleiro de damas
gRelogio = None


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
	glClearColor(0,0,0,1)

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
	global gRelogio
	gRelogio = Relogio()
	flag = gRelogio.initTexture()
	if(not flag):
		print("Não foi possível carregar a textura!")
	return flag

def update():
	global gRelogio
	gRelogio.update()

def render():
	global gRelogio
	glClear(GL_COLOR_BUFFER_BIT)
	
	#Renderizando relogio
	gRelogio.render()
	
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