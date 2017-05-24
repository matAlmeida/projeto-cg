""" Neste tutorial vamos transformar a borda branco, em uma borda transparente e a imagem central será totalmente cinza.

   Em LTexture vamos ter 3 novas funções para este tutorial. A primeira delas é loadPixelsFromFile() que carrega as os pixels
da textura que iremos utilizar. Usaremos também loadTextureFromPixels32() que cria uma textura através dos seus pixels e,
finalmente, loadTextureFromFileWithColorKey() que usa as funções loadPixelsFromFile() e loadTextureFromPixels32() para carregar
uma cor de textura com uma chave, ela recebe o caminho do arquivo e os componentes RGBA da cor a ser tornada transparente. No
início de nossa função loadPixelsFromFile() nós vamos liberar qualquer dado de textura que possa existir. Outra diferença na nossa
função é que não vamos precisar criar uma nova textura do zero, nós vamos alocar memória para receber os dados copiados através
da função memcpy() que recebe o destino dos dados, a origem dos a serem copiados e o tamanho dos dados, no nosso caso são 4 bytes
por pixel, então vamos passar 4 como terceiro argumento. Depois disso vamos sobrecarregar a função loadTextureFromPixels32()
usando pixels-membro para criar a nossa textura. Após isso vamos fazer o chaveamento de cores, vamos percorrer os nossos pixels
e se encontrarmos valores iguais RGB ou RGBA e vamos criar uma textura a partir desses pixels.
   Agora, dentro de LUtil, precisamos habilitar uma possível mistura de cores, para isso, vamos usar a função glEnable(). Depois
vamos desativar a verificação de profundidade com a função glDisable(), pois isso é utilzado apenas em aplicativos 3D ( que não
é o nosso caso neste tutorial). Por fim, vamos criar nossa mistura cm a função glBlendFunc(), primeiro argumento que vamos passar
é como os seus pixels de origem serão considerados ( ele irá verificar se o poligono que vc está criando existe), e o segundo
são os pixels de destino, vamos passar 1 como destino, pois essa função utiliza 0 à 1 como escala e a origem será alfa. Agora 
o nosso circulo terá borda transparente. Após todos esses passos, vamos renderizar nossa figura, mas antes disso vamos fazer uma
chamada a glColor4f() para passar 50% como alfa global."""







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
