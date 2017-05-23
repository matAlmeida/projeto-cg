from LTexture import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Textura de sprite
gCircleTexture = LTexture();

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

	#Inicializando a tela com a cor preta
	glClearColor(0,0,0,1);

	#Habilitando textura
	glEnable(GL_TEXTURE_2D)

	#Misturando
	glEnable(GL_BLEND)
	glDisable(GL_DEPTH_TEST)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

	#Verificando se há erros
	erro = glGetError()
	if(erro != GL_NO_ERROR):
		print("Erro ao iniciar OpenGL! %s\n", gluErrorString(erro))
		return False
	return True

def loadMedia():
	#Carregando textura com cor ciano
	if(not gCircleTexture.loadTextureFromFileWithColorKey("circle.png",000,255,255,255)):
		print("Não foi possível carregar textura circular!")
		return False
	return True

def update():
	pass

def render():
	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT);

	#Rnderizando o círculo
	glColor4f(1,1,1,0.5)
	gCircleTexture.render((SCREEN_WIDTH - gCircleTexture.imageWidth()) / 2,(SCREEN_HEIGHT - gCircleTexture.imageHeight()) / 2)

	#Atualizando tela
	glutSwapBuffers()

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)
