from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math as mt

#Constantes de Tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_FPS = 60

#Modos de cor
COLOR_MODE_CYAN = 0
COLOR_MODE_MULTI = 1

#Modos de renderização
RENDER_SQUARE = 2
RENDER_CIRCLE = 3
RENDER_PACMAN = 4

#Modo atual de renderização de cor
gColorMode = COLOR_MODE_CYAN

#Tipo de objeto a ser renderizado
gRenderMode = RENDER_SQUARE

#Define a abertura da boca. Inicia-se em 0 (boca fechada)
gAberturaBoca = 0

#Flag de verificação de boca aberta ou fechada
bocaAbrindo = True

#Coordenadas para movimento do objeto
gCameraX = 0
gCameraY = 0

#Ângulo de abertura de boca
gAngle = mt.pi

#Define a direção da boca
gBocaDir = 0

#Scala de projeção
gProjectionScale = 1.0;


def initGL():
	#Inicializando Matriz de Projeção
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, SCREEN_WIDTH, SCREEN_HEIGHT, 0.0, 1.0, -1.0)

	#Inicializando Matriz de modelo de exibição (Modelview)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	#Salvando a matriz padrão do modelo de exibição (modelview)
	glPushMatrix()

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

def renderSquare():
	#Renderizando o quadrado
	if (gColorMode == COLOR_MODE_CYAN):
		#Renderizando uma cor sólida, a partir da cor inicial ciano
		glBegin(GL_QUADS)
		glColor3f(0.0,1.0,1.0)
		glVertex2f(-50, -50)
		glVertex2f(50, -50)
		glVertex2f(50, 50)
		glVertex2f(-50, 50)
		glEnd()
	else:
		#Se não é ciano então pode-se assumir que deve ser multicolor
		glBegin(GL_QUADS)
		glColor3f(1,0,0)
		glVertex2f(-50, -50)
		glColor3f(1,1,0)
		glVertex2f(50, -50)
		glColor3f(0,1,0)
		glVertex2f(50, 50)
		glColor3f(0,0,1)
		glVertex2f(-50, 50)
		glEnd()

def renderCircle():
	# Variaveis para o circulo
	r = 50
	alpha = 0.0
	dalpha = mt.pi / 20

	if (gColorMode == COLOR_MODE_CYAN):
		# Renderizando um circulo com cor sólida, a partir da cor inicial ciano, utilizando tringulos
		x = r * mt.cos(alpha)
		y = r * mt.sin(alpha)
		glBegin(GL_TRIANGLES)
		glColor3f(0,1,1)
		for i in range(40):
			glVertex2f(x, y)
			glVertex2f(0.0, 0.0)
			alpha += dalpha
			x = r * mt.cos(alpha)
			y = r * mt.sin(alpha)
			glVertex2f(x, y)
		glEnd()
	else:
		x = r * mt.cos(alpha)
		y = r * mt.sin(alpha)
		glBegin(GL_TRIANGLES)
		glColor3f(1,0,0)
		for i in range(10):
			glVertex2f(x, y)
			glVertex2f(0.0, 0.0)
			alpha += dalpha
			x = r * mt.cos(alpha)
			y = r * mt.sin(alpha)
			glVertex2f(x, y)
		glColor3f(1,1,0)
		for i in range(10):
			glVertex2f(x, y)
			glVertex2f(0.0, 0.0)
			alpha += dalpha
			x = r * mt.cos(alpha)
			y = r * mt.sin(alpha)
			glVertex2f(x, y)
		glColor3f(0,1,0)
		for i in range(10):
			glVertex2f(x, y)
			glVertex2f(0.0, 0.0)
			alpha += dalpha
			x = r * mt.cos(alpha)
			y = r * mt.sin(alpha)
			glVertex2f(x, y)
		glColor3f(0,0,1);
		for i in range(10):
			glVertex2f(x, y)
			glVertex2f(0.0, 0.0)
			alpha += dalpha
			x = r * mt.cos(alpha)
			y = r * mt.sin(alpha)
			glVertex2f(x, y)
		glEnd()


def renderPacman():
	global gBocaDir, gAberturaBoca, bocaAbrindo
	r = 50
	alpha = 0.0
	dalpha = mt.pi / 40

	#Movendo a câmera para uma posição
	glTranslatef(gCameraX,gCameraY,0)

	#Rotacionando a boca na direção correta
	if (gBocaDir == 0):
		glRotatef(0,0,0,1)
	elif(gBocaDir == 2):
		glRotatef(180,0,0,1)
	elif(gBocaDir == 3):
		glRotatef(90,0,0,1)
	else:
		glRotatef(-90,0,0,1)

	x = r * mt.cos(alpha)
	y = r * mt.sin(alpha)
	glBegin(GL_TRIANGLES)
	for i in range(gAberturaBoca):
		alpha += dalpha
		x = r * mt.cos(alpha)
		y = r * mt.sin(alpha)
	glColor3f(1,1,0)
	for i in range(80 - (gAberturaBoca * 2)):
		glVertex2f(x, y)
		glVertex2f(0.0, 0.0)
		alpha += dalpha
		x = r * mt.cos(alpha)
		y = r * mt.sin(alpha)
		glVertex2f(x, y)
	glEnd()

	#Verificando e alterando abertura da boca
	if(bocaAbrindo):
		gAberturaBoca += 1
		if(gAberturaBoca > 10):
			bocaAbrindo = False
			gAberturaBoca -= 2
	else:
		gAberturaBoca -= 1
		if(gAberturaBoca < 0):
			bocaAbrindo = True
			gAberturaBoca += 2


def render():
	global gAberturaBoca, bocaAbrindo

	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)

	#Reiniciando a matriz Modelview
	glMatrixMode(GL_MODELVIEW)
	glPopMatrix()
	glLoadIdentity()

	#Salvando a matriz patrão novamente
	glPushMatrix()

	#Movendo a  para o centro da tela
	glTranslatef(SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0, 0.0)

	#Verificando qual objeto renderizar
	if (gRenderMode == RENDER_SQUARE):
		renderSquare()
	elif(gRenderMode == RENDER_CIRCLE):
		renderCircle()
	else:
		renderPacman()

	#Atualizando tela
	glutSwapBuffers()

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)

def handleKeys(key,x,y):
	global gColorMode, gRenderMode, gProjectionScale, gCameraX, gCameraY, gAngle, gBocaDir
	key = ord(key)
	#print ("key: "+str(key))
	#Se o usuário pressiona q
	if(key == 113):
		#Altera modo de cor
		if(gColorMode == COLOR_MODE_CYAN):
			gColorMode = COLOR_MODE_MULTI
		else:
			gColorMode = COLOR_MODE_CYAN
		glutPostRedisplay()
	#Se o usuário pressiona e
	elif(key == 101):
		# Ciclos através de escalas de projeção
		if(gProjectionScale == 1.0):
			#Zoom out
			gProjectionScale = 2.0
		elif(gProjectionScale == 2.0):
			#Zoom in
			gProjectionScale = 1.0

	#Se o usuário pressiona m
	elif(key == 109):
		if (gRenderMode == RENDER_SQUARE):
			gRenderMode = RENDER_CIRCLE
		elif(gRenderMode == RENDER_CIRCLE):
			gRenderMode = RENDER_PACMAN
		else:
			gRenderMode = RENDER_SQUARE

	#se o usuario pressiona a
	elif(key == 97):
		gCameraX -= 16
		gBocaDir = 2
	#se o usuario pressiona d
	elif(key == 100):
		gCameraX += 16
		gBocaDir = 0
	#se o usuario pressiona w
	elif(key == 119):
		gCameraY -= 16
		gBocaDir = 1
	#se o usuario pressiona s
	elif(key == 115):
		gCameraY += 16
		gBocaDir = 3

	
	#Atualizando matriz projeção
	glMatrixMode( GL_PROJECTION );
	glLoadIdentity()
	glOrtho(0.0, SCREEN_WIDTH * gProjectionScale, SCREEN_HEIGHT * gProjectionScale, 0.0, 1.0, -1.0)

	#Retirando a matriz salva na pilha e redefinindo
	glMatrixMode(GL_MODELVIEW)
	glPopMatrix()
	glLoadIdentity()

	#Salvando a matriz padrão novamente e a translação de câmera
	glPushMatrix()
	
