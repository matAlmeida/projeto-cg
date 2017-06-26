from LFont import *

#Constantes de Tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_FPS = 60

#Textura VBO renderizada 
gFont = LFont()

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
	global gFont
	if (not gFont.loadBitmap("lazy_font.png")):
		print("Não foi possivel carregar bitmap\n")
		return False
	return True
		

def update():
	pass

def render():

	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()

	#Renderizando texto vermelho
	glColor3f(1,0,0)
	gFont.renderText(0,0,"Texto em vermelho.\nAula prática CG.")

	#Atualizando tela
	glutSwapBuffers()