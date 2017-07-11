from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from LTexture import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Loaded textures
gLeft = LTexture();
gRight = LTexture();

#Generated combined texture
gCombined = LTexture();

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
	global gLeft,gRight,gCombined
	if (not gLeft.loadTextureFromFile32("left.png")):
		print("Não foi possivel carregar textura OpenGL\n")
		return False
	if (not gRight.loadTextureFromFile32("right.png")):
		print("Não foi possivel carregar textura OpenGL\n")
		return False
	#Criando pixels brancos
	gCombined.createPixels32(gLeft.imageWidth() + gRight.imageWidth(), gLeft.imageHeight())

	#Blit imagens
	gLeft.blitPixels32(0,0,gCombined)
	gRight.blitPixels32(gLeft.imageWidth(), 0, gCombined)

	#Criando e preenchendo textura
	gCombined.blitPixels32(0,0,gCombined)
	gCombined.blitPixels32(gLeft.imageWidth,0,gCombined)

	#Se livrando de texturas antigas
	gLeft.freeTexture(gLeft)
	gRight.freeTexture(gRight)

	return True

def update():
	pass

def render():

	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()

	#Renderizando textura combinada
	gCombined.render(( SCREEN_WIDTH - gCombined.imageWidth() ) / 2, ( SCREEN_HEIGHT - gCombined.imageHeight() ) / 2)

	#Atualizando tela
	glutSwapBuffers()
