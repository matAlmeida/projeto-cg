from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Vértices do quadrado
#4 coordenadas (x,y): posição 2D do vértice
gQuadVertices = [[0,0],[0,0],[0,0],[0,0]]

def initGL():
	#Definindo a janela de exibição (Viewport)
	glViewport(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

	#Inicializando Matriz de Projeção
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho( 0.0, SCREEN_WIDTH, SCREEN_HEIGHT, 0.0, 1.0, -1.0 );
    
	#Inicializando Matriz de modelo de visão (Modelview)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	
	#Inicializando a tela com a cor preta
	glClearColor(0,0,0,1)
	
	#Ativando textura
	glEnable(GL_TEXTURE_2D)

	#Ativando combinação
	glEnable(GL_BLEND)
	glDisable(GL_DEPTH_TEST)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

	#Verificando se há erros
	erro = glGetError()
	if(erro != GL_NO_ERROR):
		print("Error initializing OpenGL! %s\n", gluErrorString(erro))
		return False
	return True


def loadMedia():
	global gQuadVertices

	#Definindo vértices do quadrado
	gQuadVertices[0][0] = SCREEN_WIDTH * 1.0/4.0
	gQuadVertices[0][1] = SCREEN_HEIGHT * 1.0/4.0

	gQuadVertices[1][0] = SCREEN_WIDTH * 3.0/4.0
	gQuadVertices[1][1] = SCREEN_HEIGHT * 1.0/4.0

	gQuadVertices[2][0] = SCREEN_WIDTH * 3.0/4.0 
	gQuadVertices[2][1] = SCREEN_HEIGHT * 3.0/4.0 

	gQuadVertices[3][0] = SCREEN_WIDTH * 1.0/4.0
	gQuadVertices[3][1] = SCREEN_HEIGHT * 3.0/4.0 

	return True

def update():
	pass

def render():
	global gQuadVertices

	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)

	#Ativando array de vértices
	glEnableClientState(GL_VERTEX_ARRAY)

	#Definindo dados do vértice
	glVertexPointer(2, GL_FLOAT, 0, gQuadVertices)

	#Desenhando quadrado usando os dados do vértice
	glDrawArrays(GL_QUADS,0,4)

	#Desabilitando array de vértices
	glDisableClientState(GL_VERTEX_ARRAY)

	#Atualizando tela
	glutSwapBuffers()