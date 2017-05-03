from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Posição da câmera
gCameraX = 0
gCameraY = 0

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

	#Salvando a matriz padrão do modelo de exibição (modelview)
	glPushMatrix()

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

	#Carregando a Matriz que salvamos com a translação de câmera
	glMatrixMode(GL_MODELVIEW);
	glPopMatrix()

	#Salvando a matriz patrão novamente
	glPushMatrix()

	#Movendo a  para o centro da tela
	glTranslatef(SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0, 0.0);

	#Quadrado vermelho
	glBegin(GL_QUADS);
	glColor3f(1,0,0);
	glVertex2f(-SCREEN_WIDTH / 4, -SCREEN_HEIGHT / 4);
	glVertex2f(SCREEN_WIDTH / 4, -SCREEN_HEIGHT / 4);
	glVertex2f(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4);
	glVertex2f(-SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4);
	glEnd();

	#Movendo para a direita da tela
	glTranslatef(SCREEN_WIDTH,0,0)

	#Quadrado verde
	glBegin(GL_QUADS);
	glColor3f(0,1,0);
	glVertex2f(-SCREEN_WIDTH / 4, -SCREEN_HEIGHT / 4);
	glVertex2f(SCREEN_WIDTH / 4, -SCREEN_HEIGHT / 4);
	glVertex2f(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4);
	glVertex2f(-SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4);
	glEnd();

	#Movendo para a parte inferior direita da tela
	glTranslatef(0,SCREEN_HEIGHT,0)

	#Quadrado azul
	glBegin(GL_QUADS);
	glColor3f(0,0,1);
	glVertex2f(-SCREEN_WIDTH / 4, -SCREEN_HEIGHT / 4);
	glVertex2f(SCREEN_WIDTH / 4, -SCREEN_HEIGHT / 4);
	glVertex2f(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4);
	glVertex2f(-SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4);
	glEnd();

	#Movendo para baixo da tela
	glTranslatef(-SCREEN_WIDTH,0,0)

	#Quadrado amarelo
	glBegin(GL_QUADS);
	glColor3f(1,1,0);
	glVertex2f(-SCREEN_WIDTH / 4, -SCREEN_HEIGHT / 4);
	glVertex2f(SCREEN_WIDTH / 4, -SCREEN_HEIGHT / 4);
	glVertex2f(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4);
	glVertex2f(-SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4);
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
	global gCameraY,gCameraX
	key = ord(key)
	#print ("key: "+str(key))
	#Se o usuário pressiona w/a/s/d, muda a posição da câmera
	if(key == 119):
		gCameraY -= 16
	elif(key == 115):
		gCameraY += 16
	elif(key == 97):
		gCameraX -= 16
	elif(key == 100):
		gCameraX += 16
	glutPostRedisplay()

	#Retirando a matriz salva na pilha e redefinindo
	glMatrixMode(GL_MODELVIEW)
	glPopMatrix()
	glLoadIdentity()

	#Movendo a câmera para uma posição
	glTranslatef(-gCameraX,-gCameraY,0)

	#Salvando a matriz padrão novamente e a translação de câmera
	glPushMatrix()
