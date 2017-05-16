""" No tutorial 02 vamos utilizar um sistema de coordenadas com as dimensões 640x480 e vamos também colori-lo. Primeiro,
na nossa biblioteca auxiliar LUtil, vamos definir o tamanho da tela que iremos trabalhar e definir a quantidade de frames
por segundo com as contantes SCREEN_WIDTH, SCREEN_HEIGHT E SCREEN_FPS . Vamos também iniciar as cores do desenho como a
constante COLOR_MODE_CYAN = 0 E COLOR_MODE_MULTI = 1 . 
    Ainda em LUtil vamos chamar a função glInit() e vamos fazer os processos idênticos do Tutorial 01 , usando as funções
glMatrixMode() e glLoadIdenty() mas adicionaremos uma nova função, a glOrtho() que multiplica a matriz atual por uma matriz
ortográfica (2 dimensões) usando os valores esquerdo, direito , cima , baixo, perto e longe como argumentos. A nossa função
update() continuará sem utilidade. Na função render() vamos limpar o buffer de cor com glClear() e vamos utlizar uma matriz
Model_View para aplicar mudanças na nossa figura. A diferença entre a Model_View e a Model_Projection é que uma controla a 
visualização e a outra controla a renderização. Vamos usar a função glTranslate() para mudar nossa figura do canto superior
esquerdo , para o centro da tela. Após isso, vamos definir a próxima cor do vértice com a função glColor() usando parâmetros
do sistema RGB e vamos definir a posição do vértice com glVertex(). Observe que quando enviamos um vertice o OpenGL toma como
cor base a ultima cor passada. Não podemos esquecer de atualizar a tela com a função glutSwapBuffers().
    Outra novidade é a função handleKeys() que vamos usar para verificar a tecla pressionada e realizar uma ação se tal 
condição for satisfeita. No nosso caso se 'q' for pressionado ele troca de Ciano para Colorido ou vice-versa. Também vamos usar
a tecla 'e' para mudar a escala do nosso desenho , usando a função gProjectionScale, vamos mudar ela para o dobro do tamanho,
depois para metade do tamanho e depois ela volta para o tamanho inicial. 
    A função main() é exatamente igual a do Tutorial 01 , muda apenas a adição de glutKeyboardFunc() para o uso do teclado."""





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
		print("Unable to initialize graphics library!\n");
		return 1;

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
