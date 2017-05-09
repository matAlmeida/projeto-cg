from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from LTexture import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Textura do tabuleiro de damas
gCheckerBoardTexture = LTexture();

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

	#Verificando se há erros
	erro = glGetError()
	if(erro != GL_NO_ERROR):
		print("Erro ao iniciar OpenGL! %s\n", gluErrorString(erro))
		return False
	return True

def loadMedia():
	#Pixels do tabuleiro
	CHECKERBOARD_WIDTH = 128
	CHECKERBOARD_HEIGHT = 128
	CHECKERBOARD_PIXEL_COUNT = CHECKERBOARD_WIDTH * CHECKERBOARD_HEIGHT
	checkerBoard = [] #Tipo GLuint

	for i in range(0,CHECKERBOARD_PIXEL_COUNT):
		checkerBoard.append([0]*4)

	#Percorrendo através dos pixels
	for i in range(0,CHECKERBOARD_PIXEL_COUNT):
		#Se o 5º bit dos deslocamentos x e y do pixel não coincidir
		if(i // 128 & 16 ^ i % 128 & 16):
			#Definindo pixels brancos
			checkerBoard[i][0] = 0xFF; 
			checkerBoard[i][1] = 0xFF; 
			checkerBoard[i][2] = 0xFF;
			checkerBoard[i][3] = 0xFF;
		else:
			#Definindo pixels vermelhos
			checkerBoard[i][0] = 0xFF; 
			checkerBoard[i][1] = 0x00; 
			checkerBoard[i][2] = 0x00;
			checkerBoard[i][3] = 0xFF;
	#Carregando textura
	if(gCheckerBoardTexture.loadTextureFromPixels32(checkerBoard, CHECKERBOARD_WIDTH,CHECKERBOARD_HEIGHT) == False):
		print("Não foi possível carregar a textura do tabuleiro!")
		return False
	return True

def update():
	pass

def render():
	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT);

	#Obtendo coordenadas centrais
	x = (SCREEN_WIDTH - gCheckerBoardTexture.textureWidth()) / 2
	y = (SCREEN_HEIGHT - gCheckerBoardTexture.textureHeight()) / 2

	#Renderizando textura do tabuleiro
	gCheckerBoardTexture.render(x,y)

	#Atualizando tela
	glutSwapBuffers()

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)