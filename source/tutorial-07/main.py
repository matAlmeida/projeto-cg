""" Neste tutorial vamos mapear apenas partes de uma textura para renderizar imagens em folhas de sprite.
	Folhas de sprite são usadas, principalmente, para animações exibindo uma sequencia de frames de imagens. Na bilioteca LFRECT
vamos definimos em que parte da imagem vamos trabalhar.
	Na biblioteca LTEXTURE, vamos definir a área da textura que iremos utilizar ( podemos passar NULL para trabalhar como ele
completo). Depois vamos definir as coordenadas de textura para aplicar no nosso vértice, temos sempre que calcular isso, pois não sa-
bemos se vamos trabalhar com a imagem completa ou parte dela, para isso temos variaveis para calcular as coordenadas que vamos usar.
Para calcular a textura temos que converter para 0/1. Ex:(Em uma imagem de 256 p , se eu quero a matede tenho que passar 0,5 e não 128
tanto para largura quanto para altura ). Com essas informaçoes podemos renderizar a nossa folha de sprite.
	Em LUTIL declaramos a nossa folha de sprite e criamos um vetor de retangulos. Na função loadMedia() definimos os retangulos e
carregamos as texturas. E na função render() renderizamos os sprites de cada array em cada canto da tela da nossa imagem."""




	



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
