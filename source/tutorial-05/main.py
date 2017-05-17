""" Neste tutorial vamos criar a textura de um tabuleiro de xadrez e depois vamos mapea-lo.
	
	Primeiro, vamos criar a nossa biblioteca LTEXTURE e dentro dela vamos definir a nossa classe que se chamará LTexture também.
Temos que criar um construtor e também um destrutor da nossa classe . Após isso, vamos criar os nossos métodos. Primeiro deles é o
loadTextureFromPixels32() que recebe os dados da textura a ser criada e gera uma nova textura. Temos uma função para liberar da me-
moria desalocando os dados da textura. 
	Dentro da nossa função render() vamos posicionar a nossa textura e mapea-lo e vamos por métodos de consulta da nossa classe
como getTextureId(), textureWidth() e textureHeight() , para passar o identificador , largura e altura da nossa textura. Antes de
começar a carregar os dados, temos que ter certeza que não está com lixo a textura, para depois atribuir as dimensões. Definimos
a função glGenTextures() para gerar um identificador para a nossa textura. Com a a função glTexImage2D() vamos passar todos o argumentos
para o nosso gerador de textura como: tipo, formato dos pixels com a textura armazenada, largura, altura, formato dos dados, largura
da borda, e o endereço dos pixels que você está passando. Com a função glTexParameter() vamos definir de que modo a textura será exibida.
	Na nossa função render() vamos verificar se existe uma textura a ser criada, definir a posição dela na tela e passar os dados
para cria-la. Agora vamos chamar a função glTexCoord() para passar uma textura á um vértice, de forma parecida de como passavamos uma
cor a um vértice nos tutoriais anteriores. As texturar não trabalham como coordenas x, y, z e sim com eixos, o horizontal e o vertical
e esses eixos variam de 0 à 1, mesmo que a quantidade de texturas/pixels seja superior a 1.
	Dentro de glInit() vamos adicionar a função loadMedia() para carregar os pixels da textura e glEnable() para habilitar a textu-
rização em 2D. Vamos passar 128x128 para loadMedia() para o tamanho do nosso tabuleiro. Para colorir vamos por uma verificação, se o
quinto bit de x e y são diferentes vamos passar branco, senão, passaremos vermelho (sempre com RGB). Por fim vamos rendezirar o tabuleiro
no centro da tela."""








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
