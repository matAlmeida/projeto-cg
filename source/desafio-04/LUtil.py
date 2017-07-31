from Game import *

#Constantes de Tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 320
SCREEN_FPS = 60

game = None

def initGL():
	#Definindo a janela de exibição (Viewport)
	glViewport(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

	#Inicializando Matriz de Projeção
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho( 0.0, SCREEN_WIDTH, SCREEN_HEIGHT, 0.0, 1.0, -1.0 )
    
	#Inicializando Matriz de modelo de visão (Modelview)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	glPushMatrix()
	
	#Inicializando a tela com a cor preta
	glClearColor(0,0,0,1)
	
	#Ativando textura
	glEnable(GL_TEXTURE_2D)

	#Ativando combinação
	glEnable(GL_BLEND)
	glDisable(GL_DEPTH_TEST)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

	global game
	game = Game(SCREEN_WIDTH,SCREEN_HEIGHT)
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

	#Reiniciando a matriz Modelview
	updateMatrix()

	#Renderizando superficie
	game.renderSuperficie(0,0)

	#Reiniciando a matriz Modelview
	updateMatrix()

	#Renderizando objeto
	game.renderObjeto()

	#Reiniciando a matriz Modelview
	updateMatrix()

	#Renderizando monstro
	game.renderMonster()

	#Reiniciando a matriz Modelview
	updateMatrix()

	#Renderizando monstro
	game.renderShot()

	#Reiniciando a matriz Modelview
	updateMatrix()

	#Renderizando player 1
	game.renderPlayer1()
	

	#Atualizando tela
	glutSwapBuffers()

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)

def handleKeys(key,x,y):
	game.callHandleKeys(key)

def updateMatrix():
	#Reiniciando a matriz Modelview
	glMatrixMode(GL_MODELVIEW)
	glPopMatrix()
	glLoadIdentity()
	glPushMatrix()