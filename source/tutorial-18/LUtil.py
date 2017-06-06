
from LTexture import*


#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Textura VBO renderizada 
gVBOTexture = LTexture()

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
	global gVBOTexture
	if (not gVBOTexture.loadTextureFromFile("opengl.png")):
		print("Não foi possivel carregar textura OpenGL\n")
		return False
	return True
		

def update():
	pass

def render():

	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)

	#Inicializando matriz de exibição 
	glLoadIdentity()

	#Renderizando textura do quadrado usando VBOs
	gVBOTexture.render((SCREEN_WIDTH - gVBOTexture.imageWidth()) / 2 , (SCREEN_HEIGHT - gVBOTexture.imageHeight()) / 2 )

	#Atualizando tela
	glutSwapBuffers()