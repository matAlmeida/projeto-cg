"""
	Agora, nós iremos aplicar rotação à nossa textura. Na verdade, não iremos rotacionar a textura em si, e sim o quadrado ao qual ela está anexada.
	A função render() em LTexture agora recebe mais um argumento, que especifica quantos graus o quadrado será  rotacionado. Neste tutorial, nós queremos rotacionar a imagem em torno do próprio centro. Para isto, usaremos a função glRotate(), mas antes devemos colocar o ponto de rotação no centro da imagem. 
	A função glRotate() fará a rotação em torno do ponto de translação atual. No código, nós transladamos para o centro da imagem ao adicionar o deslocamento fornecido mais metade do tamanho do nosso quadrado. Então, nós rotacionamos o quadrado usando glRotate(). O primeiro argumento da função é quantos graus você quer rotacionar. Os próximos tres argumentos são os componentes (x, y, z) do vetor. Nosso código faz a rotação em volta do eixo z positivo. glRotate() recebe como argumento um vetor normalizado, mas irá normalizar qualquer vetor dado.
	A função update() finalmente fará alguma coisa. Nós queremos que a imagem rotacione a cada segundo, então, adicionamos o angulo de rotação dividido pelo número de frames por segundo.
	Finalmente, na função render() nós renderizamos nossa textura rotacionada. Relembrando que, o que nós estamos rotacionando é o quadrado em que a textura se anexa.
	Você deve estar se perguntando porque não fizemos o cálculo de rotação na função render(). Em um apropriado para jogos, a função de renderização nunca atualiza objeto algum, ela cuida apenas de renderizá-los como eles são. Se você nunca chamar a função update(), a função render() deverá sempre renderizar a mesma coisa.

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
