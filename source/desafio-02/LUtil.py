from Game import *

#Constantes de Tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_FPS = 120

game = Game(SCREEN_WIDTH,SCREEN_HEIGHT)

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

def render():
	# Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)

	updateMatrix()

	#Renderizando ponto
	game.renderDot()

	updateMatrix()

	#Renderizando o pacman já na direção correta do ponto
	game.renderPacman()

	#TESTE
	updateMatrix()
	game.renderObstacles()

	#Atualizando tela
	glutSwapBuffers()

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)

def updateMatrix():
	#Reiniciando a matriz Modelview
	glMatrixMode(GL_MODELVIEW)
	glPopMatrix()
	glLoadIdentity()

	#Salvando a matriz patrão novamente
	glPushMatrix()