from LUntil import *

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
	glutCreateWindow("OpenGL")

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
