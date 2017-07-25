"""	No tutorial-06, faremos o mesmo que o tutorial-05. Mas, desta vez carregaremos a imagem à partir de um arquivo. Visto isto, é importante que o arquivo a ser carregado esteja em uma pasta visível pelo python, de preferência na mesma em que se encontra o arquivo "main.py".
	Em "LTexture.py" nós iremos importar a classe "Image" e o método "open" da biblioteca PIL.
loadTextureFromFile() é a nossa nova função para carregar texturas a partir de um arquivo, que recebe uma string com o caminho do arquivo como argumento. Logo no começo da funçao, temos a nossa flag de textura carregada. Nas próximas linhas, nós carregamos nosso arquivo com a função open(), e convertemos os dados dos pixels para o padrão RGBA com o método de classe tobytes(). Agora, basta passar as informações para a função loadTextureFromPixels32(), apresentada no tutorial anterior, para gerar as texturas. Os índices 0 e 1 do vetor da imagem representam a largura e altura, respectivamente. 
	Após carregar a textura, é uma boa prática fechar o arquivo com close().

	Na nossa biblioteca LUtil, habilitaremos o uso de texturas com glEnable() na função initGL().
E faremos a chamada da função loadTextureFromFile() para carregar nossa imagem. Tenha certeza de que o arquivo "opengl.png" se encontre na mesma pasta que os arquivos python.

	Por fim, na função render(), faremos o mesmo que foi feito no tutorial-05.
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
