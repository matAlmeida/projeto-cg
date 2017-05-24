""" Neste tutorial nos vamos criar um circulo com seu background preto e adicionar listras na sua diagonal. A nossa biblioteca
LTexture terá a adição de uma nova variável, se chamará mPixels que vai armazenar os dados dos pixels da textura que iremos
manipular. Temos também, ainda em LTexture a função lock() que obtém os pixels da textura para operarmos com ele,e a função
unlock() que envia os dados depois de operados para a textura. A função getPixelData() retorna para nós um apontador para o 
vetor de pixels e as funções getPixel32() e setPixel32() enviam e recebem respectivamente pixels individuais da nossa textura.
   Agora, antes de chamarmos nossa função FreeTexture(), temos que verificar se existe algum pixel no nosso vetor para ser 
liberado. Para usar a função lock() temos que verificar se ela já não esta manipulando alguma textura e se os pixels da nossa
textura existem. Após essa verificação vamos alocar memória para nossos dados que serão copiados. Após isso nós vamos associar
os dados recebidos com a função glTexImage() e depois vamos desvincular essa textura. Após terminar as nossas manipulações
nós vamos enviar de volta os pixels da nossa textura, para isso, vamos utilizar a função glTexSubImage2D() que especifica
uma textura bidimensional e passa a uma textura destino e depois vamos atualizar nossa textura. Uma coisa importante a salientar
é que nossos pixels de textura ficam armazenados em uma matriz unidimensional, ou seja, em um vetor, assim, para obter uma coor-
denada 2D você tem que transformar em um índice 1D.
   Dentro de LUtil nós vamos carregar nossa textura e usar lock() para obter os pixels e vamos bloquea-lo para podermos modifica-
los. Vamos criar a nossa cor preta para passar aos pixels, depois vamos percorrer todos os pixels, se algum deles for o nosso
alvo, nós vamos modifica-lo para um preto transparente. Agora vamos percorrer todas as linhas e colunas e vamos mudar algumas
delas para colorir nossa diagonal. Depois disso usamos unlock() para desbloquear a textura e atualizamos a mesma.
   E, dentro de render(), vamos processar a nossa figura."""
   

	
	

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
