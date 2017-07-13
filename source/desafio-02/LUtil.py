from random import *
from Pacman import *
from Dot import *

#Constantes de Tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_FPS = 120

#Coordenadas para movimento do objeto
gCameraX = 0
gCameraY = 0

gBocaDir = 0

#Criando pacman
pacman = Pacman(30)

#Criando ponto
dot = Dot()

#Distancia entre os objetos
distancia = 3
coordX = 50
coordY = 50

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

def renderCircle():
	# Variaveis para o circulo
	r = 5
	alpha = 0.0
	dalpha = mt.pi / 20

	# Renderizando um circulo com cor sólida, a partir da cor inicial ciano, utilizando tringulos
	x = r * mt.cos(alpha)
	y = r * mt.sin(alpha)
	glBegin(GL_TRIANGLES)

	glColor3f(1, 0, 0)
	for i in range(40):
		glVertex2f(x, y)
		glVertex2f(0.0, 0.0)
		alpha += dalpha
		x = r * mt.cos(alpha)
		y = r * mt.sin(alpha)
		glVertex2f(x, y)

	glEnd()

def render():
	global distancia, coordX, coordY
	# Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT)

	#Reiniciando a matriz Modelview
	glPopMatrix()
	glLoadIdentity()

	#Salvando a matriz padrão novamente
	glPushMatrix()

	#Se a distância entre o ponto e o pacman for menor que 10, outra coordenada do ponto é calculada
	if(distancia < 1):
		coordX = randint(50, SCREEN_WIDTH-50)
		coordY = randint(50, SCREEN_HEIGHT-50)
	
	#Renderizando ponto
	dot.render(coordX, coordY)

	#Reiniciando a matriz Modelview
	glMatrixMode(GL_MODELVIEW)
	glPopMatrix()
	glLoadIdentity()

	#Salvando a matriz patrão novamente
	glPushMatrix()

	#Iniciando renderização da bola e do pacman
	# coordPacX = SCREEN_WIDTH // 2
	# coordPacY = SCREEN_HEIGHT // 2

	#Movendo para o centro da tela
	# glTranslatef(coordPacX,coordPacY, 0.0)
	pacman.render()

	#Obtendo posição do pacman
	pacPos = pacman.getPos()

	#Movendo pacman em direção ao ponto
	movePacman(pacPos[0], pacPos[1], coordX, coordY)

	#Realizando o cálculo da distância entre o pacman e o ponto
	_dX = coordX - pacPos[0]
	_dY = coordY - pacPos[1]
	distancia = mt.sqrt(_dX**2 + _dY**2)

	#Atualizando tela
	glutSwapBuffers()

def movePacman(coordPacX, coordPacY, coordX, coordY):

	# Tá com um bug q se eu aumentar a velocidade do pacman ele fica em um loop, qqr coisa dps eu explico

	global gCameraX, gCameraY, gBocaDir

	_dX = coordX - coordPacX
	_dY = coordY - coordPacY

	if(_dX > 0):
		gCameraX += 5
		gBocaDir = 0
	elif(_dX < 0):
		gCameraX -= 5
		gBocaDir = 180
	elif(_dY < 0):
		gCameraY -= 5
		gBocaDir = 270
	elif(_dY > 0):
		gCameraY += 5
		gBocaDir = 90

	pacman.changeDirection(gBocaDir)

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)

def handleKeys(key,x,y):
	global gRenderMode, gCameraX, gCameraY, gAngle, gBocaDir
	key = ord(key)
	rot = 0.0

	#se o usuario pressiona a
	if(key == 97):
		# pacman.rotate(90)
		gCameraX -= 5
		gBocaDir = 180
	#se o usuario pressiona d
	elif(key == 100):
		gCameraX += 5
		gBocaDir = 0
	#se o usuario pressiona w
	elif(key == 119):
		gCameraY -= 5
		gBocaDir = 270
	#se o usuario pressiona s
	elif(key == 115):
		gCameraY += 5
		gBocaDir = 90
	elif(key == 98):
		rot += mt.pi / 20

	pacman.changeDirection(gBocaDir)
	pacman.rotate(rot)

	
	#Atualizando matriz projeção
	glMatrixMode( GL_PROJECTION );
	glLoadIdentity()
	glOrtho(0.0, SCREEN_WIDTH, SCREEN_HEIGHT, 0.0, 1.0, -1.0)

	#Retirando a matriz salva na pilha e redefinindo
	glMatrixMode(GL_MODELVIEW)
	glPopMatrix()
	glLoadIdentity()

	#Salvando a matriz padrão novamente e a translação de câmera
	glPushMatrix()
	