"""
	Usar glBegin() e glEnd() com glVertex(), também conhecido como modo de renderização imediato, é um modo antigo de renderizar em OpenGL e foi descontinuado. Em implementações mais modernas, faz-se o uso de VBOs.
	Neste tutorial, nós criaremos um novo tipo de dado, LTexCoord. Que servirá para lidar mais facilmente com as coordenadas das texturas.
	Cada um dos vértices do nosso quadrado texturizado tem uma posição e coordenadas de textura x,y. Então, criaremos outra estrutura para agrupar estes dados. Cada um dos vértices do nosso quadrado será representado por um objeto LVertexData2D.
	Adicionaremos também novas variáveis em LTexture para o nosso VBO e IBO. Além de duas novas funções, initVBO() e freeVBO().
	Inicializamos o VBO na função initVBO, note que ela será executada apenas quando já houver uma textura carregada. Afinal, não adianta um VBO texturizado sem textura. Primeiro, declaramos a variável de vértices e a variável de índices que serão enviadas para a GPU. Então, definimos os índices. O motivo pelo qual não iremos definir os vértices aqui é porque eles serão definidos na função de renderização. E, desta vez, usaremos a constante GL_DYNAMIC_DRAW na função glBufferData(), isto porque desta vez nós atualizaremos as posições dos vértices. Por fim, geramos os buffers e enviamos os dados para eles, removendo os vínculos logo em seguida.
	Chamaremos o initVBO sempre que carregarmos uma textura, assim o VBO estará pronto para renderizar o quadrado texturizado. A forma de carregar a textura é a mesma que já foi usada ao longo dos tutoriais, o que o VBO muda é a forma como o nosso objeto será renderizado.
	Os cálculos dos vértices e coordenadas da textura na função render(), em LTexture, também não diferem. O que nós estamos mudando não são os dados, e sim a forma como eles são enviados para a GPU.
	Após concluídos os cálculos, armazenamos os dados em um array de vértices. 
	Agora, vinculamos a textura, habilitamos coordenadas em forma de array com GL_VERTEX_ARRAY e, também, coordenadas de textura em forma de array com GL_TEXTURE_COORD_ARRAY.
	Antes que possamos renderizar o nosso quadrado, precisamos atualizar os vértices do VBO com os dados que calculamos na função render(). Primeiro, vinculamos a VBO para poder realizar as operações, e então utilizamos a função glBufferSubData(), de forma semelhante a forma como atualizamos a textura usando a função glTexSubImage2D(). O primeiro argumento especifica que tipo de dados iremos atualizar. O segundo argumento é o deslocamento para a partir de onde começar a atualizar os dados, como atualizaremos todo o VBO começamos a partir do endereço 0. O terceiro argumento é o tamanho do dado que estamos atualizando, em bytes. Neste exemplo, enviamos 4 LVertexData2D, então, é quatro vezes o tamanho de LVertexData2D. O último argumento são os novos dados.

"""

from LUtil import *

def main():
	glutInit([])

	#Criando contexto OpenGL 2.1
	glutInitContextVersion( 2, 1 );

	#Criando janela dupla de buffer
	glutInitDisplayMode(GLUT_DOUBLE)
	glutInitWindowSize(SCREEN_WIDTH,SCREEN_HEIGHT)
	glutCreateWindow(b"OpenGL")

	#Chamando a função de inicialização da biblioteca gráfica
	if(initGL() == False):
		print("Não foi possível carregar a biblioteca gráfica\n")
		return 1

	if(not loadMedia()):
		print("Não foi possível carregar a midia\n")
		return 2

	#Setando a função de renderização
	glutDisplayFunc(render)
	
	#Definindo main loop
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop,0)

	#Iniciando GLUT main loop
	glutMainLoop()

	return 0

def runMainLoop(val):
	#Lógica do Frame
	update()
	render()

	#Executando o frame mais uma vez
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop, val)

main()
