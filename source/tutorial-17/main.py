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
