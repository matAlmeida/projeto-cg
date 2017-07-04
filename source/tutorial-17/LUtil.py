from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
from LVertexPos2D import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Vértices do quadrado
gQuadVertices = (LVertexPos2D * 4)(LVertexPos2D())


#Índices dos vértices
gIndices = (c_uint * 4)(c_uint())

#Buffer do Vértice
gVertexBuffer = GLuint(0)

#Index buffer
gIndexBuffer = GLuint(0)

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
	gQuadVertices[0].x = GLdouble(SCREEN_WIDTH * 1.0/4.0)
	gQuadVertices[0].y = GLdouble(SCREEN_HEIGHT * 1.0/4.0)

	gQuadVertices[1].x = GLdouble(SCREEN_WIDTH * 3.0/4.0)
	gQuadVertices[1].y = GLdouble(SCREEN_HEIGHT * 1.0/4.0)

	gQuadVertices[2].x = GLdouble(SCREEN_WIDTH * 3.0/4.0)
	gQuadVertices[2].y = GLdouble(SCREEN_HEIGHT * 3.0/4.0)

	gQuadVertices[3].x = GLdouble(SCREEN_WIDTH * 1.0/4.0)
	gQuadVertices[3].y = GLdouble(SCREEN_HEIGHT * 3.0/4.0)

	#Definindo índices de renderização
	gIndices[0] = 0
	gIndices[1] = 1
	gIndices[2] = 2
	gIndices[3] = 3

	#Criando VBO(Vertex Buffer Object)
	gVertexBuffer = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, gVertexBuffer)

	glBufferData(GL_ARRAY_BUFFER, sizeof(gQuadVertices), gQuadVertices, GL_STATIC_DRAW)


	#Criando IBO(Index Buffer Object)
	gIndexBuffer = glGenBuffers(1)
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, gIndexBuffer)

	glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(gIndices), gIndices, GL_STATIC_DRAW)

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
	glVertexPointer(2, GL_DOUBLE, sizeof(LVertexPos2D), c_void_p(LVertexPos2D.x.offset))

	#Desenhando quadrado usando os dados dos índices
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, gIndexBuffer)
	glDrawElements(GL_QUADS, 4, GL_UNSIGNED_INT,None)

	#Desabilitando array de vértices
	glDisableClientState(GL_VERTEX_ARRAY)

	#Atualizando tela
	glutSwapBuffers()
