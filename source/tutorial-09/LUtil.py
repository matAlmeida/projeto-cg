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

	#Verificando se há erros
	erro = glGetError()
	if(erro != GL_NO_ERROR):
		print("Erro ao iniciar OpenGL! %s\n", gluErrorString(erro))
		return False
	return True

def loadMedia():
	#Carregando textura
	if(not gCircleTexture.loadTextureFromFile("circle.png")):
		print("Não foi possível carregar a textura!")
		return False

	#Bloqueando textura para modificação
	gCircleTexture.lock()

	#Calculando cor alvo
	colors = []
	colors.append([0]*4)
	colors[0][0] = 000
	colors[0][0] = 255
	colors[0][0] = 255
	colors[0][0] = 255

	#Substituindo a cor alvo com preto transparente
	pixels = gCircleTexture.getPixelData32()
	pixelCount = gCircleTexture.textureWidth() * gCircleTexture.textureHeigth()
	print(pixels)
	for i in range(0,pixelCount):
		if(pixels[i] == colors[0]):
			pixels[i] = 0

	#Linhas diagonais
	for y in range(0,gCircleTexture.imageHeigth()):
		for x in range(0,gCircleTexture.imageWidth()):
			if(y % 10 != x % 10):
				gCircleTexture.setPixe32(x,y,0)

	#Atualizando textura
	gCircleTexture.unlock()

	return True

def update():
	pass

def render():
	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT);

	#Rnderizando o círculo
	gCircleTexture.render((SCREEN_WIDTH - gCircleTexture.imageWidth()) / 2,(SCREEN_HEIGHT - gCircleTexture.imageHeight()) / 2)

	#Atualizando tela
	glutSwapBuffers()

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)
