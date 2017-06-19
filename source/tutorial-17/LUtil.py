from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Vértices do quadrado
gQuadVertices = array([[0,0],[0,0],[0,0],[0,0]], dtype='float32')


#Índices dos vértices
gIndices = array([0,0,0,0], dtype='int32')

#Buffer do Vértice
gVertexBuffer = 0

#Index buffer
gIndexBuffer = 0

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
	global gQuadVertices, gVertexBuffer, gIndexBuffer, gIndices

	#Definindo vértices do quadrado
	gQuadVertices[0][0] = SCREEN_WIDTH * 1.0/4.0
	gQuadVertices[0][1] = SCREEN_HEIGHT * 1.0/4.0

	gQuadVertices[1][0] = SCREEN_WIDTH * 3.0/4.0
	gQuadVertices[1][1] = SCREEN_HEIGHT * 1.0/4.0

	gQuadVertices[2][0] = SCREEN_WIDTH * 3.0/4.0
	gQuadVertices[2][1] = SCREEN_HEIGHT * 3.0/4.0

	gQuadVertices[3][0] = SCREEN_WIDTH * 1.0/4.0
	gQuadVertices[3][1] = SCREEN_HEIGHT * 3.0/4.0

	#Definindo índices de renderização
	gIndices[0] = 0
	gIndices[1] = 1
	gIndices[2] = 2
	gIndices[3] = 3

	#Criando VBO(Vertex Buffer Object)
	gVertexBuffer = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, gVertexBuffer)
	#(2*float.__sizeof__(0.0)) pois são duas coordenadas para cada vértice
	glBufferData(GL_ARRAY_BUFFER, 4 * (2*float.__sizeof__(0.0)), gQuadVertices, GL_STATIC_DRAW)


	#Criando IBO(Index Buffer Object)
	gIndexBuffer = glGenBuffers(1)
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, gIndexBuffer)
	#(2*float.__sizeof__(1)) pois são duas coordenadas para cada vértice
	glBufferData(GL_ELEMENT_ARRAY_BUFFER, 4 * (int.__sizeof__(1)), gIndices, GL_STATIC_DRAW)

	return True

def update():
	pass

def render():
	global gQuadVertices, gVertexBuffer, gIndexBuffer

	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)

	#Ativando array de vértices
	glEnableClientState(GL_VERTEX_ARRAY)

	#Definindo dados do vértice
	glBindBuffer(GL_ARRAY_BUFFER, gVertexBuffer)
	glVertexPointer(2, GL_FLOAT, 0, None)

	#Desenhando quadrado usando os dados dos índices
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, gIndexBuffer)
	glDrawElements(GL_QUADS, 4, GL_UNSIGNED_INT,None)

	#Desabilitando array de vértices
	glDisableClientState(GL_VERTEX_ARRAY)

	#Atualizando tela
	glutSwapBuffers()
