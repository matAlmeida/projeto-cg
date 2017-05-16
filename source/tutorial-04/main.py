""" 
No tutorial-04, nós vamos realizar transformações na matriz de modelo de exibição (modelview) para mover a área que será renderizada na tela. Em outras palavras, movimentaremos a câmera para renderizar uma área diferente.
Logo no início da nossa biblioteca LUtil.py, nós definimos as coordenadas x e y da câmera, com "gCameraX" e
"gCameraY". A função initGL() é basicamente a mesma do tutorial-03, apenas adicionamos a função glPushMatrix() para salvar
a matriz de modelo de exibição na pilha. No contexto atual (OpenGL 2.1) nós temos a matriz de projeção e de modelo de
exibição (GL_PROJECTION e GL_MODELVIEW), além de outras duas apresentadas na documentação. Cada uma dessas matrizes possui uma pilha associada a ela, você pode adicionar uma cópia da matriz atual à pilha, salvando-a para mais tarde.
Como dito no começo do tutorial, nós iremos realizar translações na matriz de modelo de exibição, no entanto, diferente do tutorial-02, desta vez nós não iremos fazer a chamada das funções glLoadIdentity() e glOrtho() a cada modificação. Nós iremos empilhar uma cópia da matriz de modelo de projeção inicial movida para a posição da câmera, salvando-a para quando seja necessário fazer modificações na mesma. 
Aplicar transformações da câmera à matriz de projeção, como foi feito no tutorial-02, é considerado uma má prática visto que isto causa interferências no cálculo de iluminação e névoa. Fizemos desta forma apenas por questão de simplicidade.
Obs: A pilha de matrizes não é infinita, empilhar muitas matrizes pode causar o retorno de GL_STACK_OVERFLOW da função glGetError().
Na função handleKeys() nós modificamos a posição da câmera quando o usuário pressiona as teclas w, a, s ou d.
Já que nós mudamos a posição da câmera, alterando o valor de suas coordenadas, quando o usuário pressiona uma tecla, precisamos também alterar o valor padrão da matriz da câmera.
Primeiro, desempilhamos a antiga matriz padrão para a matriz atual com glPopMatrix(). Então, carregamos a matriz identidade na matriz atual com glLoadMatrix(). E transladamos a matriz de modelo de exibição pela deslocação da câmera, feito isto, a cena será renderizada relativamente à camera.
Agora, como nós desempilhamos a matriz padrão, precisamos empilhar a nossa nova matriz no topo da pilha com glPushMatrix() para salva-la.
Na função render(), no lugar de usar glLoadIdentity() para redefinir a matriz, usaremos glPopMatrix() para carregar a matriz que acabamos de salvar com a translação da câmera. Isto porque nós precisamos desta matriz para o próximo frame. Então, a reempilhamos imediatamente.

Agora que a matriz de modelo de exibição renderiza tudo em relação à camera, nós podemos começar a renderizar os vértices.
Renderizamos uma cena que tem o dobro do tamanho da altura e largura da camera. Os vértices nunca deslocam sua posição, apenas a câmera.

Neste tutorial, a única transformação que aplicamos foi a translação com glTranslate(). Se você quiser aumentar ou diminuir o zoom, pode escalar a matriz usando glScale(). Ou rotacioná-la, usando glRotate(). Todas presentes na documentação.
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
