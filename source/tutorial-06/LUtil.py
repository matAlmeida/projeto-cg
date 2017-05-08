from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from LTexture import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Textura do tabuleiro de damas
gLoadedTexture = LTexture();

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

	#Verificando se há erros
	erro = glGetError()
	if(erro != GL_NO_ERROR):
		print("Erro ao iniciar OpenGL! %s\n", gluErrorString(erro))
		return False
	return True

def loadMedia():
	#Carregando textura
	if(gLoadedTexture.loadTextureFromFile("opengl.png")):
		return True
	else:
		print("Não foi possível carregar a textura!")
		return False

def update():
	pass

def render():
	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT);

	#Obtendo coordenadas centrais
	x = (SCREEN_WIDTH - gLoadedTexture.textureWidth()) / 2
	y = (SCREEN_HEIGHT - gLoadedTexture.textureHeight()) / 2

	#Renderizando textura do tabuleiro
	gLoadedTexture.render(x,y)

	#Atualizando tela
	glutSwapBuffers()

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 / SCREEN_FPS, runMainLoop, val)