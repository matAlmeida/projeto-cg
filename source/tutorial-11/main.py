"""
	Neste tutorial nós vamos definir quadrados de tamanhos diferentes para esticar a nossa textura e usaremos filtros para controlar como ficará a textura quando esticada.
	A função render() agora tem um argumento adicional: Um retângulo, para definir o quanto a textura será esticada, que terá valor padrão NULL para o caso de não desejarmos esticar a textura.
	As coordenadas da nossa textura na função render() funcionam do mesmo jeito que antes. O que muda é que iremos passar coordenadas diferentes para os vértices. Quando a nossa função possuir um retangulo de esticamento, as dimensões do nosso quadrado serão iguais ao tamanho do retângulo. Então, quando nosso quadrado com textura for renderizado, a textura será esticada para preencher o novo tamanho do quadrado.
	Declararemos algumas variáveis globais no topo da biblioteca LUtil.py. "gStretchedTexture" é a textura que nós vamos carregar, de 160x120 pixels. "gStretchRect" é o retângulo que usaremos para esticar a textura para o tamanho da tela. "gFiltering" será responsável por controlar como a textura será filtrada quando renderizada. A melhor forma de explicar como o filtro funciona é através de demonstração. Faremos isso com a nossa função handleKeys().
	Na função loadMedia() nós carregamos a nossa textura e na função render() nós a esticamos para o tamanho da tela.
	Quando o usuário pressiona a tecla 'q', nós ativamos e mudamos o filtro da nossa textura. Isto é possíve mesmo que estejamos fora da classe LTexture, contanto que tenhamos a ID da textura que desejamos realizar as operações. As funções utilizadas para tal devem lhe parecer familiares, pois já foram usadas na função que carrega a textura. 
	"GL_TEXTURE_MAG_FILTER" controla como a textura é filtrada quando esticada. O valor padrão que colocamos quando carregamos a textura é "GL_LINEAR". Isto significa que a nossa textura "mistura" os pixels ao ser esticada. Quando mudado para "GL_NEAREST", o opengl apenas pega o valor texel mais próximo, o que resulta numa imagem mais granulada.
	Vale notar que "GL_TEXTURE_MIN_FILTER" controla o filtro da textura quando ela é comprimida para um tamanho menor. Os valores dos dois não precisam ser iguais caso você queira aplicar filtros diferentes em situações diferentes.

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

	#Definindo tecla
	glutKeyboardFunc(handleKeys);

	#Setando a função de renderização
	glutDisplayFunc(render);

	#Definindo main loop
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop,0);

	#Iniciando GLUT main loop
	glutMainLoop();

	return 0;

main()
