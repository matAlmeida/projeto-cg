""" No primeiro tutorial o nosso objetivo principal é exibir na tela uma aplicação gráfica
que desenha na tela uma figura quadrangular. Para isso vamos utilizar as bibliotecas OpenGl.GL,
OpenGl.GLU e OpenGl.GLUT tornando a nossa aplicação portável para outras janelas.
    Vamos utilizar também a biblioteca LUtil para utilizar as funções de loop para mantes nossa
aplicação rodando e também para utilizar as funções de inicialização. As constantes da biblioteca SCREEN_WIDTH,
SCREEN_HEIGHT E SCREEN_FPS inicializam largura, altura e frames respectivamente.Ainda na biblioteca LUtil usaremos
as funções update() e render() para atualizar a lógica e processar a nossa aplicação, no nosso caso a aplicação não tem
nada para ser atualizado então nossa função update ficará sem argumentos e corpo.
    Essas funções e constantes são extremamente importantes para criar um contexto válido para a nossa aplicação
OpenGL. Vamos usar também a função glMatrixMode() que especifica qual a matriz vai ser utilizada, glLoadIdenty() para 
utilizar como auxiliar da nossa matriz. Vamos definir cor para a nossa aplicação através da função glClearColor(), o 
sistema utilizado para colorir é o RGB (Red, Green, Blue) com valores que variam de 0 à 255 e o argumento Alpha, após
isso vamos usar glGetError() para informar possíveis erros da aplicação. Dentro do render() vamos limpar o buffer de cor
com a função glClear(). Após limpar a tela vamos usar glBegin() para iniciar o desenho da nossa figura, essa função delimita
os vértices de uma figura, nessa função a ordem dos parâmetros importa, pois ligara um vértice ao seu posterior.Após delimitar
nossa figura, vamos envia-la para a Unidade de Processamento Gráfico(GPU), através da função glVertex() passando as coordenadas
x , y, z... quantas dimensões você quiser utilizar. No nosso caso vamos usar apenas 2 dimensões. Após passar as coordenadas vamos
enviar as nossas coordenadas e renderizar nossa figura usando a função glEnd(). Para atualizar a tela com a nossa figura vamos
usar glSwapBuffers(), para criar 2 buffers um para o usuário e um para memória onde vai ser atualizado e depois vai ser invertido
com o outro buffer. glutInitDisplayMode() e glutInitWindowSize() irão definir um display inicial e o tamanho inicial da nossa
janela e glutCreateWindow() criará a janela e podemos passar um nome para ela como parâmetro.
    Queremos agora que a nossa figura seja exibida constantemente na tela, para isso vamos chamar uma função de loop chamada
glutTimerFunc() para executar o frame. Agora vamos criar nossa função de loop principal que chama as outras funções de loop,
a função glutMainLoop() para fazer todos os eventos GLUT entratem em loop, fazendo assim nossa figura ser exibida na tela."""
    





from LUtil import *

def main():
	#Inicializando FreeGLUT
	# Caso esteja dando erro nessa linha no linux é preciso instalar o freglut
	# sudo apt-get install freeglut3-dev
	glutInit([])

	#Criando contexto OpenGL 2.1
	glutInitContextVersion( 2, 1 );

	#Criando janela dupla de buffer
	glutInitDisplayMode(GLUT_DOUBLE)
	glutInitWindowSize(SCREEN_WIDTH,SCREEN_HEIGHT)
	glutCreateWindow(b"OpenGL")

	#Chamando a função de inicialização da biblioteca gráfica
	if(initGL() == False):
		print("Unable to initialize graphics library!\n")
		return 1

	#Setando a função de renderização
	glutDisplayFunc(render)

	#Definindo main loop
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop,0)

	#Iniciando GLUT main loop
	glutMainLoop()

	return 0

main()
