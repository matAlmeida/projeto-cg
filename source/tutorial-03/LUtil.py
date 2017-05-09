from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Constantes de Tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_FPS = 60

#Modo de exibição da janela (viewport)
VIEWPORT_MODE_FULL = 0
VIEWPORT_MODE_HALF_CENTER = 1
VIEWPORT_MODE_HALF_TOP = 2
VIEWPORT_MODE_QUAD = 3
VIEWPORT_MODE_RADAR = 4

#Modo Viewport
gViewportMode = VIEWPORT_MODE_FULL

def initGL():
	#Configurando viewport
	glViewport(0,0, SCREEN_WIDTH, SCREEN_HEIGHT)

	#Inicializando Matriz de Projeção
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, SCREEN_WIDTH, SCREEN_HEIGHT, 0.0, 1.0, -1.0)

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
	glClear(GL_COLOR_BUFFER_BIT);

	#Reiniciando a matriz Modelview
	glLoadIdentity();

	#Movendo a  para o centro da tela
	glTranslatef(SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0, 0.0);

	#Visão completa
	if(gViewportMode == VIEWPORT_MODE_FULL):
		#Preenchendo a tela
		glViewport(0,0,SCREEN_WIDTH, SCREEN_HEIGHT)

		#Quadrado vermelho
		glBegin(GL_QUADS)
		glColor3f(1,0,0)
		glVertex2f(-SCREEN_WIDTH/2, -SCREEN_HEIGHT / 2)
		glVertex2f(SCREEN_WIDTH/2, -SCREEN_HEIGHT / 2)
		glVertex2f(SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)
		glVertex2f(-SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)
		glEnd()

	#Janela exibida no centro da tela
	elif(gViewportMode == VIEWPORT_MODE_HALF_CENTER):
		#viewport central
		glViewport(int(SCREEN_WIDTH / 4), int(SCREEN_HEIGHT / 4),int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))

		#Quadrado verde
		glBegin(GL_QUADS)
		glColor3f(0,1,0)
		glVertex2f(-SCREEN_WIDTH/2, -SCREEN_HEIGHT / 2)
		glVertex2f(SCREEN_WIDTH/2, -SCREEN_HEIGHT / 2)
		glVertex2f(SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)
		glVertex2f(-SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)
		glEnd()

	#Viewport centralizada no topo da tela
	elif(gViewportMode == VIEWPORT_MODE_HALF_TOP):
		#Viewport do topo
		glViewport(int(SCREEN_WIDTH / 4), int(SCREEN_HEIGHT / 2),int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))

		#Quadrado vermelho
		glBegin(GL_QUADS)
		glColor3f(0,0,1)
		glVertex2f(-SCREEN_WIDTH/2, -SCREEN_HEIGHT / 2)
		glVertex2f(SCREEN_WIDTH/2, -SCREEN_HEIGHT / 2)
		glVertex2f(SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)
		glVertex2f(-SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)
		glEnd()

	#Configurando as quatro viewports
	elif(gViewportMode == VIEWPORT_MODE_QUAD):
		#Quadrado vermelho inferior esquerdo
		glViewport(0,0,int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
		glBegin(GL_QUADS)
		glColor3f(1,0,0)
		glVertex2f(-SCREEN_WIDTH/4, -SCREEN_HEIGHT / 4)
		glVertex2f(SCREEN_WIDTH/4, -SCREEN_HEIGHT / 4)
		glVertex2f(SCREEN_WIDTH/4, SCREEN_HEIGHT / 4)
		glVertex2f(-SCREEN_WIDTH/4, SCREEN_HEIGHT / 4)
		glEnd()

		#Quadrado verde inferior direito
		glViewport(int(SCREEN_WIDTH / 2), 0, int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
		glBegin(GL_QUADS)
		glColor3f(0,1,0)
		glVertex2f(-SCREEN_WIDTH/4, -SCREEN_HEIGHT / 4)
		glVertex2f(SCREEN_WIDTH/4, -SCREEN_HEIGHT / 4)
		glVertex2f(SCREEN_WIDTH/4, SCREEN_HEIGHT / 4)
		glVertex2f(-SCREEN_WIDTH/4, SCREEN_HEIGHT / 4)
		glEnd()

		#Quadrado azul superior esquerdo
		glViewport(0, int(SCREEN_HEIGHT / 2), int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
		glBegin(GL_QUADS)
		glColor3f(0,0,1)
		glVertex2f(-SCREEN_WIDTH/4, -SCREEN_HEIGHT / 4)
		glVertex2f(SCREEN_WIDTH/4, -SCREEN_HEIGHT / 4)
		glVertex2f(SCREEN_WIDTH/4, SCREEN_HEIGHT / 4)
		glVertex2f(-SCREEN_WIDTH/4, SCREEN_HEIGHT / 4)
		glEnd()

		#Quadrado amarelo superior direito
		glViewport(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
		glBegin(GL_QUADS)
		glColor3f(1,1,0)
		glVertex2f(-SCREEN_WIDTH/4, -SCREEN_HEIGHT / 4)
		glVertex2f(SCREEN_WIDTH/4, -SCREEN_HEIGHT / 4)
		glVertex2f(SCREEN_WIDTH/4, SCREEN_HEIGHT / 4)
		glVertex2f(-SCREEN_WIDTH/4, SCREEN_HEIGHT / 4)
		glEnd()

	#Viewport com subjanela de exibição
	elif(gViewportMode == VIEWPORT_MODE_RADAR):
		#Quadrado de tamanho completo
		glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
		glBegin(GL_QUADS)
		glColor3f(1,1,1)
		glVertex2f(-SCREEN_WIDTH/8, -SCREEN_HEIGHT / 8)
		glVertex2f(SCREEN_WIDTH/8, -SCREEN_HEIGHT / 8)
		glVertex2f(SCREEN_WIDTH/8, SCREEN_HEIGHT / 8)
		glVertex2f(-SCREEN_WIDTH/8, SCREEN_HEIGHT / 8)
		glColor3f(0,0,0)
		glVertex2f(-SCREEN_WIDTH/16, -SCREEN_HEIGHT / 16)
		glVertex2f(SCREEN_WIDTH/16, -SCREEN_HEIGHT / 16)
		glVertex2f(SCREEN_WIDTH/16, SCREEN_HEIGHT / 16)
		glVertex2f(-SCREEN_WIDTH/16, SCREEN_HEIGHT / 16)
		glEnd()

		#Quadrado de radar
		glViewport(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
		glBegin(GL_QUADS)
		glColor3f(1,1,1)
		glVertex2f(-SCREEN_WIDTH/8, -SCREEN_HEIGHT / 8)
		glVertex2f(SCREEN_WIDTH/8, -SCREEN_HEIGHT / 8)
		glVertex2f(SCREEN_WIDTH/8, SCREEN_HEIGHT / 8)
		glVertex2f(-SCREEN_WIDTH/8, SCREEN_HEIGHT / 8)
		glColor3f(0,0,0)
		glVertex2f(-SCREEN_WIDTH/16, -SCREEN_HEIGHT / 16)
		glVertex2f(SCREEN_WIDTH/16, -SCREEN_HEIGHT / 16)
		glVertex2f(SCREEN_WIDTH/16, SCREEN_HEIGHT / 16)
		glVertex2f(-SCREEN_WIDTH/16, SCREEN_HEIGHT / 16)
		glEnd()

	#Atualizando tela
	glutSwapBuffers();

def runMainLoop(val):
	#Frame logic
	update()
	render()

	#Run frame one more time
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)

def handleKeys(key,x,y):
	global gViewportMode
	key = ord(key)
	print("key: "+str(key))
	#Se o usuario pressiona q
	if(key == 113):
		#Ciclos através de escalas de projeção
		gViewportMode += 1
		if(gViewportMode > VIEWPORT_MODE_RADAR):
			gViewportMode = VIEWPORT_MODE_FULL
		glutPostRedisplay()