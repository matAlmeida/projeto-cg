"""
	No tutorial-08, nós vamos renderizar uma imagem de 520x235 pixels e preenche-la numa textura de 1024x256.
	A forma como nós vamos renderizar uma textura que não é potência de dois (520x120) é tornar a imagem maior, preenchendo-a com pixels (512x128), e então cortar a parte da textura com a imagem real nela.
	Para fazer isto nossa função loadTexturefromPixels32() sofreu modificações, pois nós precisamos saber o tamanho da imagem original e o tamanho da textura preenchida. Por isso, adicionamos variáveis à classe LTexture para armazenar as dimensões tanto da imagem quanto da textura.
	Há também a adição da função powerOfTwo(), que usaremos para calcular o quanto será preciso redimensionar a textura. Por exemplo, se lhe dermos o argumento 60, ela retornará 64.
	Em LTexture.py, importaremos o arquivo LFRect, que importa a biblioteca PIL, para usar as funções de abertura de imagem. E em nosso construtor, inicializaremos as dimensões da textura e imagem.
	Em loadTextureFromFile() faremos o carregamento e conversão da imagem como de costume. Porém, desta vez devemos ter certeza de pegar a largura e altura da imagem original.
	Após carregar a imagem, usaremos a função powerOfTwo() para calcular as novas dimensões da imagem para que ela seja potência de dois. E então verificamos se as novas dimensões e as dimensões originais não são iguais. Já que se a imagem carregada já tenha dimensões em potência de dois não faz sentido redimensioná-la.
	Caso a imagem precise ser redimensionada, definiremos sua origem como sendo o canto superior-esquerdo para que quando a imagem seja preenchida os pixels sejam adicionados na parte inferior/direita. Para preencher a imagem nós esticamos o canvas para as dimensões da textura.
	Com a nossa imagem pronta, nós a enviamos para a função loadTextureFromPixels32(). O que faremos aqui é basicamente o mesmo, com a diferença de que agora nós definimos as dimensões tanto da imagem quanto da textura.
	Na função render(), definiremos as coordenadas da textura como sendo a proporção entre as dimensões da imagem original e da textura. Isto para que a parte que foi preenchida seja cortada da renderização.
	Nosso destrutor é basicamente o mesmo, com adição de que ele agora retorna as dimensões para 0.
	Preencher uma imagem de 520x235 para uma textura de dimensões 1024x256 consome muitos pixels. Por este motivo, é uma boa prática colocar várias imagens em uma textura para usar a memória da GPU da forma mais eficiente o possível.
"""

from LUtil import *

def main():
	#Inicializando FreeGLUT
	# Caso esteja dando erro nessa linha no linux é preciso instalar o freglut
	# sudo apt-get install freeglut3-dev
	glutInit([]);

	#Criando contexto OpenGL 2.1
	glutInitContextVersion(2, 1);

	#Criando janela dupla de buffer
	glutInitDisplayMode(GLUT_DOUBLE);
	glutInitWindowSize(SCREEN_WIDTH,SCREEN_HEIGHT);
	glutCreateWindow(b"OpenGL");

	#Chamando a função de inicialização da biblioteca gráfica
	if(initGL() == False):
		print("Não foi possível iniciar as bibliotecas gráficas!\n");
		return 1;

	#Carregando função loadMedia
	if(loadMedia() == False):
		print("Não foi possível carregar midia!")
		return 2

	#Setando a função de renderização
	glutDisplayFunc(render);

	#Definindo main loop
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop,0);

	#Iniciando GLUT main loop
	glutMainLoop();

	return 0;

main()
