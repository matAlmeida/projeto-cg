from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

def initGL():
	#Inicializando Matriz de Projeção
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
    
	#Inicializando Matriz de modelo de visão (Modelview)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	
	#Inicializando a tela com a cor preta
	glClearColor(0,0,0,1)
	
	#Verificando se há erros
	erro = glGetError()
	if(erro != GL_NO_ERROR):
		print("Error initializing OpenGL! %s\n", gluErrorString(erro))
		return False
	return True

def update():
	pass

def render():
	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)

	#Renderizando o quadrado
	glBegin(GL_QUADS)
	glVertex2f(-0.5,-0.5)
	glVertex2f(0.5,-0.5)    	
	glVertex2f(0.5,0.5)
	glVertex2f(-0.5,0.5)
	glEnd()

	#Atualizando tela
	glutSwapBuffers()

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)