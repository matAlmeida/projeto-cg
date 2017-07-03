from LSpriteSheet import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Textura VBO renderizada 
gArrowSprites = LSpriteSheet()

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
	global gArrowSprites
	if (not gArrowSprites.loadTextureFromFile("arrows.png")):
		print("Não foi possivel carregar textura OpenGL\n")
		return False
	#Setando clips
	clip = LFRect(0,0,128,128)

	#Superior esquerda
	clip.x = 0
	clip.y = 0
	gArrowSprites.addClipSprite(clip)

	clip = LFRect(0,0,128,128)
	#Superior direita
	clip.x = 128
	clip.y = 0
	gArrowSprites.addClipSprite(clip)

	clip = LFRect(0,0,128,128)
	#Inferior esquerda
	clip.x = 0
	clip.y = 128
	gArrowSprites.addClipSprite(clip)

	clip = LFRect(0,0,128,128)
	#Inferior direita
	clip.x = 128
	clip.y = 128
	gArrowSprites.addClipSprite(clip)

	#Gerando VBO
	if(not gArrowSprites.generateDataBuffer()):
		print("Não foi possível gerar sprite sheet!\n")
		return False
	return True
		

def update():
	pass

def render():

	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)

	#Renderizando seta superior esquerda
	glLoadIdentity()
	glTranslatef(64,64,0)
	gArrowSprites.renderSprite(0)

	#Renderizando seta superior direita
	glLoadIdentity()
	glTranslatef(SCREEN_WIDTH - 64,64,0)
	gArrowSprites.renderSprite(1)

	#Renderizando seta inferior esquerda
	glLoadIdentity()
	glTranslatef(64,SCREEN_HEIGHT - 64,0)
	gArrowSprites.renderSprite(2)

	#Renderizando seta inferior direita
	glLoadIdentity()
	glTranslatef(SCREEN_WIDTH - 64,SCREEN_HEIGHT - 64,0)
	gArrowSprites.renderSprite(3)

	#Atualizando tela
	glutSwapBuffers()
