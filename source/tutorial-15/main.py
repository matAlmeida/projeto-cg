"""
	Neste tutorial, usaremos diferentes formas de envelopamento de textura.
	Em opengl 1.1 há apenas dois modos de envelopamento de textura, já em opengl 2.1 há cinco tipos.
	Basicamente, nosso programa é o mesmo de antes, com a diferença de que agora usamos cinco formas de envelopar a textura. Além das que já tinhamos, agora temos GL_CLAMP_TO_BORDER que fará a textura parar de ser mapeada além de 0.0 ou 1.0. GL_CLAMP_TO_EDGE que usará valores texel no limite da texture e repetir até o limite do polígono. E GL_MIRRORED_REPEAT que irá repetir a textura para valores além de 0 e 1, com a diferença de que a textura será espelhada a cada repetição.
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
	glutKeyboardFunc(handlekeys)

	#Setando a função de renderização
	glutDisplayFunc(render);

	#Definindo main loop
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop,0);

	#Iniciando GLUT main loop
	glutMainLoop();

	return 0;

main()
