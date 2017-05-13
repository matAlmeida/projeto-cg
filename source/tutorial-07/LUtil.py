from LTexture import *

#Constantes de Tela
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;
SCREEN_FPS = 60;

#Textura de sprite
gArrowTexture = LTexture();

#Área de sprite
gArrowClips = []
gArrowClips.append(LFRect());
gArrowClips.append(LFRect());
gArrowClips.append(LFRect());
gArrowClips.append(LFRect());

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
	#Definindo retângulos
	gArrowClips[ 0 ].x = 0
	gArrowClips[ 0 ].y = 0
	gArrowClips[ 0 ].w = 128
	gArrowClips[ 0 ].h = 128

	gArrowClips[ 1 ].x = 128
	gArrowClips[ 1 ].y = 0
	gArrowClips[ 1 ].w = 128
	gArrowClips[ 1 ].h = 128

	gArrowClips[ 2 ].x = 0
	gArrowClips[ 2 ].y = 128
	gArrowClips[ 2 ].w = 128
	gArrowClips[ 2 ].h = 128

	gArrowClips[ 3 ].x = 128
	gArrowClips[ 3 ].y = 128
	gArrowClips[ 3 ].w = 128
	gArrowClips[ 3 ].h = 128

	#Carregando textura
	if(gArrowTexture.loadTextureFromFile("arrows.png")):
		return True
	else:
		print("Não foi possível carregar a textura!")
		return False

def update():
	pass

def render():
	#Limpando o buffer de cor
	glClear(GL_COLOR_BUFFER_BIT);

	#Renderizando setas
	gArrowTexture.render( 0, 0, gArrowClips[ 0 ] )
	gArrowTexture.render( SCREEN_WIDTH - gArrowClips[ 1 ].w, 0, gArrowClips[ 1 ] )
	gArrowTexture.render( 0, SCREEN_HEIGHT - gArrowClips[ 2 ].h, gArrowClips[ 2 ] )
	gArrowTexture.render( SCREEN_WIDTH - gArrowClips[ 3 ].w, SCREEN_HEIGHT - gArrowClips[ 3 ].h, gArrowClips[ 3 ] )

	#Atualizando tela
	glutSwapBuffers()

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)
