from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Modos de cor
COLOR_MODE_CYAN = 0;
COLOR_MODE_MULTI = 1;

#Modo atual de renderização de cor
gColorMode = COLOR_MODE_CYAN;

#Scala de projeção
gProjectionScale = 1.0; #Tipo: GLfloat

def initGL():
	#Inicializando Matriz de Projeção
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(0.0, SCREEN_WIDTH, SCREEN_HEIGHT, 0.0, 1.0, -1.0);

	#Inicializando Matriz de modelo de exibição (Modelview)
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	#Inicializando a tela com a cor preta
	glClearColor(0,0,0,1);

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
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	#Movendo a  para o centro da tela
	glTranslatef(SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0, 0.0);

	#Renderizando o quadrado
	if(gColorMode == COLOR_MODE_CYAN):
		#Renderizando uma cor sólida, a partir da cor inicial ciano
		glBegin(GL_QUADS);
		glColor3f(0.0,1.0,1.0);
		glVertex2f(-50, -50);
		glVertex2f(50, -50);
		glVertex2f(50, 50);
		glVertex2f(-50, 50);
		glEnd();
	else:
		#Se não é ciano então pode-se assumir que deve ser multicolor
		glBegin(GL_QUADS);
		glColor3f(1,0,0);
		glVertex2f(-50, -50);
		glColor3f(1,1,0);
		glVertex2f(50, -50);
		glColor3f(0,1,0);
		glVertex2f(50, 50);
		glColor3f(0,0,1);
		glVertex2f(-50, 50);
		glEnd();

	#Atualizando tela
	glutSwapBuffers();

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 / SCREEN_FPS, runMainLoop, val)

def handleKeys(key,x,y):
	global gColorMode
	global gProjectionScale
	key = ord(key)
	print ("key: "+str(key))
	#Se o usuário pressiona q
	if(key == 113):
		#Altera modo de cor
		if(gColorMode == COLOR_MODE_CYAN):
			gColorMode = COLOR_MODE_MULTI;
		else:
			gColorMode = COLOR_MODE_CYAN;
		glutPostRedisplay()
	elif(key == 101):
		# Ciclos através de escalas de projeção
		if(gProjectionScale == 1.0):
			#Zoom out
			gProjectionScale = 2.0;
		elif(gProjectionScale == 2.0):
			#Zoom in
			gProjectionScale = 1.0;
		glutPostRedisplay()

	#Atualizando matriz de projeção
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(0.0, SCREEN_WIDTH * gProjectionScale, SCREEN_HEIGHT * gProjectionScale, 0.0, 1.0, -1.0);
