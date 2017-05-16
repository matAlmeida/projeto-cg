"""Neste tutorial vamos utilizar o viewport para podermos trabalhar com diferentes partes da tela , essa ferramenta é muito utilizada
no desenvolvimento de jogos, pode ajudar também na portabilidade do jogo para diferentes tamanhos de tela. O viewport define a área da 
tela que iremos trabalhar .
	Nosso código do LUtil irá receber algumas mudanças. Na função initGL() vamos adicionar uma chamada a função glViewPort() , que
define qual parte da tela vamos renderizar recebendo x e y para inicio da renderização e largura e altura do nosso componente. Utilizando
VIEWPORT_MODE_FULL estamos dizendo para o programa que vamos utilizar a tela inteira para a renderização do nosso desenho. Dentro da nossa
função render() vamos usar vários tipos de viewport. Primeiro, após limpar o buffer de cor da tela, e mudas nosso componente para o centro
da tela com glTranstale(). Agora vamos utilizar VIEWPORT_MODE_HALF_CENTER que renderiza o nosso componente para apenas a metade da tela, como
estamos usando 640x480 nosso desenho será 320x240 . Utilizando VIEWPORT_MODE_HALF_TOP vamos passar para o compilador que queremos apenas
a metade superior da tela para a renderização do nosso desenho. Com VIEWPORT_MODE_QUAD podemos desenhar diversos componentes por toda a
tela , inclusive de cores diferentes. E , por último , VIEWPORT_MODE_RADAR que nos permite criar uma versão reduzida de todo o nosso 
desenho e por na tela com ele completo . É muito utilizado em jogos para fazer mapas, radares. Você já deve ter visto no Counter-Strike
Need For Speed e em outros diversos jogos.
	Após criar as viewport vamos utilizar a nossa ja conhecida função handleKeys() para percorer os vários viewport definidos no
nosso código. O código da nossa função main() é idêntico ao do tutorial 02 ."""


    






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
